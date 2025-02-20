from google.cloud import speech_v1
from google.cloud import texttospeech
import io

class SpeechService:
    def __init__(self):
        self.stt_client = speech_v1.SpeechClient()
        self.tts_client = texttospeech.TextToSpeechClient()
    
    async def transcribe_audio(self, audio_content: bytes) -> str:
        """
        Transcribe audio using Google Speech-to-Text
        """
        audio = speech_v1.RecognitionAudio(content=audio_content)
        config = speech_v1.RecognitionConfig(
            encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code="en-US",
            sample_rate_hertz=16000,
        )
        
        response = self.stt_client.recognize(config=config, audio=audio)
        return response.results[0].alternatives[0].transcript if response.results else ""
    
    async def synthesize_speech(self, text: str) -> bytes:
        """
        Convert text to speech using Google Text-to-Speech
        """
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Standard-C",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        
        response = self.tts_client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        return response.audio_content 