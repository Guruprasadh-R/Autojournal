# 🧠 AutoJournal — AI-Powered Emotional Journal

## 📋 Overview
**AutoJournal** is a Generative AI-powered journaling web app that understands user emotions and provides personalized, empathetic advice.  
It uses NLP models to detect your mood from text entries and generate short, meaningful suggestions to help you reflect, relax, or take action.  

This project blends **AI**, **psychology**, and **self-reflection** — turning simple journaling into an intelligent, supportive experience.

---

## ⚙️ Tech Stack

### 🖥️ Frontend
- **React (Vite)** — Fast, modern frontend framework  
- **Tailwind CSS** — Clean, responsive styling  
- **Axios** — For API communication with backend  

### 🧩 Backend
- **Flask (Python)** — Lightweight and efficient web server  
- **Flask-CORS** — Handles frontend-backend communication  
- **Transformers (Hugging Face)** — For emotion detection and text generation  

---

## 🤖 Hugging Face Models Used

| Task | Model | Description |
|------|--------|-------------|
| **Emotion Detection** | `j-hartmann/emotion-english-distilroberta-base` | Detects emotions such as joy, sadness, anger, fear, and love from journal entries |
| **Advice Generation** | `declare-lab/flan-alpaca-base` | Generates short, empathetic and actionable advice tailored to the detected emotion |

---

## 🧠 Generative AI Approach

AutoJournal uses two GenAI pipelines:
1. **Emotion Classification:**  
   Transformer-based model identifies the dominant emotion from text input.  

2. **Contextual Text Generation:**  
   An instruction-tuned LLM generates short, supportive advice and an actionable step based on the detected emotion and journal context.  

---

## 🚀 How It Works

1. ✍️ User writes a journal entry describing their thoughts or mood.  
2. ⚙️ Flask backend analyzes the text using Hugging Face emotion model.  
3. 💬 Based on the emotion, an AI model generates short empathetic advice.  
4. 🎯 React frontend displays the **emotion** and **AI advice** beautifully.  

---


