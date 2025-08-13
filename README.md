AgriSentinel Prototype (The Stakemates) - Quick Start

1) Python environment
   python -m venv venv
   source venv/bin/activate   (or venv\Scripts\activate on Windows)

2) Install
   cd backend
   pip install -r requirements.txt

3) Optional: enable OpenAI recommendations
   cp .env.example .env
   edit .env and set OPENAI_API_KEY=sk-...

4) Start server
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

5) Open browser
   http://localhost:8000
   Upload one of sample_images and click Analyze

Notes:
- This is a demo MVP using a simple color/greenness heuristic.
- For production: replace analyze.py heuristics with a trained segmentation/detection model (YOLOv8 / U-Net) or use multispectral NDVI images.
