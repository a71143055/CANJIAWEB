"""
CANJIA 웹사이트 설정 파일
제주 산업 발전 및 네트워크 공동체
"""

import os
from datetime import timedelta

class Config:
    """기본 설정"""
    # Flask 설정
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'canjia-secret-key-2026'
    DEBUG = False
    
    # 세션 설정
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # 데이터베이스 설정 (SQLite)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///canjia.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # CANJIA 설정
    CANJIA_FIELDS = [
        'AGI', 'ACTF', '수영', '스키', '암벽등반', '카페취업', '기술연마'
    ]
    
    CANJIA_GOALS = [
        '경제자립', '취미생활', '기술증진', '회원모집', '주거이전', '생명연장', '우주유영'
    ]
    
    # 이메일 설정 (선택사항)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = os.environ.get('MAIL_PORT', 587)
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class DevelopmentConfig(Config):
    """개발 환경 설정"""
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class ProductionConfig(Config):
    """운영 환경 설정"""
    DEBUG = False

class TestingConfig(Config):
    """테스트 환경 설정"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
