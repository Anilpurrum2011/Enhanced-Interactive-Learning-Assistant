
from jinja2 import Template

def generate_report(topic, objective, research, questions):
    template = """
    <h2>Learning Report: {{ topic }}</h2>
    <p><strong>Objective:</strong> {{ objective }}</p>

    <h3>1. Learning Progression</h3>
    <ol>
        <li>Introduction to {{ topic }}</li>
        <li>Understanding Core Concepts</li>
        <li>Advanced Applications & Research</li>
    </ol>

    <h3>2. Research Summary</h3>
    <ul>
      <li><b>Web:</b> {{ research.web }}</li>
      <li><b>Video:</b> {{ research.video }}</li>
      <li><b>Academic:</b> {{ research.academic }}</li>
    </ul>

    <h3>3. Visual Aids</h3>
    <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Artificial_neural_network.svg/1280px-Artificial_neural_network.svg.png' width="500"/>

    <h3>4. Citations & References</h3>
    <ul>
        <li>Wikipedia: https://en.wikipedia.org/wiki/{{ topic.replace(' ', '_') }}</li>
        <li>arXiv: https://arxiv.org/search/?query={{ topic.replace(' ', '+') }}</li>
        <li>Additional references as per LLM response.</li>
    </ul>

    <h3>5. Recommended Resources</h3>
    <ul>
        <li>Book: Deep Learning by Ian Goodfellow</li>
        <li>Video: MIT OCW {{ topic }}</li>
        <li>Course: Coursera / edX on {{ topic }}</li>
    </ul>

    <h3>6. Interactive Questions Asked</h3>
    <ul>
      {% for q in questions.values() %}
        <li>{{ q }}</li>
      {% endfor %}
    </ul>
    """
    return Template(template).render(topic=topic, objective=objective, research=research, questions=questions)
