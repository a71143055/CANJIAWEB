"""
CANJIA Flask 애플리케이션 메인 파일
제주 산업 발전 및 네트워크 공동체 - CANJIA
"""

from flask import Flask, render_template, session, redirect, url_for, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime, timedelta
import secrets
import string
from config import config

# Flask 앱 초기화
app = Flask(__name__)
app.config.from_object(config['development'])
app.secret_key = app.config.get('SECRET_KEY') or 'canjia-secret-key-2026'

# 데이터베이스 초기화
db = SQLAlchemy(app)

# 세션 초기화
Session(app)

# ============================================================
# 유틸리티 함수
# ============================================================

def generate_two_factor_code():
    """6자리 2차 인증 코드 생성"""
    return ''.join(secrets.choice(string.digits) for _ in range(6))

# ============================================================
# 데이터베이스 모델
# ============================================================

class User(db.Model):
    """사용자 모델"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    profile_image = db.Column(db.String(500))
    bio = db.Column(db.Text)
    fields = db.Column(db.String(500))  # 관심 분야 (쉼표로 구분)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_verified = db.Column(db.Boolean, default=False)
    two_factor_enabled = db.Column(db.Boolean, default=True)  # 기본 활성화
    two_factor_method = db.Column(db.String(20), default='email')  # 'email' 또는 'app'
    
    documents = db.relationship('Document', backref='author', lazy=True)
    
    def set_password(self, password):
        """비밀번호 해시 설정"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """비밀번호 검증"""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.email}>'

class TwoFactorCode(db.Model):
    """2차 인증 코드 모델"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    code = db.Column(db.String(6), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, default=lambda: datetime.utcnow() + timedelta(minutes=10))
    is_used = db.Column(db.Boolean, default=False)
    used_at = db.Column(db.DateTime)
    
    user = db.relationship('User', backref='two_factor_codes')
    
    def is_expired(self):
        """코드 만료 여부 확인"""
        return datetime.utcnow() > self.expires_at
    
    def __repr__(self):
        return f'<TwoFactorCode {self.user_id}>'

class Document(db.Model):
    """사용자 문서 모델"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    field = db.Column(db.String(50), nullable=False)  # AGI, ACTF, 수영 등
    is_public = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Document {self.title}>'

class Comment(db.Model):
    """문서 댓글 모델"""
    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    author = db.relationship('User', backref='comments')
    document = db.relationship('Document', backref='comments')

# ============================================================
# 라우트 정의
# ============================================================

@app.route('/')
def index():
    """홈페이지"""
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('home.html', user=user)
    return render_template('index.html')

@app.route('/intro')
def intro():
    """소개 페이지"""
    return render_template('intro.html')

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    """로그인 페이지"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            # 로그인 성공 - 2차 인증 필요
            if user.two_factor_enabled:
                # 2차 인증 코드 생성
                code = generate_two_factor_code()
                tfa_code = TwoFactorCode(user_id=user.id, code=code)
                db.session.add(tfa_code)
                db.session.commit()
                
                # 임시 세션에 사용자 ID 저장
                session['pending_user_id'] = user.id
                session['pending_email'] = user.email
                
                # 실제 배포 시 이메일 발송 로직 추가
                print(f"2FA Code for {email}: {code}")
                flash('이메일로 인증 코드를 보냈습니다.', 'info')
                
                return redirect(url_for('verify_2fa'))
            else:
                # 2FA 미사용시 바로 로그인
                session['user_id'] = user.id
                return redirect(url_for('index'))
        else:
            flash('이메일 또는 비밀번호가 잘못되었습니다.', 'error')
    
    return render_template('login.html')

