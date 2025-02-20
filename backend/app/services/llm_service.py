from llama_cpp import Llama
from typing import Dict, List, Optional
import os
from app.utils.memory_manager import MemoryManager
import asyncio

class LLMService:
    def __init__(self):
        model_path = os.getenv("LLM_MODEL_PATH", "models/mistral-7b-instruct-v0.2.Q3_K_S.gguf")
        
        self.llm = Llama(
            model_path=model_path,
            n_ctx=2048,  # Reduced context window
            n_threads=8,  # Optimized for M-series
            n_gpu_layers=-1,  # Use Metal for acceleration
            n_batch=512,  # Batch size for inference
            use_mlock=True,  # Keep model in memory
            use_mmap=True  # Use memory mapping
        )
        
        # System prompt for child development assessment
        self.system_prompt = """You are an AI assistant specialized in child development assessment.
        Your role is to engage parents in natural conversation while carefully observing developmental indicators.
        Focus on being supportive and non-judgmental while gathering relevant information."""
    
    async def generate_response(
        self,
        message: str,
        context: Dict,
        temperature: float = 0.7
    ) -> str:
        if not MemoryManager.is_memory_available(threshold_mb=1000):
            MemoryManager.cleanup()
            await asyncio.sleep(0.1)  # Give system time to reclaim memory
        
        conversation = self._format_conversation(message, context)
        
        response = self.llm.create_chat_completion(
            messages=conversation,
            temperature=temperature,
            max_tokens=256  # Reduced for memory efficiency
        )
        
        MemoryManager.cleanup()
        return response['choices'][0]['message']['content']
    
    def _format_conversation(self, message: str, context: Dict) -> List[Dict]:
        conversation = [
            {"role": "system", "content": self.system_prompt}
        ]
        
        # Add conversation history if available
        if "history" in context:
            for msg in context["history"]:
                conversation.append(msg)
        
        # Add current message
        conversation.append({"role": "user", "content": message})
        
        return conversation 