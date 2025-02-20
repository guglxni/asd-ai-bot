import os
import requests
from huggingface_hub import hf_hub_download

def download_model():
    """Download the GGUF model from Hugging Face"""
    model_path = "models/mistral-7b-instruct-v0.2.Q3_K_S.gguf"
    
    if not os.path.exists("models"):
        os.makedirs("models")
    
    if not os.path.exists(model_path):
        print("Downloading model...")
        hf_hub_download(
            repo_id="TheBloke/Mistral-7B-Instruct-v0.2-GGUF",
            filename="mistral-7b-instruct-v0.2.Q3_K_S.gguf",
            local_dir="models"
        )
        print("Model downloaded successfully!")
    else:
        print("Model already exists!")

if __name__ == "__main__":
    download_model() 