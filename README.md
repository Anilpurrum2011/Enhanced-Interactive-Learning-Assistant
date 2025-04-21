#  Enhanced Interactive Learning Assistant (Powered by Ollama LLM)

##  Overview

This project is a modular and extensible **Interactive Learning Assistant** powered by a local LLM (LLaMA3 via Ollama) and a FastAPI backend. It simulates personalized research, generates structured reports, and enables iterative improvement based on user feedback.

---

## ✅ Expected Deliverables

1. ✅ **Working Prototype**: Handles topic research, report generation, and feedback updates.
2. ✅ **Source Code**: Well-organized and documented in a Dockerized environment.
3. ✅ **Sample Topics & Reports**: Available in the `/samples` folder.
4. ✅ **README File**: (You are reading it) – details setup, architecture, and methodology.
5. ✅ **Sample Input/Output**: Included below.

---

##  Setup Instructions

> Requires: Docker, Ollama (installed and running locally), Python 3.9+

### 1. Install and Start Ollama
Install Ollama: https://ollama.com

Start the LLaMA3 model:
```bash
ollama run llama3
```

>  **Note**: Ensure your system has at least **6 GB** free RAM. If not, consider using a lighter model or a cloud-based LLM API.

### 2. Build and Run the Application
```bash
docker build -t learning-assistant .
docker run -p 8000:8000 learning-assistant
```

Access at: `http://localhost:8000/docs` (FastAPI Swagger UI)

---

##  System Architecture

```
Client (Browser or Tool)
       │
       ▼
+---------------------------+
|        FastAPI App        |
+---------------------------+
│  ├─ /generate-report      │
│  ├─ /update-report        │
│  └─ OllamaService         │
│           │
│           ▼
│     [LLaMA3 via Ollama]
│
└─ Templates (Jinja2)
       └─ HTML Reports
```

- **Backend**: Python + FastAPI
- **LLM**: LLaMA3 via Ollama (local inference)
- **Templating**: Jinja2 for HTML reports
- **Dockerized**: 1-line setup for full system

---

##  Research Methodology

Prompts are structured and dynamically created to simulate research from:

- General web content
- Video transcripts (simulated)
- Academic-style literature

This method enables **context-aware** content generation without live crawling.

---

##  Personalization Approach

The system adapts responses based on:

-  User interest (technical, creative, academic)
-  Skill level (beginner, intermediate, expert)
-  Preferred format (summary, full report, Q&A)

Interactive Q&A helps refine reports progressively.

---

##  Report Generation

- **Structured Output**: Sections build from fundamentals to advanced topics.
- **Enhanced Content**:
  - Diagrams & visual resource links
  - Summaries and explanations
  - References and follow-up suggestions
- **Templated Reports** using Jinja2

---

##  Report Modification API

**Endpoint**: `/update-report`

Allows:
- Feedback-driven modifications
- Regeneration of specific sections
- Personalization tuning

---

##  Sample Input/Output

###  Input Prompt:
```json
{
  "topic": "Quantum Computing for Beginners",
  "audience_level": "beginner",
  "format": "structured_report"
}
```

###  Output:
```html
<h1>Introduction to Quantum Computing</h1>
<p>Quantum computing leverages quantum bits, or qubits, which can exist in multiple states at once...</p>

<h2>Core Concepts</h2>
<ul>
  <li>Superposition</li>
  <li>Entanglement</li>
  <li>Quantum Gates</li>
</ul>

<h3>Visual Resources</h3>
<p><a href="https://example.com/quantum-visual">Quantum Concepts in Visuals</a></p>

<h3>Next Steps</h3>
<p>To dive deeper, explore Qiskit by IBM...</p>
```

 Sample reports can be found in `/samples/reports/`

---

##  Limitations

-  Ollama LLM must be running locally – high memory usage (~6 GB).
-  No live data fetching – all research is simulated.
-  UI not implemented – currently backend API only.

---

##  Future Improvements

-  Persistent user sessions with history
-  PDF export and bookmarking
-  Vector store for user memory/contextual follow-up
-  Optional cloud LLM fallback (for low-RAM systems)
-  Web-based frontend UI

---

##  Submission Checklist

- [x] **Code Repository**: Organized and modular
- [x] **Docker Setup**: Single command deployment
- [x] **README**: Full setup and architectural guide
- [x] **Sample Reports**: Provided for evaluation
- [x] **Demo Media**: Screenshots or screen recording included
- [x] **Focus on Core Features**: Prioritized functionality

---

##  Technology Justification

- **FastAPI**: Lightweight, async-ready API framework
- **Ollama**: Offline-friendly LLM platform
- **Docker**: Clean, portable deployment
- **Jinja2**: Flexible templating for content formatting

---

##  Demo Screenshots

> ![WhatsApp Image 2025-04-21 at 21 35 25_63f04a8f](https://github.com/user-attachments/assets/26ec7cb2-c198-430e-b026-05bf39320c83)
> ![WhatsApp Image 2025-04-21 at 21 38 36_2f85c4e7](https://github.com/user-attachments/assets/8600ae03-5da8-4458-a1a6-9a925b6e3a2e)
> ![WhatsApp Image 2025-04-21 at 21 41 55_9ad610e8](https://github.com/user-attachments/assets/419c5207-c4a0-4d49-825d-eadc4f8837d7)

---

##  Author

**Annaiah** – Final year B.Tech (AI/ML), SRM University, AP  
Passionate about AI, software engineering, and building meaningful tools with LLMs.
---
