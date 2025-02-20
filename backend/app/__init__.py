from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.middleware.error_handler import error_handler

app = FastAPI(title="Autism Assessment Bot")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add error handling middleware
app.middleware("http")(error_handler)

# Import and include routers
from app.routes import assessment_router, speech_router, auth_router

app.include_router(assessment_router, prefix="/api/assessment", tags=["assessment"])
app.include_router(speech_router, prefix="/api/speech", tags=["speech"])
app.include_router(auth_router, prefix="/api/auth", tags=["auth"]) 