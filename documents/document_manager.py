"""
CANJIA 문서 관리 모듈
문서 작성, 수정, 삭제 기능
"""

from datetime import datetime
from app import db, Document

class DocumentManager:
    """문서 관리 클래스"""
    
    @staticmethod
    def create_document(user_id, title, content, field, is_public=True):
        """새 문서 생성"""
        doc = Document(
            user_id=user_id,
            title=title,
            content=content,
            field=field,
            is_public=is_public,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(doc)
        db.session.commit()
        return doc
    
    @staticmethod
    def update_document(doc_id, title=None, content=None, field=None, is_public=None):
        """문서 수정"""
        doc = Document.query.get(doc_id)
        if doc:
            if title:
                doc.title = title
            if content:
                doc.content = content
            if field:
                doc.field = field
            if is_public is not None:
                doc.is_public = is_public
            doc.updated_at = datetime.utcnow()
            db.session.commit()
        return doc
    
    @staticmethod
    def delete_document(doc_id):
        """문서 삭제"""
        doc = Document.query.get(doc_id)
        if doc:
            db.session.delete(doc)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_user_documents(user_id):
        """사용자의 모든 문서 조회"""
        return Document.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_public_documents(field=None):
        """공개 문서 조회"""
        query = Document.query.filter_by(is_public=True)
        if field:
            query = query.filter_by(field=field)
        return query.all()
    
    @staticmethod
    def search_documents(keyword, field=None):
        """문서 검색"""
        query = Document.query.filter(
            (Document.title.ilike(f'%{keyword}%')) |
            (Document.content.ilike(f'%{keyword}%')),
            Document.is_public == True
        )
        if field:
            query = query.filter_by(field=field)
        return query.all()
    
    @staticmethod
    def get_trending_documents(limit=10):
        """인기 문서 조회 (댓글 많은 순)"""
        from sqlalchemy import func
        
        return db.session.query(Document).filter(
            Document.is_public == True
        ).outerjoin(
            db.session.query(Document.id, func.count().label('comment_count')).group_by(Document.id)
        ).order_by(
            'comment_count'
        ).limit(limit).all()
    
    @staticmethod
    def get_recent_documents(field=None, limit=10):
        """최근 문서 조회"""
        query = Document.query.filter_by(is_public=True).order_by(
            Document.created_at.desc()
        )
        if field:
            query = query.filter_by(field=field)
        return query.limit(limit).all()

class MarkdownConverter:
    """마크다운 변환 클래스"""
    
    @staticmethod
    def to_html(markdown_text):
        """마크다운을 HTML로 변환"""
        import markdown
        return markdown.markdown(markdown_text)
    
    @staticmethod
    def escape_html(text):
        """HTML 특수 문자 이스케이프"""
        import html
        return html.escape(text)

class DocumentValidator:
    """문서 검증 클래스"""
    
    @staticmethod
    def validate_title(title):
        """제목 검증"""
        if not title or len(title.strip()) == 0:
            return False, "제목은 필수입니다."
        if len(title) > 200:
            return False, "제목은 200자 이내여야 합니다."
        return True, ""
    
    @staticmethod
    def validate_content(content):
        """내용 검증"""
        if not content or len(content.strip()) == 0:
            return False, "내용은 필수입니다."
        if len(content) > 50000:
            return False, "내용은 50000자 이내여야 합니다."
        return True, ""
    
    @staticmethod
    def validate_field(field, valid_fields):
        """분야 검증"""
        if field not in valid_fields:
            return False, "유효하지 않은 분야입니다."
        return True, ""
    
    @staticmethod
    def validate_document(title, content, field, valid_fields):
        """전체 문서 검증"""
        valid, msg = DocumentValidator.validate_title(title)
        if not valid:
            return False, msg
        
        valid, msg = DocumentValidator.validate_content(content)
        if not valid:
            return False, msg
        
        valid, msg = DocumentValidator.validate_field(field, valid_fields)
        if not valid:
            return False, msg
        
        return True, "검증 성공"
