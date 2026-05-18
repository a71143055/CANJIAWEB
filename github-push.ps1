#!/usr/bin/env pwsh
# CANJIA 웹사이트 GitHub 푸시 스크립트 (PowerShell)
# 사용법: .\github-push.ps1 -Username YOUR_USERNAME

param(
    [Parameter(Mandatory=$true, HelpMessage="GitHub 사용자명")]
    [string]$Username
)

# 색상 정의
$Success = "Green"
$Error = "Red"
$Info = "Cyan"
$Warning = "Yellow"

function Write-Title {
    param([string]$Text)
    Write-Host "`n" -ForegroundColor $Info
    Write-Host "=" * 50 -ForegroundColor $Info
    Write-Host $Text -ForegroundColor $Info
    Write-Host "=" * 50 -ForegroundColor $Info
    Write-Host "`n" -ForegroundColor $Info
}

function Write-Status {
    param(
        [string]$Step,
        [string]$Text,
        [string]$Status = "진행 중"
    )
    Write-Host "[$Step] $Text ... $Status" -ForegroundColor $Info
}

function Write-Success {
    param([string]$Text)
    Write-Host "✅ $Text" -ForegroundColor $Success
}

function Write-Error {
    param([string]$Text)
    Write-Host "❌ $Text" -ForegroundColor $Error
}

# 메인 로직
try {
    Write-Title "CANJIA GitHub 푸시 스크립트"
    
    $RepoUrl = "https://github.com/$Username/CANJIAWEB.git"
    $ProjectPath = "c:\Users\USER\OneDrive\바탕 화면\CANJIAWEB"
    
    Write-Host "사용자명: $Username" -ForegroundColor $Info
    Write-Host "저장소 URL: $RepoUrl" -ForegroundColor $Info
    Write-Host "`n" -ForegroundColor $Info
    
    # 1. 폴더 이동
    Write-Status "1/5" "프로젝트 폴더로 이동" "진행 중"
    if (-not (Test-Path $ProjectPath)) {
        Write-Error "폴더를 찾을 수 없습니다: $ProjectPath"
        exit 1
    }
    Set-Location $ProjectPath
    Write-Success "폴더 이동 완료"
    
    # 2. Git 저장소 확인
    Write-Status "2/5" "Git 저장소 확인" "진행 중"
    if (-not (Test-Path .git)) {
        Write-Error "Git 저장소가 아닙니다"
        exit 1
    }
    & git status | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Git 명령 실패"
        exit 1
    }
    Write-Success "Git 저장소 확인 완료"
    
    # 3. 원격 저장소 설정
    Write-Status "3/5" "원격 저장소 설정" "진행 중"
    & git remote remove origin 2>$null
    & git remote add origin $RepoUrl
    if ($LASTEXITCODE -ne 0) {
        Write-Error "원격 저장소 설정 실패"
        exit 1
    }
    Write-Success "원격 저장소 설정 완료"
    
    # 4. 현재 상태 확인
    Write-Status "4/5" "변경 사항 확인" "진행 중"
    & git status
    Write-Success "상태 확인 완료"
    
    # 5. GitHub에 푸시
    Write-Status "5/5" "GitHub에 푸시" "진행 중"
    Write-Host "`nGitHub 자격증명을 입력하세요." -ForegroundColor $Warning
    Write-Host "HTTPS를 사용하는 경우 Personal Access Token을 비밀번호로 사용하세요.`n" -ForegroundColor $Warning
    
    & git push -u origin main
    
    if ($LASTEXITCODE -ne 0) {
        Write-Error "푸시 실패"
        Write-Host "`n문제 해결:`n"
        Write-Host "1. GitHub 저장소가 생성되었는지 확인" -ForegroundColor $Warning
        Write-Host "2. Personal Access Token(PAT)이 올바른지 확인" -ForegroundColor $Warning
        Write-Host "3. 네트워크 연결 확인" -ForegroundColor $Warning
        exit 1
    }
    
    Write-Title "✅ GitHub 푸시 완료!"
    
    Write-Host "저장소 정보:" -ForegroundColor $Info
    Write-Host "  URL: https://github.com/$Username/CANJIAWEB" -ForegroundColor $Info
    Write-Host "  브랜치: main" -ForegroundColor $Info
    Write-Host "`n" -ForegroundColor $Info
    
    Write-Host "다음 명령어로 상태를 확인할 수 있습니다:" -ForegroundColor $Info
    Write-Host "  git log --oneline" -ForegroundColor $Info
    Write-Host "  git remote -v" -ForegroundColor $Info
    Write-Host "`n" -ForegroundColor $Info
    
    Write-Success "모든 작업이 완료되었습니다!"
    
} catch {
    Write-Error "예기치 않은 오류: $_"
    exit 1
}
