# 🏥 OPAL-AI — Intelligent Organ & Blood Donor Matching Platform

OPAL-AI is an AI-powered healthcare donor matching platform built using FastAPI, Next.js, Supabase, Gemini AI, and Machine Learning.

The platform helps hospitals and healthcare staff:
- manage blood and organ donors
- find compatible donors
- rank donor suitability using ML
- analyze donor/request activity
- interact with an AI healthcare assistant

---

# 🚀 Features

## 🔹 Donor Management
- Add blood donors
- Add organ donors
- Hospital registration
- Real-time donor database

## 🔹 Intelligent Matching Engine
- Blood compatibility matching
- Organ compatibility matching
- Urgency-aware ranking
- Distance-aware scoring
- Availability scoring
- ML-enhanced donor ranking

## 🔹 AI Assistant
- Gemini-powered healthcare chatbot
- Donor matching explanations
- Platform assistance
- Safe healthcare workflow guidance

## 🔹 Dashboard Analytics
- Blood donor distribution charts
- Organ donor distribution charts
- Urgency breakdown analytics
- Match request history

## 🔹 Machine Learning Integration
- Synthetic dataset generation
- RandomForest ML ranking model
- Hybrid rule-based + ML scoring
- Predictive donor suitability scoring

---

# 🧠 Tech Stack

## Frontend
- Next.js
- TypeScript
- Tailwind CSS
- Recharts

## Backend
- FastAPI
- Python
- Pydantic

## Database
- Supabase

## AI & ML
- Gemini AI
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

# 📁 Project Structure

```bash
OPAL-AI V2/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── ml/
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   └── lib/
│   │
│   └── package.json
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/opal-ai.git
cd opal-ai
```

---

# 🔧 Backend Setup

## Create virtual environment

```bash
python -m venv venv
```

## Activate environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install dependencies

```bash
cd backend
pip install -r requirements.txt
```

---

## Create `.env`

```env
SUPABASE_URL=
SUPABASE_SERVICE_KEY=
GEMINI_API_KEY=
```

---

## Run backend

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```txt
http://127.0.0.1:8000
```

---

# 💻 Frontend Setup

## Install packages

```bash
cd frontend
npm install
```

---

## Create `.env.local`

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

---

## Run frontend

```bash
npm run dev
```

Frontend runs on:

```txt
http://localhost:3000
```

---

# 🤖 ML Pipeline

## Generate training dataset

```bash
python app/ml/scripts/generate_training_data.py
```

## Train ML model

```bash
python app/ml/scripts/train_ranking_model.py
```

---

# 📊 Current Capabilities

- Real-time donor management
- AI-assisted healthcare chatbot
- ML-enhanced donor ranking
- Analytics dashboard
- Match request tracking
- Geo-aware matching
- Hybrid scoring system

---

# 🔒 Future Improvements

- JWT authentication
- Role-based access control
- Docker deployment
- CI/CD pipelines
- Real medical dataset integration
- Advanced ML models
- Cloud deployment

---

# 📸 Screenshots

(Add screenshots here later)

---

# 👨‍💻 Author

Bilal Mohammad Afzal

- GitHub: https://github.com/
- LinkedIn: https://linkedin.com/

#  Team



---

# ⭐ Project Vision

OPAL-AI aims to become an intelligent healthcare coordination platform that combines:
- AI assistance
- Machine Learning
- Real-time donor coordination
- Healthcare workflow automation

to support faster and smarter donor-recipient matching.