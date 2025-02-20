from pydantic import BaseModel
from typing import Optional, Dict, Any

class AssessmentStartRequest(BaseModel):
    age_months: int

class AssessmentResponse(BaseModel):
    message: str
    area: Optional[str] = None
    milestone: Optional[str] = None
    assessmentData: Optional[Dict[str, Any]] = None

class ProcessResponseRequest(BaseModel):
    message: str
    context: Dict[str, Any]

class SynthesizeRequest(BaseModel):
    text: str 