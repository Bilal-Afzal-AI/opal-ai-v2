# 🏥 OPAL-AI — AI-Powered Organ & Blood Donor Matching Platform

<p align="center">
  <img src="assets/screenshots/dashboard.png" width="100%" alt="OPAL-AI Banner"/>
</p>

<p align="center">
  <b>Intelligent Healthcare Matching System using AI, Machine Learning, FastAPI, Next.js, and Supabase</b>
</p>

---

# 🚨 The Problem

Every day, hospitals and healthcare organizations face critical delays in finding compatible blood and organ donors.

Traditional donor coordination systems often rely on:
- manual searching
- fragmented hospital records
- delayed communication
- spreadsheet-based workflows
- inconsistent prioritization

These inefficiencies can slow emergency response times and directly impact patient outcomes.

---

# 💡 The Solution — OPAL-AI

OPAL-AI is an intelligent healthcare platform designed to streamline and automate donor-recipient matching using:

- 🧠 Artificial Intelligence
- 🤖 Machine Learning
- 📍 Geo-aware matching
- ⚡ Real-time analytics
- 🏥 Healthcare workflow automation

The platform intelligently ranks compatible donors based on:
- blood compatibility
- organ compatibility
- urgency level
- geographic distance
- donor availability
- ML-based suitability scoring

---

# ✨ Key Features

## 🔹 Donor Management
- Blood donor registration
- Organ donor registration
- Hospital management
- Real-time donor database

---

## 🔹 Intelligent Matching Engine
- Blood compatibility matching
- Organ compatibility matching
- Distance-aware ranking
- Urgency-based prioritization
- Availability scoring
- AI-enhanced recommendations

---

## 🔹 AI Healthcare Assistant
- Gemini-powered chatbot
- Donor matching explanations
- Healthcare workflow guidance
- Intelligent support responses

---

## 🔹 Dashboard Analytics
- Blood group distribution charts
- Organ donor analytics
- Urgency breakdown visualization
- Match request history
- Real-time dashboard metrics

---

## 🔹 Machine Learning Integration
- RandomForest ranking model
- Hybrid rule-based + ML scoring
- Predictive donor suitability ranking
- Synthetic dataset generation pipeline

---

# 🧠 System Architecture

<p align="center">
  <img src="assets/screenshots/architecture-diagram.png" width="100%" alt="Architecture Diagram"/>
</p>

---

# 🛠️ Tech Stack

# Frontend
- Next.js
- TypeScript
- Tailwind CSS
- Recharts

# Backend
- FastAPI
- Python
- Pydantic
- REST APIs

# Database
- Supabase

# AI & ML
- Google Gemini AI
- Scikit-learn
- Pandas
- NumPy
- Joblib

# Tools & DevOps
- GitHub
- Docker (In Progress)

---

# 📂 Project Structure

```bash
OPAL-AI V2/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── database/
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
├── assets/
│   └── screenshots/
│
└── README.md
```

---

# 📸 Screenshots

## 📊 Dashboard

<p align="center">
  <img src="assets/screenshots/dashboard.png" width="100%" />
</p>

---

## 🩸 Blood Donor Management

<p align="center">
  <img src="assets/screenshots/blood-donors.png" width="100%" />
</p>

---

## 🫀 Organ Donor Management

<p align="center">
  <img src="assets/screenshots/organ-donors.png" width="100%" />
</p>

---

## 🏥 Hospital Management

<p align="center">
  <img src="assets/screenshots/hospitals.png" width="100%" />
</p>

---

## 🤝 Intelligent Matching Engine

<p align="center">
  <img src="assets/screenshots/matching.png" width="100%" />
</p>

---

## 📜 Match Request History

<p align="center">
  <img src="assets/screenshots/match-history.png" width="100%" />
</p>

---

## 🤖 AI Chatbot Assistant

<p align="center">
  <img src="assets/screenshots/chatbot.png" width="100%" />
</p>

---

## ⚙️ FastAPI Swagger Documentation

<p align="center">
  <img src="assets/screenshots/api-docs.png" width="100%" />
</p>

---

# ⚙️ Installation Guide

# 1️⃣ Clone Repository

```bash
git clone https://github.com/Bilal-Afzal-AI/opal-ai-v2.git
cd opal-ai-v2
```

---

# 🔧 Backend Setup

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

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

## Run Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```txt
http://127.0.0.1:8000
```

---

# 💻 Frontend Setup

## Install Packages

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

## Run Frontend

```bash
npm run dev
```

Frontend URL:

```txt
http://localhost:3000
```

---

# 🤖 Machine Learning Pipeline

## Generate Training Dataset

```bash
python app/ml/scripts/generate_training_data.py
```

---

## Train ML Model

```bash
python app/ml/scripts/train_ranking_model.py
```

---

# 📈 Current Capabilities

✅ AI-powered donor matching  
✅ Machine learning ranking engine  
✅ Gemini healthcare chatbot  
✅ Real-time analytics dashboard  
✅ Geo-aware donor scoring  
✅ Match request tracking  
✅ Full-stack healthcare platform  
✅ Supabase cloud database integration  

---

# 🔒 Future Improvements

- JWT Authentication
- Role-Based Access Control
- Docker Deployment
- CI/CD Pipelines
- Cloud Deployment
- Real Healthcare Dataset Integration
- Advanced Deep Learning Ranking
- Mobile Application

---

# 🌍 Project Vision

OPAL-AI aims to become an intelligent healthcare coordination platform that combines:

- AI Assistance
- Machine Learning
- Real-time Donor Coordination
- Healthcare Workflow Automation

to support faster, smarter, and more efficient donor-recipient matching systems.

---
---

# 🤝 Team & Contributions

## 👨‍💻 Bilal Mohammad Afzal
- Project Creator & Lead Developer
- AI/ML Integration
- Backend & Frontend Development
- Healthcare Matching System Design


## 👩‍💻 Mariuram
A very supportive and hardworking teammate who contributed with dedication, collaboration, and continuous support throughout the development of OPAL-AI.Her teamwork, effort, and positive contribution played an important role in the project’s progress and success.

---

# ⭐ Support

If you found this project helpful, consider giving it a star ⭐ on GitHub.

It helps support the project and increases visibility.
