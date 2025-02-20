from fastapi import APIRouter, UploadFile, File
from typing import Dict
from app.services.speech_service import SpeechService

router = APIRouter()
speech_service = SpeechService()

@router.post("/transcribe")
async def transcribe_audio(audio: UploadFile = File(...)) -> Dict[str, str]:
    audio_content = await audio.read()
    text = await speech_service.transcribe_audio(audio_content)
    return {"text": text}

@router.post("/synthesize")
async def synthesize_text(text: str) -> bytes:
    return await speech_service.synthesize_speech(text) 