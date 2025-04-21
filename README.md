
# 📚 Enhanced Interactive Learning Assistant (with Ollama LLM)

## 🔧 Setup Instructions

1. Start Ollama with:
```bash
ollama run llama3
```

2. Build and run the app:
```bash
docker build -t learning-assistant .
docker run -p 8000:8000 learning-assistant
```

## 🧠 System Architecture

- **FastAPI** backend for handling user input & serving content
- **Ollama** LLM for local research and generation
- **Jinja2** for report templating
- Modular services for extensibility

## 🔍 Research Methodology

- Prompts sent to LLM to simulate research from:
  - Web content
  - Video transcripts
  - Academic sources

## 🎯 Personalization Approach

- Asks questions to clarify interest, level, and format
- Adapts report content accordingly

## 📝 Report Features

- Structured sections (progression from basic to advanced)
- Diagrams and visual links
- Resource recommendations and citations
- Interactive Q&A captured

## 🔄 Modifications

- `/update-report` endpoint allows feedback-driven changes

## 🚫 Limitations

- Ollama is required to be locally running
- Simulated research (no live crawling)

## 🚀 Future Upgrades

- Add persistent user sessions
- Allow PDF export and bookmarking
- Use vector databases for memory
