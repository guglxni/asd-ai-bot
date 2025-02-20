import psutil
import gc
import torch

class MemoryManager:
    @staticmethod
    def check_memory():
        memory = psutil.Process().memory_info()
        return {
            "rss": memory.rss / 1024 / 1024,  # MB
            "vms": memory.vms / 1024 / 1024   # MB
        }
    
    @staticmethod
    def cleanup():
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    @staticmethod
    def is_memory_available(threshold_mb: int = 1000) -> bool:
        memory = psutil.virtual_memory()
        return memory.available / 1024 / 1024 > threshold_mb 