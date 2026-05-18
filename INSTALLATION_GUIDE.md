# CANJIA 웹사이트 - 프로젝트 구축 완료! 🎉

## 📌 프로젝트 개요

제주 산업 발전 및 네트워크 공동체(CANJIA) 웹사이트가 완성되었습니다!

**프로젝트명**: CANJIA (Community for Association & Network in Jeju Industry Association)
**작성인**: 정구영
**작성일**: 2026년 05월 15일

---

## 📁 프로젝트 구조

```
CANJIAWEB/
├── 📄 app.py                    # Flask 메인 애플리케이션
├── 📄 config.py                 # 설정 파일
├── 📄 setup.py                  # 초기 설정 스크립트
├── 📄 requirements.txt          # Python 의존성
├── 📄 .env.example              # 환경 변수 예제
├── 📄 .gitignore                # Git 제외 파일
├── 📄 README.md                 # 프로젝트 문서
├── 📄 QUICKSTART.md             # 빠른 시작 가이드
├── 📁 templates/                # HTML 템플릿
│   ├── base.html                # 기본 레이아웃
│   ├── index.html               # 홈페이지
│   ├── intro.html               # 소개 페이지
│   ├── login.html               # 로그인
│   ├── signup.html              # 회원가입
│   ├── profile.html             # 프로필 수정
│   ├── fields.html              # 분야 탐색
│   ├── field_detail.html        # 분야 상세
│   ├── documents.html           # 내 문서
│   ├── document_edit.html       # 문서 작성/수정
│   ├── document_view.html       # 문서 보기
│   ├── 404.html                 # 404 에러
│   └── 500.html                 # 500 에러
├── 📁 static/                   # 정적 파일
│   ├── css/
│   │   └── style.css            # 메인 스타일 (반응형 디자인)
│   ├── js/
│   │   └── main.js              # 메인 스크립트
│   └── images/                  # 이미지 폴더
├── 📁 auth/                     # 인증 모듈
│   └── authentication.py        # Microsoft OAuth 처리
└── 📁 documents/                # 문서 관리 모듈
    └── document_manager.py      # 문서 CRUD 작업
```

---

## 🎯 구현된 주요 기능

### 1. 사용자 관리
✅ Microsoft OAuth 2.0 기반 로그인/가입
✅ 프로필 작성 및 수정
✅ 관심 분야 설정
✅ 2차 인증 지원

### 2. 문서 시스템
✅ Google Docs 스타일 편집기
✅ 마크다운 형식 지원
✅ 분야별 문서 분류
✅ 공개/비공개 설정
✅ 댓글 및 피드백 기능

### 3. 분야 탐색
✅ 7가지 발전 분야 (AGI, ACTF, 수영, 스키, 암벽등반, 카페취업, 기술연마)
✅ 분야별 문서 검색
✅ 인기 문서 및 최신 문서
✅ 분야별 커뮤니티

### 4. 웹사이트 UI/UX
✅ 반응형 디자인 (모바일/태블릿/데스크탑)
✅ 현대적인 그래디언트 디자인
✅ 직관적인 네비게이션
✅ 부드러운 애니메이션

---

## 🚀 빠른 시작

### 1단계: 폴더 진입
```bash
cd "c:\Users\USER\OneDrive\바탕 화면\CANJIAWEB"
```

### 2단계: 가상 환경 생성 (Windows)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3단계: 의존성 설치
```bash
pip install -r requirements.txt
```

### 4단계: 환경 변수 설정
```bash
copy .env.example .env
```

텍스트 편집기에서 `.env` 파일을 열고 필요한 설정을 입력하세요.

### 5단계: 초기 설정
```bash
python setup.py
```

### 6단계: 애플리케이션 실행
```bash
python app.py
```

### 7단계: 브라우저 접속
```
http://localhost:5000
```

---

## 📚 데이터베이스 모델

### User (사용자)
- id: 사용자 ID
- email: 이메일 (고유)
- name: 이름
- profile_image: 프로필 이미지
- bio: 소개글
- fields: 관심 분야 (쉼표로 구분)
- created_at: 생성 날짜
- is_verified: 이메일 검증 여부
- two_factor_enabled: 2차 인증 활성화

### Document (문서)
- id: 문서 ID
- user_id: 작성자 ID
- title: 문서 제목
- content: 문서 내용
- field: 분야 (AGI, ACTF, 수영 등)
- is_public: 공개 여부
- created_at: 작성 날짜
- updated_at: 수정 날짜

### Comment (댓글)
- id: 댓글 ID
- document_id: 문서 ID
- user_id: 작성자 ID
- content: 댓글 내용
- created_at: 작성 날짜

---

## 🔧 주요 기술 스택

### 백엔드
- **Flask**: 웹 프레임워크
- **SQLAlchemy**: ORM
- **SQLite**: 데이터베이스
- **Flask-Session**: 세션 관리
- **MSAL**: Microsoft 인증

### 프론트엔드
- **HTML5**: 마크업
- **CSS3**: 스타일링 (반응형)
- **Vanilla JavaScript**: 클라이언트 로직

---

## 🌍 웹사이트 라우트

### 페이지 라우트
- `GET /` - 홈페이지
- `GET /intro` - 소개 페이지
- `GET /fields` - 분야 탐색
- `GET /field/<field_name>` - 분야 상세
- `GET /documents` - 내 문서
- `GET /auth/profile` - 프로필

### 문서 라우트
- `GET /document/<id>` - 문서 보기
- `GET /document/new` - 문서 작성 페이지
- `POST /document/new` - 문서 생성
- `GET /document/<id>/edit` - 문서 수정 페이지
- `POST /document/<id>/edit` - 문서 수정
- `POST /document/<id>/delete` - 문서 삭제

