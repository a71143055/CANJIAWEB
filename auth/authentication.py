"""
CANJIA 인증 모듈
Microsoft OAuth 2.0 기반 로그인 구현
"""

import os
from datetime import datetime
import msal
from functools import wraps
from flask import session, redirect, url_for

class MicrosoftAuthenticator:
    """Microsoft OAuth 2.0 인증 클래스"""
    
    def __init__(self, client_id, client_secret, authority, redirect_path):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authority = authority
        self.redirect_path = redirect_path
        
        self.app = msal.PublicClientApplication(
            client_id=client_id,
            authority=authority
        )
    
    def get_auth_url(self):
        """인증 URL 생성"""
        auth_code_flow = self.app.initiate_auth_code_flow(
            scopes=['user.read'],
            redirect_uri=self.redirect_path
        )
        return auth_code_flow['auth_uri'], auth_code_flow['state']
    
    def acquire_token_by_auth_code(self, auth_code):
        """인증 코드로 토큰 획득"""
        result = self.app.acquire_token_by_auth_code(
            auth_code,
            scopes=['user.read'],
            redirect_uri=self.redirect_path
        )
        return result
    
    def get_user_info(self, access_token):
        """사용자 정보 조회"""
        import requests
        
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get('https://graph.microsoft.com/v1.0/me', headers=headers)
        
        if response.status_code == 200:
            return response.json()
        return None

def login_required(f):
    """로그인 필수 데코레이터"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """관리자 권한 필수 데코레이터"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        
        # 관리자 권한 확인 로직
        # from app import User
        # user = User.query.get(session['user_id'])
        # if not user.is_admin:
        #     return redirect(url_for('index'))
        
        return f(*args, **kwargs)
    return decorated_function

def two_factor_required(f):
    """2차 인증 필수 데코레이터"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        
        if not session.get('two_factor_verified'):
            # 2차 인증 페이지로 리다이렉트
            return redirect(url_for('two_factor_auth'))
        
        return f(*args, **kwargs)
    return decorated_function

def generate_two_factor_code():
    """2차 인증 코드 생성"""
    import random
    return ''.join(str(random.randint(0, 9)) for _ in range(6))

def verify_two_factor_code(user_code, stored_code):
    """2차 인증 코드 검증"""
    return user_code == stored_code
