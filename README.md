# CANJIA - 제주 산업 발전 및 네트워크 공동체

## 프로젝트 소개

CANJIA (Community for Association & Network in Jeju Industry Association)는 제주도 기반의 산업 발전 및 네트워크 공동체 웹 플랫폼입니다.

- **작성인**: 정구영
- **작성일**: 2026년 05월 15일
- **약자**: CANJIA

## 주요 기능

### 1. 회원 관리
- Microsoft Client 기반 인증
- 프로필 작성 및 수정
- 관심 분야 설정
- 2차 인증 지원

### 2. 분야 탐색
CANJIA는 7가지 발전 분야를 제공합니다:

1. **AGI (범용 인공 지능)** - 사람 수준의 AI 개발
2. **ACTF (안드로이드 사이보그 트랜스포머)** - 미래 로봇 기술
3. **수영** - 무중력 환경 체험
4. **스키** - 중력 활용 스포츠
5. **암벽등반** - 신체 능력 단련
6. **카페취업** - 제주도 경제 활동 탐색
7. **기술연마** - 실무 기술 습득

### 3. 문서 관리
- Google Docs 스타일의 편집 인터페이스
- 분야별 문서 작성 및 공유
- 마크다운 형식 지원
- 공개/비공개 설정
- 댓글 및 피드백 기능

### 4. 커뮤니티
- 사용자 프로필 탐색
- 문서 공유 및 협업
- 댓글 및 토론
- 분야별 그룹

## 프로젝트 구조

```
CANJIAWEB/
├── app.py                 # Flask 메인 애플리케이션
├── config.py             # 설정 파일
├── requirements.txt      # Python 의존성
├── README.md            # 프로젝트 문서
├── templates/           # HTML 템플릿
│   ├── base.html        # 기본 템플릿
│   ├── index.html       # 홈페이지
│   ├── intro.html       # 소개 페이지
│   ├── login.html       # 로그인 페이지
│   ├── signup.html      # 회원가입 페이지
│   ├── profile.html     # 프로필 수정 페이지
│   ├── fields.html      # 분야 탐색 페이지
│   ├── field_detail.html # 분야 상세 페이지
│   ├── documents.html   # 문서 목록 페이지
│   ├── document_edit.html # 문서 작성/수정 페이지
│   ├── document_view.html # 문서 보기 페이지
│   ├── 404.html         # 404 에러 페이지
│   └── 500.html         # 500 에러 페이지
├── static/
│   ├── css/
│   │   └── style.css    # 메인 스타일시트
│   ├── js/
│   │   └── main.js      # 메인 JavaScript
│   └── images/          # 이미지 폴더
├── auth/                # 인증 관련 모듈
└── documents/           # 문서 관련 모듈
```

## 설치 및 실행

### 필수 요구사항
- Python 3.8 이상
- pip (Python 패키지 관리자)

### 설치 단계

1. **저장소 클론** (또는 폴더 진입)
```bash
cd CANJIAWEB
```

2. **가상 환경 생성** (권장)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **의존성 설치**
```bash
pip install -r requirements.txt
```