### 인증 라우트
- `GET /auth/login` - 로그인 페이지
- `GET /auth/signup` - 회원가입 페이지
- `GET /auth/logout` - 로그아웃

---

## 💡 주요 특징

### 1. 반응형 디자인
- 모든 기기에서 최적화된 UI
- 모바일 친화적 인터페이스
- 터치 제스처 지원

### 2. 현대적 디자인
- 그래디언트 배경
- 부드러운 애니메이션
- 카드 기반 레이아웃
- 직관적인 색상 체계

### 3. 사용자 중심 기능
- 쉬운 회원가입
- 직관적인 문서 작성
- 빠른 분야 탐색
- 활발한 커뮤니티

### 4. 보안
- Microsoft OAuth 인증
- 세션 기반 관리
- CSRF 보호
- SQL Injection 방지

---

## 📖 사용 예시

### 1. 회원가입
1. 홈페이지에서 "시작하기" 클릭
2. 이메일, 이름, 비밀번호 입력
3. 이용약관 동의
4. 회원가입 완료

### 2. 첫 문서 작성
1. 로그인 후 "새 문서 작성" 클릭
2. 제목 입력 (예: "AGI 개발 경험")
3. 분야 선택 (예: AGI)
4. 마크다운 형식으로 내용 작성
5. 공개 설정 후 작성 완료

### 3. 분야 탐색
1. "분야 탐색" 메뉴 클릭
2. 원하는 분야 선택 (예: 수영)
3. 분야의 모든 문서 보기
4. 관심 있는 문서 읽기
5. 댓글로 피드백 남기기

---

## 🎨 디자인 특징

### 색상 팔레트
- **Primary**: #667eea (보라색)
- **Secondary**: #764ba2 (짙은 보라)
- **Success**: #48bb78 (초록색)
- **Danger**: #f56565 (빨강색)
- **Warning**: #ed8936 (주황색)

### 폰트
- 기본: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- 일관된 라인 높이: 1.6

### 반응형 중단점
- 모바일: < 768px
- 태블릿: 768px - 1024px
- 데스크탑: > 1024px

---

## 🔐 보안 설정

### 구현된 보안 기능
✅ 환경 변수로 민감한 정보 관리
✅ HTTPS 준비 (배포 시 필수)
✅ 세션 쿠키 보안 설정
✅ CSRF 토큰 지원
✅ 사용자 입력 검증

### 보안 권장사항
1. .env 파일을 절대 공개하지 않기
2. 프로덕션 환경에서 DEBUG=False
3. 정기적인 의존성 업데이트
4. HTTPS 사용 필수
5. SQL 입력값 검증

---

## 📝 설정 파일

### .env 파일 필수 항목
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///canjia.db
MICROSOFT_CLIENT_ID=your-client-id
MICROSOFT_CLIENT_SECRET=your-client-secret
```

### config.py의 주요 설정
- `SECRET_KEY`: Flask 세션 비밀키
- `SQLALCHEMY_DATABASE_URI`: 데이터베이스 연결
- `MICROSOFT_CLIENT_ID/SECRET`: OAuth 설정
- `CANJIA_FIELDS`: 7가지 분야 정의
- `CANJIA_GOALS`: 7가지 목표 정의

---

## 🚀 배포 준비

### Heroku 배포 (예시)
```bash
# Procfile 생성
echo "web: python app.py" > Procfile

# Heroku 로그인
heroku login

# 앱 생성
heroku create your-app-name

# 환경 변수 설정
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-secret-key

# 배포
git push heroku main
```

---

## 🎓 학습 자료

### CANJIA의 7가지 분야에 대해 배우기

1. **AGI (범용 인공 지능)**
   - 머신러닝 기초
   - 딥러닝 이해
   - 자연어 처리

2. **ACTF (안드로이드 사이보그 트랜스포머)**
   - 로봇 공학
   - 센서 기술
   - 자동화

3. **수영**
   - 무중력 환경 체험
   - 신체 유연성
   - 호흡 기술

4. **스키 (스카이 다이빙)**
   - 중력 활용
   - 신체 적응
   - 안전 기술

5. **암벽등반**
   - 근력 훈련
   - 정신력 단련
   - 문제 해결

6. **카페취업**
   - 제주도 경제
   - 취업 기술
   - 커뮤니티 활동

7. **기술연마**
   - 바리스타 기술
   - 실무 경험
   - 기술 개발

---

## 📞 문제 해결

### 자주 묻는 질문 (FAQ)

**Q: 포트 5000이 이미 사용 중이에요**
A: `PORT=5001 python app.py` 명령으로 다른 포트 사용

**Q: 데이터베이스 오류가 발생해요**
A: `rm canjia.db` 후 `python app.py` 실행

**Q: Microsoft OAuth 설정이 안 되요**
A: Azure Portal에서 애플리케이션 등록 후 Client ID/Secret 설정

---

## 🎉 축하합니다!

CANJIA 웹사이트가 준비되었습니다!

### 다음 단계
1. 로컬에서 테스트
2. 기능 커스터마이징
3. Microsoft OAuth 실제 설정
4. 배포 준비

---

## 📄 라이선스

MIT License - 자유롭게 사용, 수정, 배포 가능

---

**CANJIA - 제주 산업 발전 및 네트워크 공동체**

🚀 경제 자립 | 취미 생활 | 기술 증진 | 회원 모집 | 주거 이전 | 생명 연장 | 우주 유영

제주도에서 시작되는 새로운 미래를 함께 만들어가겠습니다!