@app.route('/auth/signup', methods=['GET', 'POST'])
def signup():
    """회원가입 페이지"""
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        
        # 유효성 검사
        if not email or not name or not password:
            flash('모든 필드를 입력해주세요.', 'error')
            return render_template('signup.html')
        
        if password != password_confirm:
            flash('비밀번호가 일치하지 않습니다.', 'error')
            return render_template('signup.html')
        
        if len(password) < 6:
            flash('비밀번호는 최소 6자 이상이어야 합니다.', 'error')
            return render_template('signup.html')
        
        # 중복 이메일 확인
        if User.query.filter_by(email=email).first():
            flash('이미 가입된 이메일입니다.', 'error')
            return render_template('signup.html')
        
        # 새 사용자 생성
        user = User(email=email, name=name)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('회원가입이 완료되었습니다. 로그인해주세요.', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/auth/verify-2fa', methods=['GET', 'POST'])
def verify_2fa():
    """2차 인증 코드 검증"""
    if 'pending_user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        code = request.form.get('code')
        pending_user_id = session.get('pending_user_id')
        
        # 최근 미사용 인증 코드 찾기
        tfa_code = TwoFactorCode.query.filter_by(
            user_id=pending_user_id,
            code=code,
            is_used=False
        ).order_by(TwoFactorCode.created_at.desc()).first()
        
        if tfa_code and not tfa_code.is_expired():
            # 코드 사용 처리
            tfa_code.is_used = True
            tfa_code.used_at = datetime.utcnow()
            db.session.commit()
            
            # 세션에 사용자 저장
            session['user_id'] = pending_user_id
            session.pop('pending_user_id', None)
            session.pop('pending_email', None)
            
            flash('로그인되었습니다.', 'success')
            return redirect(url_for('index'))
        else:
            flash('인증 코드가 잘못되었거나 만료되었습니다.', 'error')
    
    pending_email = session.get('pending_email', '')
    return render_template('verify_2fa.html', email=pending_email)

@app.route('/auth/profile')
def profile():
    """프로필 작성 페이지"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template('profile.html', user=user, fields=app.config['CANJIA_FIELDS'])

@app.route('/fields')
def fields():
    """분야 구성 바 (대시보드)"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template('fields.html', user=user, fields=app.config['CANJIA_FIELDS'])

@app.route('/field/<field_name>')
def field_detail(field_name):
    """특정 분야 상세 페이지"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    documents = Document.query.filter_by(field=field_name, is_public=True).all()
    
    return render_template('field_detail.html', 
                         user=user, 
                         field_name=field_name,
                         documents=documents,
                         fields=app.config['CANJIA_FIELDS'])

@app.route('/documents')
def documents_list():
    """문서 목록 페이지"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    user_documents = Document.query.filter_by(user_id=user.id).all()
    
    return render_template('documents.html', 
                         user=user,
                         documents=user_documents)

@app.route('/document/new', methods=['GET', 'POST'])
def create_document():
    """새 문서 작성 페이지"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        field = request.form.get('field')
        is_public = request.form.get('is_public') == 'on'
        
        doc = Document(
            user_id=session['user_id'],
            title=title,
            content=content,
            field=field,
            is_public=is_public
        )
        db.session.add(doc)
        db.session.commit()
        
        return redirect(url_for('documents_list'))
    
    user = User.query.get(session['user_id'])
    return render_template('document_edit.html', 
                         user=user,
                         fields=app.config['CANJIA_FIELDS'])

@app.route('/document/<int:doc_id>')
def view_document(doc_id):
    """문서 보기 페이지"""
    doc = Document.query.get_or_404(doc_id)
    user = User.query.get(session.get('user_id'))
    
    return render_template('document_view.html',
                         document=doc,
                         user=user)

@app.route('/document/<int:doc_id>/edit', methods=['GET', 'POST'])
def edit_document(doc_id):
    """문서 수정 페이지"""
    doc = Document.query.get_or_404(doc_id)
    
    if 'user_id' not in session or session['user_id'] != doc.user_id:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        doc.title = request.form.get('title')
        doc.content = request.form.get('content')
        doc.field = request.form.get('field')
        doc.is_public = request.form.get('is_public') == 'on'
        db.session.commit()
        
        return redirect(url_for('view_document', doc_id=doc.id))
    
    user = User.query.get(session['user_id'])
    return render_template('document_edit.html',
                         user=user,
                         document=doc,
                         fields=app.config['CANJIA_FIELDS'])

@app.route('/document/<int:doc_id>/delete', methods=['POST'])
def delete_document(doc_id):
    """문서 삭제"""
    doc = Document.query.get_or_404(doc_id)
    
    if 'user_id' not in session or session['user_id'] != doc.user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    db.session.delete(doc)
    db.session.commit()
    
    return redirect(url_for('documents_list'))

@app.route('/api/user/profile', methods=['GET', 'POST'])
def api_user_profile():
    """API: 사용자 프로필 조회/수정"""
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        user.name = request.json.get('name', user.name)
        user.bio = request.json.get('bio', user.bio)
        user.fields = request.json.get('fields', user.fields)
        db.session.commit()
        
        return jsonify({
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'bio': user.bio,
            'fields': user.fields
        })
    
    return jsonify({
        'id': user.id,
        'email': user.email,
        'name': user.name,
        'bio': user.bio,
        'fields': user.fields,
        'created_at': user.created_at.isoformat()
    })

@app.route('/auth/logout')
def logout():
    """로그아웃"""
    session.clear()
    flash('로그아웃되었습니다.', 'success')
    return redirect(url_for('index'))

@app.route('/auth/settings')
def auth_settings():
    """2FA 설정 페이지"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    return render_template('auth_settings.html', user=user)

@app.route('/auth/toggle-2fa', methods=['POST'])
def toggle_2fa():
    """2FA 활성화/비활성화"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    action = request.form.get('action')
    
    if action == 'enable':
        user.two_factor_enabled = True
        flash('2차 인증이 활성화되었습니다.', 'success')
    elif action == 'disable':
        user.two_factor_enabled = False
        flash('2차 인증이 비활성화되었습니다.', 'warning')
    
    db.session.commit()
    return redirect(url_for('auth_settings'))

@app.route('/auth/change-password', methods=['POST'])
def change_password():
    """비밀번호 변경"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')
    
    # 현재 비밀번호 검증
    if not user.check_password(current_password):
        flash('현재 비밀번호가 잘못되었습니다.', 'error')
        return redirect(url_for('auth_settings'))
    
    # 새 비밀번호 일치 확인
    if new_password != confirm_password:
        flash('새 비밀번호가 일치하지 않습니다.', 'error')
        return redirect(url_for('auth_settings'))
    
    # 비밀번호 길이 확인
    if len(new_password) < 6:
        flash('비밀번호는 최소 6자 이상이어야 합니다.', 'error')
        return redirect(url_for('auth_settings'))
    
    # 비밀번호 변경
    user.set_password(new_password)
    db.session.commit()
    
    flash('비밀번호가 변경되었습니다.', 'success')
    return redirect(url_for('auth_settings'))

@app.errorhandler(404)
def not_found(error):
    """404 에러 핸들러"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """500 에러 핸들러"""
    db.session.rollback()
    return render_template('500.html'), 500

# ============================================================
# 애플리케이션 시작
# ============================================================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
