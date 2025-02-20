# Child Development Assistant 🧸

A conversational AI system for tracking child development (0-3 years), powered by local LLM technology. Combines natural language processing with developmental psychology to provide insights through friendly conversation.

![App Preview Coming Soon]()

## ✨ Key Features

- 💬 **Natural Language Interface**: Conversational assessment using Mistral 7B LLM
- 📊 **Real-time CDDC**: Dynamic Child Development Data Chart visualization
- 🎯 **Age-Specific Assessment**: Tailored developmental milestones tracking
- 🔒 **Privacy-First**: Local processing with hardware acceleration support
- 🤖 **Adaptive Responses**: Reinforcement learning for question optimization
- 🌟 **Comprehensive Tracking**: Seven key developmental domains

## 🚀 Quick Start

### For Users
Coming Soon! Web interface under development.

### For Developers

```bash
# Clone repository
git clone https://github.com/yourusername/child-development-assistant
cd child-development-assistant

# Backend Setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install backend dependencies with hardware acceleration
# For macOS (Apple Silicon):
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
# For NVIDIA GPU:
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
# For CPU only:
pip install llama-cpp-python

pip install -r requirements.txt

# Download LLM model
python scripts/download_model.py

# Frontend Setup
cd ../frontend
npm install

# Run Development Servers
# Terminal 1 (Backend):
cd backend && uvicorn app.main:app --reload --port 8000

# Terminal 2 (Frontend):
cd frontend && npm run dev
```

## 🎯 Development Areas & Assessment Methods

### Physical Development 🏃‍♀️
- **Gross Motor**: Large movement coordination
- **Fine Motor**: Hand-eye coordination, manipulation
- **Assessment**: Movement pattern analysis, milestone tracking

### Communication & Language 🗣️
- **Receptive**: Language comprehension
- **Expressive**: Speech and communication
- **Assessment**: Natural language processing, speech pattern analysis

### Cognitive & Daily Living 🧠
- **Problem Solving**: Learning and adaptation
- **Self-Care**: Daily living skills
- **Assessment**: Task completion analysis, behavioral patterns

### Social-Emotional 👥
- **Social Interaction**: Peer relationships
- **Emotional Expression**: Feeling recognition
- **Assessment**: Sentiment analysis, interaction patterns

## 🛠 Technical Stack

### Backend
- FastAPI for API endpoints
- Mistral 7B (Q3 quantized) for conversation
- Hardware acceleration support (Metal/CUDA/CPU)
- SQLAlchemy for data persistence
- Spacy for NLP processing

### Frontend
- React 18 with TypeScript
- Material-UI for components
- Chart.js for visualization
- Vite for development

### AI/ML Components
- Local LLM inference
- Reinforcement learning for question selection
- Developmental milestone mapping
- Sentiment analysis pipeline

## 💡 Implementation Details

### LLM Configuration
```python
# Hardware-specific optimizations
LLM_CONFIG = {
    "model_path": "models/mistral-7b-instruct-v0.2.Q3_K_S.gguf",
    "n_ctx": 2048,  # Adjust based on available memory
    "n_threads": 8,
    # Hardware acceleration settings:
    # Apple Silicon: n_gpu_layers=-1
    # NVIDIA GPU: n_gpu_layers=35
    # CPU only: n_gpu_layers=0
    "n_gpu_layers": -1,
    "n_batch": 512,  # Adjust based on GPU memory
    # Optional hardware-specific settings
    "use_mmap": True,
    "use_mlock": True
}
```

### API Endpoints
- `/api/assessment/start`: Initialize assessment session
- `/api/assessment/process`: Process conversation
- `/api/speech/*`: Speech-to-text and text-to-speech
- `/api/auth/*`: Authentication endpoints

## ❓ FAQ

**Q: System Requirements?**
A: 
Minimum Requirements:
- Any modern CPU (Intel/AMD/ARM)
- 8GB RAM
- 5GB storage
- Python 3.11+
- Node.js 18+

Recommended Hardware:
- Apple Silicon Mac (M1/M2/M3) OR
- NVIDIA GPU (8GB VRAM) OR
- Modern CPU (8+ cores)
- 16GB RAM

Performance Tiers:
1. **Best**: Apple Silicon Mac or NVIDIA RTX 3060+ GPU
2. **Good**: NVIDIA GTX 1660+ GPU
3. **Basic**: Modern multi-core CPU

**Q: Is this a diagnostic tool?**
A: No, this is a development tracking assistant. Consult healthcare professionals for diagnosis.

**Q: Data Privacy?**
A: All processing is local. No data leaves your device.

**Q: Performance on different hardware?**
A: The system adapts to available hardware:
- Apple Silicon: Fastest, most energy efficient
- NVIDIA GPU: Similar performance to Apple Silicon
- CPU only: Slower but fully functional

## 🆘 Support

- 📝 [Documentation](docs/)
- 🐛 [Issue Tracker](issues/)
- 💬 [Discussions](discussions/)

## 🌟 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

---

Made with ❤️ for families and developers alike 