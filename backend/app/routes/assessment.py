from fastapi import APIRouter, HTTPException
from typing import Dict
from app.services.assessment_service import AssessmentService
from app.models.api_models import (
    AssessmentStartRequest,
    AssessmentResponse,
    ProcessResponseRequest
)

router = APIRouter()
assessment_service = AssessmentService()

@router.post("/start")
async def start_assessment(request: AssessmentStartRequest) -> AssessmentResponse:
    try:
        return await assessment_service.start_conversation(request.age_months)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/process")
async def process_response(request: ProcessResponseRequest) -> AssessmentResponse:
    try:
        return await assessment_service.process_response(request.message, request.context)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 