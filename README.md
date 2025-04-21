# 🧠 Learning Assistant 

Hey there! 👋

Welcome to the **Enhanced Interactive Learning Assistant**, a personal project where I combined my passion for AI, learning, and software development to build a tool that feels like your personal research companion.

This project uses a local LLM (LLaMA3 through Ollama) to simulate smart research and generate personalized, well-structured reports based on your topic of interest.

---

## 🚀 Quick Setup

Before diving in, make sure you have:

- ✅ [Ollama](https://ollama.com) installed and ready
- ✅ Docker installed

### Step 1: Fire up the LLM

```bash
ollama run llama3
```

> ⚠️ Heads-up: LLaMA3 is memory-hungry. Make sure you have ~6 GB free RAM. If not, consider a lighter model.

### Step 2: Build and launch the app

```bash
docker build -t learning-assistant .
docker run -p 8000:8000 learning-assistant
```

Now hit up your browser at `http://localhost:8000/docs` to test the API. Simple, right? 😎

---

## 🧩 How It Works (Architecture)

Here’s the rough flow of what’s happening under the hood:

1. You send a topic or question to the backend (FastAPI).
2. The backend talks to the local LLM via Ollama.
3. It then processes that info, structures it, and uses Jinja2 to make it readable and pretty.
4. You get a nicely crafted HTML-style report back.

It’s all dockerized too – just two commands and you're good to go.

---

## 🔍 How Research Is Simulated

Instead of scraping live websites or YouTube, I crafted dynamic prompts to simulate how a human would research from:

- Blogs
- Videos
- Academic papers

It feels natural and layered without needing actual crawling.

---

## 🎯 Making It Personal

Everyone learns differently, so the assistant tries to adapt by asking:

- “What level are you at?” (Beginner, Pro, somewhere in between?)
- “Want a summary or full guide?”
- “Need visuals or want it concise?”

This helps it shape the tone and format of the final report.

---

## 📘 Report Magic

Every report you get follows a clean structure:

- **Intro**: What’s this topic?
- **Core Concepts**: Explained simply
- **Deep Dive**: Advanced stuff (if needed)
- **Visual Aids**: Links or diagrams
- **Follow-ups**: What next?

There’s even a `/update-report` endpoint so you can ask it to refine or tweak parts based on feedback.

---

## 🧪 Sample Input & Output

### Input JSON

```json
{
  "topic": "Machine Learning vs Deep Learning",
  "audience_level": "intermediate",
  "format": "structured_report"
}
```

### Output HTML Snippet

```html
<h1>Machine Learning vs Deep Learning</h1>
<p>Machine Learning is a subset of AI that focuses on...</p>

<h2>Key Differences</h2>
<ul>
  <li>Data requirements</li>
  <li>Model complexity</li>
  <li>Interpretability</li>
</ul>
```

Sample outputs are included in the `/samples` folder.

---

## 🔒 Known Limitations

- Needs Ollama + enough RAM to run LLaMA3
- Doesn’t fetch real-time data – all info is simulated via LLM
- No fancy UI (yet!) – it’s all API for now

---

## 🧠 Future Ideas

Here’s what I want to build next:

- Persistent sessions (remember users & their topics)
- PDF export of reports
- Bookmarking & history
- Vector database for better memory
- Maybe a frontend UI?

---

## ✅ Submission Checklist

- [x] App runs with just 2 commands
- [x] Dockerized backend
- [x] README you're reading now 😄
- [x] Sample reports included
- [x] Well-structured codebase
- [x] Prioritized core features

---

## 📸 Bonus: Add Demo Media

- Swagger `/docs`
- Input prompt
- HTML report preview


---

## 🙋‍♂️ About Me

Hey! I’m **Anil**, a final-year B.Tech student (AI/ML) at SRM University, AP. I love building smart tools with AI and simplifying complex concepts. This project was my attempt to do just that.

Thanks for checking it out. Hope it’s helpful or at least sparks some ideas! 🙌

