# 🧠 Incident Triage Pipeline

AI-powered Streamlit application that classifies, prioritises, and logs engineering incidents using structured AI analysis and deterministic scoring.

---

## 🚀 Live App

👉 https://incident-triage-pipeline-nvlnwpsx68qzavj7puq8mz.streamlit.app/

---

## 📌 Overview

This project simulates a real-world engineering triage system where incident descriptions are:

```
Input → AI Analysis → Structured Output → Scoring → Prioritised Dashboard
```

The application combines:
- Large Language Models (OpenAI)
- Structured parsing logic
- Deterministic scoring
- Interactive dashboarding (Streamlit)

---

## ⚙️ Features

- 📝 Free-text incident input  
- 🤖 AI-generated analysis:
  - Cause  
  - Severity  
  - Priority  
  - Owner  
  - Recommended action  
- 🧱 Structured parsing of AI output  
- 📊 Incident log stored in session  
- 🔢 Priority & severity scoring  
- 📈 Automatic sorting (highest priority first)  
- 🌐 Cloud deployment via Streamlit  

---

## 🧱 System Architecture

```
User Input
   ↓
Streamlit UI
   ↓
OpenAI API (LLM)
   ↓
Structured Text Output
   ↓
Custom Parsing Function
   ↓
Data Model (dict → DataFrame)
   ↓
Scoring + Sorting Logic
   ↓
Dashboard Display
```

---

## 🧠 How It Works

### 1. Input
User enters an incident description via Streamlit UI.

### 2. AI Analysis
The app sends the incident to OpenAI with a structured prompt:

```text
Cause:
Severity:
Priority:
Owner:
Action:
```

---

### 3. Parsing
Custom Python function converts AI output into structured fields:

```python
parsed = parse_response(output)
```

---

### 4. Scoring

Text values are converted into numerical scores:

```python
priority_score_map = {"P1": 3, "P2": 2, "P3": 1}
severity_score_map = {"High": 3, "Medium": 2, "Low": 1}
```

---

### 5. Storage

Results are stored in session state:

```python
st.session_state["log"].append(result)
```

---

### 6. Display

Data is converted to a DataFrame and sorted:

```python
df = df.sort_values(by=["priority_score", "severity_score"], ascending=False)
```

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **OpenAI API**
- **Pandas**

---

## ▶️ Running Locally

### 1. Clone repo

```bash
git clone https://github.com/craig-automation/incident-triage-pipeline.git
cd incident-triage-pipeline
```

---

### 2. Create virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API key

Create file:

```bash
.streamlit/secrets.toml
```

Add:

```toml
OPENAI_API_KEY = "your_api_key_here"
```

---

### 5. Run app

```bash
streamlit run app.py
```

---

## 🔐 Security

- API keys are stored using Streamlit Secrets  
- No sensitive data is committed to the repository  

---

## 📈 Future Improvements

- Add incident categorisation (Electrical / Mechanical / Hydraulic)  
- Add confidence scoring  
- Persist data to database (SQLite / cloud)  
- Add alerting for P1 incidents  
- Improve UI with charts and filters  

---

## 📄 CV Summary

Built an AI-powered incident triage pipeline that classifies, prioritises, and logs engineering incidents using Streamlit and OpenAI. Implemented structured parsing, scoring logic, and prioritised dashboard views to simulate real-world engineering workflows.

---

## 🧭 Key Learning Outcomes

- Designing AI-driven workflows  
- Structuring LLM outputs for reliability  
- Combining AI + deterministic logic  
- Building and deploying full-stack data apps  
- Managing secrets securely in production  

---

## 👤 Author

Craig Parker  
GitHub: https://github.com/craig-automation

---
