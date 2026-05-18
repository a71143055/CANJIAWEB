# 🚀 GitHub 업로드 방법

## 📋 사전 준비

### 1. GitHub 계정 준비
- GitHub 계정이 없으면 https://github.com/signup 에서 생성

### 2. 새 저장소 생성
1. https://github.com/new 접속
2. Repository name: `CANJIAWEB`
3. Description: `제주 산업 발전 및 네트워크 공동체 - CANJIA Web Platform`
4. Public 선택
5. "Create repository" 클릭

### 3. Personal Access Token 생성 (선택사항이지만 권장)
1. https://github.com/settings/tokens 접속
2. "Generate new token" 또는 "Generate new token (classic)" 클릭
3. Token name: `CANJIAWEB`
4. Expiration: 90 days 또는 No expiration
5. Scopes: `repo` 선택
6. "Generate token" 클릭
7. 토큰 복사 (다시 볼 수 없음!)

---

## 🔧 업로드 방법

### ✨ 방법 1: 자동 스크립트 (권장) - PowerShell

```powershell
# PowerShell 실행정책 변경 (처음 한 번만)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 스크립트 실행
cd "c:\Users\USER\OneDrive\바탕 화면\CANJIAWEB"
.\github-push.ps1 -Username YOUR_GITHUB_USERNAME
```

**YOUR_GITHUB_USERNAME을 실제 GitHub 사용자명으로 바꿔주세요!**

예시:
```powershell
.\github-push.ps1 -Username johndoe
```

---

### ✨ 방법 2: 자동 스크립트 - Batch (Windows)

```batch
cd "c:\Users\USER\OneDrive\바탕 화면\CANJIAWEB"
github-push.bat YOUR_GITHUB_USERNAME
```

**YOUR_GITHUB_USERNAME을 실제 GitHub 사용자명으로 바꿔주세요!**

예시:
```batch
github-push.bat johndoe
```

---

### ✨ 방법 3: 수동 명령어 - PowerShell

```powershell
cd "c:\Users\USER\OneDrive\바탕 화면\CANJIAWEB"

# 1. 원격 저장소 설정
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/CANJIAWEB.git

# 2. 상태 확인
git status

# 3. GitHub에 푸시
git push -u origin main
```

---

### ✨ 방법 4: 수동 명령어 - CMD

```cmd
cd c:\Users\USER\OneDrive\바탕 화면\CANJIAWEB

REM 1. 원격 저장소 설정
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/CANJIAWEB.git

REM 2. 상태 확인
git status

REM 3. GitHub에 푸시
git push -u origin main
```

---

## 🔐 자격증명 입력

### HTTPS 사용 시
- **Username**: GitHub 사용자명
- **Password**: Personal Access Token (위에서 생성한 토큰)

### 처음 푸시 시 자격증명 요청 창이 나타나면:
1. GitHub 사용자명 입력
2. Personal Access Token 입력 (비밀번호 칸에)

---

## ✅ 성공 확인

### 1. 콘솔에서 확인
```
To https://github.com/YOUR_USERNAME/CANJIAWEB.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

### 2. GitHub 웹사이트에서 확인
- https://github.com/YOUR_USERNAME/CANJIAWEB 접속
- 모든 파일이 업로드되었는지 확인

---

## 📊 업로드될 파일

```
CANJIAWEB/
├── 📄 Python 파일 (11개)
├── 📄 HTML 템플릿 (13개)
├── 📄 CSS 스타일
├── 📄 JavaScript
├── 📄 README 및 가이드 (8개)
├── 📄 설정 파일
└── 📁 폴더 구조 (auth, static, templates)
```

총 파일: **50+개**
커밋: **5개**

---

## 🆘 문제 해결

### ❌ "Authentication failed"

**해결책:**
```powershell
# Windows Credential Manager에서 자격증명 제거
$CmdCert = 'git:https://github.com'
cmdkey /delete $CmdCert

# 다시 푸시 (새로 입력)
git push -u origin main
```

### ❌ "remote origin already exists"

**해결책:**
```powershell
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/CANJIAWEB.git
```

### ❌ "Permission denied (publickey)"

**SSH 문제인 경우:**
```powershell
# SSH 연결 확인
ssh -T git@github.com

# HTTPS로 변경
git remote set-url origin https://github.com/YOUR_USERNAME/CANJIAWEB.git
```

### ❌ "fatal: not a git repository"

**해결책:**
```powershell
cd "c:\Users\USER\OneDrive\바탕 화면\CANJIAWEB"
git status  # Git 저장소 확인
```

---

## 🔄 업데이트 푸시 (향후)

추후 변경사항을 GitHub에 업데이트하려면:

```powershell
cd "c:\Users\USER\OneDrive\바탕 화면\CANJIAWEB"

# 1. 변경사항 확인
git status

# 2. 모든 변경사항 추가
git add .

# 3. 커밋 메시지와 함께 커밋
git commit -m "새로운 기능 추가"

# 4. GitHub에 푸시
git push origin main
```

---

## 📚 참고 정보

### 현재 저장소 상태
| 항목 | 상태 |
|------|------|
| 로컬 저장소 | ✅ 준비됨 |
| 커밋 개수 | 5개 |
| 현재 브랜치 | main |
| 워킹 트리 | Clean (깨끗함) |

### 파일 통계
```
Python 코드: 11개 파일
HTML 템플릿: 13개 파일
CSS: 1개 파일
JavaScript: 1개 파일
설정/가이드: 8개 파일
```

---

## 🎯 다음 단계

1. ✅ GitHub 저장소 생성
2. ✅ Personal Access Token 생성 (선택)
3. ✅ 스크립트 실행 또는 수동 명령어 입력
4. ✅ GitHub 웹사이트에서 확인
5. ✅ README.md 수정 (선택)

---

## 💡 팁

### GitHub 저장소 설명 추가
```markdown
# CANJIA - 제주 산업 발전 및 네트워크 공동체

제주도 기반의 산업 발전 및 네트워크 공동체 웹 플랫폼

## 주요 기능
- 회원 관리 (이메일/비밀번호 + 2FA)
- 문서 작성 및 공유
- 분야별 커뮤니티
- 반응형 디자인

## 기술 스택
- Flask
- SQLAlchemy
- SQLite
- HTML5, CSS3, JavaScript

## 목표
경제 자립 | 취미 생활 | 기술 증진 | 회원 모집 | 주거 이전 | 생명 연장 | 우주 유영
```

---

## 🎉 축하합니다!

**CANJIA 웹사이트가 GitHub에 성공적으로 업로드됩니다!** 🚀

---

**문제가 있으시면 이 가이드의 문제 해결 섹션을 참고하세요.**
