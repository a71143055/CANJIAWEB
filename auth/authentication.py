"""
CANJIA 인증 모듈
이메일/비밀번호 기반 로그인 + 2차 인증
"""

from datetime import datetime, timedelta
from functools import wraps
from flask import session, redirect, url_for
import secrets
import string

def login_required(f):
    """로그인 필수 데코레이터"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def generate_two_factor_code():
    """6자리 2차 인증 코드 생성"""
    return ''.join(secrets.choice(string.digits) for _ in range(6))

def send_2fa_code_email(email, code):
    """
    2차 인증 코드를 이메일로 전송
    실제 배포 시 이메일 서비스(SMTP) 연동 필요
    """
    # TODO: 이메일 전송 로직 구현
    # from flask_mail import Mail, Message
    # msg = Message(
    #     subject=f'CANJIA 2단계 인증 코드: {code}',
    #     recipients=[email],
    #     html=f'<p>인증 코드: <strong>{code}</strong></p><p>10분 내에 입력해주세요.</p>'
    # )
    # mail.send(msg)
    
    # 개발 환경에서는 콘솔에 출력
    print(f"[2FA] {email}에 인증 코드 전송: {code}")
    return True

def verify_password_strength(password):
    """
    비밀번호 강도 확인
    최소 6자, 숫자 포함 권장
    """
    if len(password) < 6:
        return False, "최소 6자 이상이어야 합니다"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    # 강도: 약(1단계) - 중간(2단계) - 강(3단계)
    strength = sum([has_upper, has_lower, has_digit])
    
    return True, strength

