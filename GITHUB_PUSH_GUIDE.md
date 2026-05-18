# GitHub 푸시 가이드

## 1단계: GitHub 저장소 생성

### GitHub에서 새 저장소 생성:
1. https://github.com/new 접속
2. Repository name: `CANJIAWEB`
3. Description: `제주 산업 발전 및 네트워크 공동체 - CANJIA Web Platform`
4. Public 선택
5. "Create repository" 클릭

---

## 2단계: 원격 저장소 연결 (선택사항)

현재 커밋 로그:
```
b5e11cb (HEAD -> main) CANJIAWEB
1c32269 CANJIAWEB
99be28b CANJIAWEB
53d638b CANJIAWEB
af4b1a7 CANJIAWEB
```

---

## 3단계: 원격 저장소 설정 및 푸시

### 옵션 A: HTTPS (권장)
```bash
cd "c:\Users\USER\OneDrive\바탕 화면\CANJIAWEB"

# 원격 저장소 추가
git remote set-url origin https://github.com/YOUR_USERNAME/CANJIAWEB.git

# 또는 기존 원격 저장소를 제거하고 새로 추가
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/CANJIAWEB.git

# 푸시
git push -u origin main
```

### 옵션 B: SSH (개선된 보안)
```bash
# SSH 키 생성 (처음 한 번만)
ssh-keygen -t ed25519 -C "your-email@example.com"

# GitHub에서 SSH 키 추가
# 1. https://github.com/settings/keys 접속
# 2. "New SSH key" 클릭
# 3. 공개 키 내용 붙여넣기

# 원격 저장소 추가
git remote set-url origin git@github.com:YOUR_USERNAME/CANJIAWEB.git

# 푸시
git push -u origin main
```

---

## 4단계: 자격증명 설정 (처음 푸시 시)

### Windows Credential Manager 사용
```bash
# Git Credential Manager가 자동으로 나타날 것입니다
# GitHub 사용자명과 Personal Access Token(PAT)을 입력
```

### Personal Access Token 생성
1. GitHub Settings → Developer settings → Personal access tokens
2. "Generate new token" 클릭
3. Scopes: `repo` (모든 저장소 접근)
4. Token 복사 후 안전한 곳에 저장

---

## 5단계: 현재 파일 상태 확인

### 모든 파일 추가 및 커밋 (이미 커밋됨)
```bash
git status  # 상태 확인
```

현재 상태: `working tree clean` (모든 파일이 커밋됨)

---

## 🚀 빠른 실행 (Template)

### GitHub 저장소 URL 준비 후:
```bash
cd "c:\Users\USER\OneDrive\바탕 화면\CANJIAWEB"

# 1. 원격 저장소 제거 (기존)
git remote remove origin

# 2. 새 원격 저장소 추가
git remote add origin https://github.com/YOUR_USERNAME/CANJIAWEB.git

# 3. 메인 브랜치로 푸시
git push -u origin main

# 또는 force push (주의)
git push -u origin main --force
```

---

## 📝 현재 상태

| 항목 | 상태 |
|------|------|
| **로컬 저장소** | ✅ 준비됨 |
| **커밋** | ✅ 5개 커밋 |
| **워킹 트리** | ✅ 깨끗함 (Clean) |
| **원격 저장소** | ❌ 설정 필요 |
| **메인 브랜치** | ✅ 준비됨 |

---

## ⚡ 한 줄 명령어

```bash
cd "c:\Users\USER\OneDrive\바탕 화면\CANJIAWEB" ; git remote set-url origin https://github.com/YOUR_USERNAME/CANJIAWEB.git ; git push -u origin main
```

---

## 🔐 보안 팁

1. **Personal Access Token 사용** (비밀번호 대신)
2. **SSH 키 사용** (최고의 보안)
3. **.gitignore 확인** (민감한 파일 미포함)
4. **.env 파일** GitHub에 올리지 않기

---

## ❓ 문제 해결

### "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/CANJIAWEB.git
```

### "Authentication failed"
```bash
# 자격증명 초기화
git config --global credential.helper wincred
git config --global --unset credential.helper
```

### "Permission denied"
```bash
# SSH 키 확인
ssh -T git@github.com
```

---

## 다음 단계

1. ✅ GitHub 저장소 생성
2. ✅ 원격 저장소 URL 준비
3. ✅ 로컬에서 원격 저장소 설정
4. ✅ 푸시 실행
5. ✅ GitHub에서 확인

---

**준비 완료! GitHub에 푸시하실 준비가 되셨습니다.** 🚀