4. **환경 변수 설정** (.env 파일 생성)
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
MICROSOFT_CLIENT_ID=your-microsoft-client-id
MICROSOFT_CLIENT_SECRET=your-microsoft-client-secret
DATABASE_URL=sqlite:///canjia.db
```

5. **데이터베이스 초기화**
```bash
python
>>> from app import app, db
>>> with app.app_context():
>>>     db.create_all()
>>> exit()
```

6. **애플리케이션 실행**
```bash
python app.py
```

7. **브라우저에서 접속**
```
http://localhost:5000
```

## 사용 방법

### 회원 가입
1. 홈페이지에서 "시작하기" 또는 "가입" 버튼 클릭
2. 이메일, 이름, 비밀번호 입력
3. 이용약관 동의
4. 회원가입 완료

### 프로필 작성
1. 로그인 후 프로필 페이지 접속
2. 프로필 사진, 소개글, 관심 분야 설정
3. 저장

### 문서 작성
1. "새 문서 작성" 버튼 클릭
2. 제목, 분야, 내용 입력
3. 공개/비공개 설정
4. 작성 완료

### 분야 탐색
1. 분야 탐색 페이지 접속
2. 원하는 분야 선택
3. 해당 분야의 모든 문서 확인
4. 관심 있는 문서 읽기 및 댓글 작성

## 기술 스택

### 백엔드
- **Framework**: Flask (Python 웹 프레임워크)
- **Database**: SQLite + SQLAlchemy ORM
- **Authentication**: Microsoft OAuth 2.0
- **Session**: Flask-Session

### 프론트엔드
- **Markup**: HTML5
- **Styling**: CSS3 (Responsive Design)
- **Scripting**: Vanilla JavaScript (ES6+)

### 추가 라이브러리
- MSAL (Microsoft Authentication Library)
- python-dotenv (환경 변수 관리)
- Requests (HTTP 라이브러리)

## API 엔드포인트

### 인증
- `GET /auth/login` - 로그인 페이지
- `GET /auth/signup` - 회원가입 페이지
- `GET /auth/logout` - 로그아웃

### 페이지
- `GET /` - 홈페이지
- `GET /intro` - 소개 페이지
- `GET /fields` - 분야 탐색
- `GET /field/<field_name>` - 분야 상세

### 사용자
- `GET /auth/profile` - 프로필 페이지
- `GET /api/user/profile` - 프로필 API (조회)
- `POST /api/user/profile` - 프로필 API (수정)

### 문서
- `GET /documents` - 내 문서 목록
- `GET /document/<doc_id>` - 문서 상세 보기
- `GET /document/new` - 새 문서 작성 페이지
- `POST /document/new` - 새 문서 작성
- `GET /document/<doc_id>/edit` - 문서 수정 페이지
- `POST /document/<doc_id>/edit` - 문서 수정
- `POST /document/<doc_id>/delete` - 문서 삭제

## 7가지 목표

1. **경제 자립** - 배우고 학습하는 시대를 벗어나 실제 경제 활동 시작
2. **취미 생활** - 다양한 스포츠와 활동을 통해 삶의 질 향상
3. **기술 증진** - AGI와 ACTF 기술 개발을 통한 미래 준비
4. **회원 모집** - 같은 생각을 가진 사람들과 함께 성장
5. **주거 이전** - 제주도로 이전하여 새로운 삶의 환경 구축
6. **생명 연장** - 기술을 통해 생명 연장 목표 달성
7. **우주 유영** - 최종 목표로 미래 기술 실현

## 개발 환경

### 개발 도구
- IDE: VS Code
- Python Version: 3.8+
- Package Manager: pip
- Version Control: Git

### Google Colab
- 환경: Google Colab - Gemini
- AI 지원: Gemini를 활용한 개발 지원

## 환경 설정

### 로그인 및 인증
- **로그인 방식**: Microsoft Client ID & Secret 기반
- **2차 인증**: 선택적 활성화
- **세션 관리**: Flask-Session 활용

### 웹페이지 구성
1. **로그인 및 소개 라인**
   - 소개 페이지
   - 프로필 작성
   - 회원 가입
   - 로그인
   - 2차 인증

2. **분야 구성 바**
   - AGI / ACTF / 수영 / 스키 / 암벽등반 / 카페취업 / 기술연마

3. **등록된 사람들의 분야별 문서 등록 창**
   - 분야 선택시 자동으로 이동
   - 분야별 문서 목록 표시

4. **문서 작성 페이지**
   - Google Docs 스타일 편집기
   - 마크다운 형식 지원
   - 공유 기능

## 배포

### 운영 환경 배포
```bash
# 운영 설정 사용
export FLASK_ENV=production
python app.py
```

### Heroku 배포 (선택사항)
```bash
heroku login
heroku create your-app-name
git push heroku main
```

## 주의사항

1. **보안**
   - `.env` 파일을 `.gitignore`에 추가
   - 프로덕션 환경에서는 `SECRET_KEY` 변경
   - HTTPS 사용 필수 (배포 시)

2. **데이터베이스**
   - 정기적인 백업 수행
   - 대규모 트래픽 시 PostgreSQL 고려

3. **Microsoft OAuth**
   - Client ID와 Secret을 안전하게 관리
   - Redirect URI 정확히 설정

## 문제 해결

### 포트 이미 사용 중인 경우
```bash
# 다른 포트 사용
python app.py --port 5001
```

### 데이터베이스 오류
```bash
# 데이터베이스 초기화
rm canjia.db
python app.py
```

### 모듈 import 오류
```bash
# 의존성 재설치
pip install --upgrade -r requirements.txt
```

## 기여 가이드

이 프로젝트에 기여하고 싶으시면:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 연락처

- **작성자**: 정구영
- **작성일**: 2026년 05월 15일
- **프로젝트명**: CANJIA (Community for Association & Network in Jeju Industry Association)
- **지역**: 제주도

## 감사의 말

CANJIA 프로젝트에 관심을 가져주신 모든 분께 감사드립니다.

---

**CANJIA - 제주 산업 발전 및 네트워크 공동체**

제주도에서 시작되는 새로운 미래, 함께 만들어가겠습니다.

🚀 AGI & Android Cyborg Transformers를 통한 미래 기술 실현
🌍 경제 자립과 기술 증진을 위한 커뮤니티
⭐ 생명 연장과 우주 유영이라는 최종 목표
