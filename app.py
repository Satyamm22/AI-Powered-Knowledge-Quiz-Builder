import os
import json

from flask import Flask, render_template, request, session
from dotenv import load_dotenv
import google.generativeai as genai


# Load Environment Variables
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


# Flask App
app = Flask(__name__)

app.secret_key = "quiz_secret_key"


@app.route("/", methods=["GET", "POST"])
def home():

    # Initialize session variables
    if "questions" not in session:
        session["questions"] = []

    if "current" not in session:
        session["current"] = 0

    questions = session["questions"]

    if request.method == "POST":

        action = request.form.get("action")

        
        # Generate Quiz
        if action == "generate":

            topic = request.form["topic"]

            prompt = f"""
Generate exactly 5 multiple choice quiz questions on {topic}.

Return ONLY valid JSON.

Format:

[
 {{
   "question":"Question here",
   "options":[
      "Option A",
      "Option B",
      "Option C",
      "Option D"
   ],
   "answer":0,
   "explanation":"Short explanation"
 }}
]

Rules:

- Exactly 5 questions
- answer must be 0,1,2 or 3
- Do not write markdown
- Do not write ```json
- Return ONLY JSON
"""

            response = model.generate_content(prompt)

            response_text = response.text.strip()

            # Remove markdown if Gemini returns it
            if response_text.startswith("```json"):
                response_text = (
                    response_text
                    .replace("```json", "")
                    .replace("```", "")
                    .strip()
                )

            questions = json.loads(response_text)

            session["questions"] = questions
            session["current"] = 0

            session.pop("feedback", None)
            session.pop("selected", None)
            session.pop("explanation", None)

        # ==========================================
        # Submit Answer
        # ==========================================
        elif action == "submit":

            questions = session["questions"]

            current = session["current"]

            selected = int(request.form["answer"])

            correct = questions[current]["answer"]

            if selected == correct:
                session["feedback"] = "correct"
            else:
                session["feedback"] = "wrong"

            session["selected"] = selected
            session["explanation"] = questions[current]["explanation"]

        # ==========================================
        # Next Question
        # ==========================================
        elif action == "next":

            if session["current"] < len(session["questions"]) - 1:
                session["current"] += 1
            else:
                session["current"] = len(session["questions"])

            session.pop("feedback", None)
            session.pop("selected", None)
            session.pop("explanation", None)

    # -------------------------
    # Load current question
    # -------------------------
    questions = session.get("questions", [])

    current = session.get("current", 0)

    # -------------------------
    # Quiz Finished
    # -------------------------
    if questions and current >= len(questions):
        session.clear()
        return render_template("index.html")

    question = None

    if questions:
        question = questions[current]

    return render_template(
        "index.html",
        question=question,
        current=current,
        total=len(questions),
        feedback=session.get("feedback"),
        explanation=session.get("explanation"),
        selected=session.get("selected"),
    )


if __name__ == "__main__":
    app.run(debug=True)