from .assessment import router as assessment_router
from .speech import router as speech_router
from .auth import router as auth_router

__all__ = ['assessment_router', 'speech_router', 'auth_router'] 