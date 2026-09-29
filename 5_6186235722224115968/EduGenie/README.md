# 🎓 EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant designed to make
learning simpler, faster, and more personalized.

It provides five core learning capabilities:

- 💬 **Q&A** — Ask academic and general learning questions.
- 🧠 **Concept Explanation** — Break difficult concepts into beginner-friendly explanations.
- 📝 **Quiz Generation** — Generate 3 MCQs with 4 options each from a topic or passage.
- 📚 **Summarization** — Turn long educational passages into concise revision notes.
- 🗺️ **Learning Path** — Generate a beginner-to-advanced study roadmap.

The project uses **FastAPI** for the backend, **HTML/CSS/Jinja2** for the web interface,
**Google Gemini** for cloud-based generative AI, and a **LaMini-Flan-T5** model
for the local explanation feature.

> **Note:** The project document describes Gemini 1.5 Pro. This implementation keeps
> the Gemini model configurable through `GEMINI_MODEL`, so the repository can use a
> currently available Gemini model without changing application code.

---

## ✨ Features

| Feature | Endpoint | Purpose |
|---|---|---|
| Q&A | `POST /qa` | Answer student questions |
| Explain | `POST /explain` | Simplify difficult concepts |
| Quiz | `POST /quiz` | Generate 3 MCQs |
| Summary | `POST /summarize` | Summarize long text |
| Learning Path | `POST /learn/recommendations` | Create a structured roadmap |

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │     Student        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  HTML + CSS + JS   │
                    │     Frontend       │
                    └──────────┬──────────┘
                               │ HTTP POST
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI       │
                    │      main.py       │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
     Q&A Module          Quiz Module          Summary Module
     qna.py              quiz_module.py       summary_module.py
          │                    │                    │
          └────────────────────┼────────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │   Google Gemini    │
                    └─────────────────────┘

                    Explanation Module
                            │
                            ▼
                  LaMini-Flan-T5 (local)
```

---

## 📁 Project Structure

```text
EduGenie/
│
├── main.py
├── gemini_client.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── tests/
│   └── test_api.py
│
├── .env.example
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🛠️ Technology Stack

### Backend
- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

### AI
- Google Gemini API
- Google GenAI Python SDK
- LaMini-Flan-T5-783M
- Hugging Face Transformers
- PyTorch

### Frontend
- HTML5
- CSS3
- JavaScript
- Jinja2

### Testing
- Pytest
- FastAPI TestClient

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/EduGenie.git
cd EduGenie
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Then add your Gemini API key:

```env
GEMINI_API_KEY=your_real_api_key
GEMINI_MODEL=gemini-2.5-flash
```

**Never commit `.env` to GitHub.**

### 5. Run the application

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## 🔑 Getting a Gemini API Key

Create a Gemini API key through Google AI Studio and store it in the
`GEMINI_API_KEY` environment variable.

Do not put your API key directly inside Python source code.

---

## 🔌 API Documentation

Once the server is running:

```text
Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc
```

### Example Request

```http
POST /qa
Content-Type: application/json
```

```json
{
  "text": "What is machine learning?"
}
```

### Example Response

```json
{
  "result": "Machine learning is a branch of artificial intelligence..."
}
```

---

## 🧪 Testing

Run:

```bash
pytest
```

The tests verify the home page and health endpoint without requiring a Gemini
API call.

---

## 📌 How the Modules Work

### Q&A

`qna.py` sends the student's question to Gemini with an educational prompt
and returns the generated answer.

### Explanation

`explanation_module.py` attempts to use the local
`MBZUAI/LaMini-Flan-T5-783M` model. If the local model cannot be loaded,
it falls back to Gemini so the application can still provide explanations.

### Quiz

`quiz_module.py` requests exactly three MCQs and validates the returned JSON
before sending it to the frontend.

### Summary

`summary_module.py` asks Gemini to preserve important information while
removing repetition and unnecessary detail.

### Learning Path

`learning_path.py` asks Gemini to organize a topic from beginner to advanced
and include practice and learning resources.

---

## 🔐 Security Notes

- Never commit API keys.
- Keep `.env` local.
- Use `.env.example` for configuration documentation.
- Add authentication and rate limiting before exposing the API publicly.
- Validate and limit user input.
- Review AI-generated educational content before using it as authoritative
  academic material.

---

## 🚧 Limitations

- AI-generated answers may contain inaccuracies.
- Gemini API access requires an API key.
- Local LaMini-Flan-T5 inference can require significant RAM and disk space.
- The current version does not include user accounts or persistent learning
  history.
- The current version is a lightweight educational assistant rather than a
  full Learning Management System.

---

## 🔮 Future Scope

Possible future enhancements include:

- 🎙️ Voice-based interaction
- 🌐 Multilingual learning
- 📱 Android/iOS application
- 📊 Learning progress dashboard
- 🏆 Badges, streaks, and gamification
- 🧠 Adaptive learning paths
- 👨‍🏫 Teacher/parent dashboards
- 👥 Group study sessions
- 🏫 Moodle / Google Classroom integration
- 📄 PDF and image-based question solving
- 🔔 Smart learning notifications

---

## 📄 Project Reference

This repository implementation is based on the supplied EduGenie project
document, which defines the project around Q&A, simplified explanations,
quiz generation, summarization, personalized learning paths, FastAPI,
HTML/CSS, Gemini, and LaMini-Flan-T5.

---

## 📜 License

This project is released under the MIT License.

---

## 👨‍💻 Author

**EduGenie Contributors**

Built as an educational AI project focused on accessible and personalized
learning.
