# CANJIA 웹사이트 빠른 시작 가이드

## 🚀 5분 안에 시작하기

### 1단계: 저장소 설정

```bash
cd CANJIAWEB
```

### 2단계: 가상 환경 생성

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3단계: 의존성 설치

```bash
pip install -r requirements.txt
```

### 4단계: 환경 설정

```bash
# .env 파일 생성
cp .env.example .env
```

`.env` 파일을 텍스트 편집기로 열어 다음을 설정하세요:

```
FLASK_ENV=development
MICROSOFT_CLIENT_ID=your-client-id
MICROSOFT_CLIENT_SECRET=your-client-secret
```

### 5단계: 초기 설정

```bash
python setup.py
```

### 6단계: 애플리케이션 실행

```bash
python app.py
```

### 7단계: 브라우저에서 접속

```
http://localhost:5000
```

---

## 📋 기본 기능

### 회원가입
- 이메일, 이름, 비밀번호 입력
- 프로필 작성
- 관심 분야 설정

### 문서 작성
- "새 문서 작성" 클릭
- 제목, 분야, 내용 입력
- 마크다운 형식 지원

### 분야 탐색
- 7가지 분야 중 선택
- 분야별 모든 문서 보기
- 댓글 및 피드백 작성

### 프로필 관리
- 프로필 사진 업로드
- 소개글 작성
- 관심 분야 설정

---

## 🔧 문제 해결

### "포트 5000이 이미 사용 중입니다"

```bash
# 다른 포트 사용
# Windows
set FLASK_ENV=development & set PORT=5001 & python app.py

# Linux/macOS
FLASK_ENV=development PORT=5001 python app.py
```

### "ModuleNotFoundError: No module named 'flask'"

```bash
# 의존성 재설치
pip install --upgrade -r requirements.txt
```

### "Database is locked"

```bash
# 데이터베이스 초기화
rm canjia.db  # Linux/macOS
del canjia.db  # Windows
python app.py
```

---

## 📚 다음 단계

1. **프로필 작성**: 홈페이지에서 프로필을 완성하세요
2. **분야 탐색**: 관심 있는 분야를 선택하세요
3. **문서 작성**: 첫 번째 문서를 작성해보세요
4. **커뮤니티 참여**: 다른 사용자의 문서에 댓글을 남기세요

---

## 🎯 CANJIA의 7가지 분야

1. 🤖 **AGI** - 범용 인공 지능
2. 🔧 **ACTF** - 안드로이드 사이보그 트랜스포머
3. 🏊 **수영** - 무중력 환경 체험
4. 🪂 **스키** - 중력 활용 스포츠
5. 🧗 **암벽등반** - 신체 능력 단련
6. ☕ **카페취업** - 제주도 경제 활동
7. ⚙️ **기술연마** - 실무 기술 습득

---

## 📞 지원

문제가 발생하거나 질문이 있으시면:

1. README.md의 문제 해결 섹션 확인
2. GitHub Issues에 문제 보고
3. 커뮤니티에서 도움 요청

---

**CANJIA와 함께 성장하세요! 🚀**
