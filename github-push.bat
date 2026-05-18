@echo off
REM CANJIA 웹사이트 GitHub 푸시 스크립트 (Windows)
REM 사용법: github-push.bat YOUR_USERNAME

setlocal enabledelayedexpansion

if "%1"=="" (
    echo.
    echo ========================================
    echo CANJIA GitHub 푸시 스크립트
    echo ========================================
    echo.
    echo 사용법: github-push.bat YOUR_GITHUB_USERNAME
    echo.
    echo 예시: github-push.bat johndoe
    echo.
    exit /b 1
)

set USERNAME=%1
set REPO_URL=https://github.com/%USERNAME%/CANJIAWEB.git

echo.
echo ========================================
echo GitHub 푸시 진행 중...
echo ========================================
echo.
echo Username: %USERNAME%
echo Repository: %REPO_URL%
echo.

REM 1. 폴더로 이동
cd /d "c:\Users\USER\OneDrive\바탕 화면\CANJIAWEB"

if errorlevel 1 (
    echo 오류: 폴더를 찾을 수 없습니다.
    exit /b 1
)

REM 2. Git 상태 확인
echo [1/5] Git 상태 확인 중...
git status
if errorlevel 1 (
    echo 오류: Git 저장소가 아닙니다.
    exit /b 1
)

REM 3. 원격 저장소 설정
echo.
echo [2/5] 원격 저장소 설정 중...
git remote remove origin
git remote add origin %REPO_URL%
if errorlevel 1 (
    echo 오류: 원격 저장소 설정 실패
    exit /b 1
)

REM 4. 현재 상태 확인
echo.
echo [3/5] 변경 사항 확인 중...
git status

REM 5. 푸시 실행
echo.
echo [4/5] GitHub에 푸시 중...
git push -u origin main
if errorlevel 1 (
    echo.
    echo 오류: 푸시 실패
    echo 다음을 확인하세요:
    echo 1. GitHub 저장소가 생성되었는지 확인
    echo 2. 자격증명(Personal Access Token)이 올바른지 확인
    echo 3. 네트워크 연결 확인
    exit /b 1
)

REM 6. 완료
echo.
echo [5/5] 완료!
echo.
echo ========================================
echo ✅ GitHub 푸시 완료!
echo ========================================
echo.
echo 저장소 URL: https://github.com/%USERNAME%/CANJIAWEB
echo.
echo 다음 명령어로 현재 상태를 확인할 수 있습니다:
echo git log --oneline
echo git remote -v
echo.
pause
