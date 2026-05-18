#!/usr/bin/env python
"""
CANJIA 웹사이트 초기 설정 스크립트
이 스크립트는 애플리케이션 실행에 필요한 초기 설정을 수행합니다.
"""

import os
import sys
from pathlib import Path

def setup_environment():
    """환경 설정"""
    print("=" * 60)
    print("CANJIA 웹사이트 초기 설정")
    print("=" * 60)
    print()
    
    # .env 파일 확인
    env_file = Path('.env')
    if not env_file.exists():
        print("⚠️  .env 파일이 없습니다.")
        print("  .env.example을 복사하여 .env 파일을 생성하세요.")
        print("  명령어: cp .env.example .env (Linux/macOS)")
        print("         copy .env.example .env (Windows)")
        response = input("\n계속하시겠습니까? (y/n): ")
        if response.lower() != 'y':
            return False
    else:
        print("✅ .env 파일 발견")
    
    return True

def check_python_version():
    """Python 버전 확인"""
    print("\n📦 Python 버전 확인 중...")
    version = sys.version_info
    print(f"  Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 이상이 필요합니다.")
        return False
    
    print("✅ Python 버전 확인 완료")
    return True

def check_dependencies():
    """의존성 확인"""
    print("\n📚 의존성 확인 중...")
    
    required_packages = [
        'flask',
        'flask_sqlalchemy',
        'flask_session',
        'sqlalchemy',
        'msal',
        'requests'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('_', '-').replace('-', '_'))
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package} (설치 필요)")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  {len(missing_packages)}개의 패키지가 설치되지 않았습니다.")
        response = input("pip install을 실행하시겠습니까? (y/n): ")
        if response.lower() == 'y':
            os.system('pip install -r requirements.txt')
        else:
            print("❌ 의존성이 설치되지 않았습니다. 다시 실행해주세요.")
            return False
    
    print("✅ 의존성 확인 완료")
    return True

def initialize_database():
    """데이터베이스 초기화"""
    print("\n🗄️  데이터베이스 초기화 중...")
    
    try:
        from app import app, db
        
        with app.app_context():
            # 기존 데이터베이스 확인
            db_file = Path('canjia.db')
            if db_file.exists():
                print("  데이터베이스가 이미 존재합니다.")
                response = input("  기존 데이터베이스를 초기화하시겠습니까? (y/n): ")
                if response.lower() == 'y':
                    db_file.unlink()
                    print("  ✅ 기존 데이터베이스 삭제")
                else:
                    print("  ✅ 기존 데이터베이스 유지")
                    return True
            
            # 데이터베이스 테이블 생성
            db.create_all()
            print("  ✅ 데이터베이스 테이블 생성 완료")
            
        return True
    except Exception as e:
        print(f"  ❌ 데이터베이스 초기화 실패: {e}")
        return False

def create_sample_data():
    """샘플 데이터 생성"""
    print("\n📝 샘플 데이터 생성 중...")
    
    response = input("샘플 데이터를 생성하시겠습니까? (y/n): ")
    if response.lower() != 'y':
        print("  ⏭️  샘플 데이터 생성 건너뛰기")
        return True
    
    try:
        from app import app, db, User, Document
        
        with app.app_context():
            # 샘플 사용자
            sample_user = User(
                email='demo@canjia.kr',
                name='데모 사용자',
                bio='CANJIA 커뮤니티의 데모 사용자입니다.',
                fields='AGI, 수영',
                is_verified=True
            )
            db.session.add(sample_user)
            db.session.commit()
            
            # 샘플 문서
            sample_docs = [
                {
                    'title': 'AGI 개발 입문 가이드',
                    'content': '범용 인공 지능(AGI) 개발에 대한 기초적인 가이드입니다.\n\n## 1. AGI란?\nAGI는 사람의 수준에 맞는 인공 지능입니다.\n\n## 2. 필요 기술\n- 머신러닝\n- 딥러닝\n- 자연어 처리',
                    'field': 'AGI',
                    'user_id': sample_user.id
                },
                {
                    'title': '수영을 통한 우주 적응 훈련',
                    'content': '수영은 무중력 환경을 간접 체험할 수 있는 훌륭한 방법입니다.\n\n## 수영의 효과\n1. 신체 유연성 증진\n2. 호흡 능력 개발\n3. 무중력 환경 적응',
                    'field': '수영',
                    'user_id': sample_user.id
                }
            ]
            
            for doc_data in sample_docs:
                doc = Document(**doc_data)
                db.session.add(doc)
            
            db.session.commit()
            print("  ✅ 샘플 데이터 생성 완료")
            print(f"    - 사용자: {sample_user.name} (demo@canjia.kr)")
            print(f"    - 문서: 2개")
            
        return True
    except Exception as e:
        print(f"  ❌ 샘플 데이터 생성 실패: {e}")
        return False

def print_setup_summary():
    """설정 완료 요약"""
    print("\n" + "=" * 60)
    print("✅ CANJIA 웹사이트 초기 설정 완료!")
    print("=" * 60)
    print()
    print("다음 단계:")
    print("1. .env 파일에서 설정값을 확인하세요")
    print("   - MICROSOFT_CLIENT_ID")
    print("   - MICROSOFT_CLIENT_SECRET")
    print()
    print("2. 애플리케이션을 실행하세요")
    print("   명령어: python app.py")
    print()
    print("3. 브라우저에서 접속하세요")
    print("   URL: http://localhost:5000")
    print()
    print("=" * 60)

def main():
    """메인 설정 함수"""
    try:
        # 1. 환경 확인
        if not setup_environment():
            print("❌ 설정 취소됨")
            return False
        
        # 2. Python 버전 확인
        if not check_python_version():
            return False
        
        # 3. 의존성 확인
        if not check_dependencies():
            return False
        
        # 4. 데이터베이스 초기화
        if not initialize_database():
            return False
        
        # 5. 샘플 데이터 생성
        if not create_sample_data():
            return False
        
        # 6. 설정 완료 요약
        print_setup_summary()
        return True
        
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
