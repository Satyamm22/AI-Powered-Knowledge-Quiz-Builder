# AI-Powered Knowledge Quiz Builder

An AI-powered quiz application built using **Python**, **Flask**, and the **Google Gemini API**. The application generates topic-based multiple-choice quizzes dynamically and provides instant feedback with explanations for each answer.

---

## Project Overview

This project allows users to generate quizzes on any topic by entering a subject of their choice. The Gemini API creates multiple-choice questions, and the application displays one question at a time.

After selecting an answer, the application immediately informs the user whether the answer is correct or incorrect, displays the correct answer, provides a short explanation, and then allows the user to continue to the next question.

---

## Features

* Generate AI-based quizzes on any topic
* Topic-based multiple-choice questions
* Four answer options for every question
* Instant answer validation
* Explanation for every answer
* One question displayed at a time
* Clean and responsive user interface
* Built using Flask and Google Gemini API

---

## Technologies Used

* Python 3
* Flask
* HTML5
* CSS3
* Google Gemini API
* python-dotenv

---

## Project Structure

```
AI-Powered-Knowledge-Quiz-Builder/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── .env
```

> Note: The `.env` file is not included in this repository because it contains the Gemini API key.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Satyamm22/AI-Powered-Knowledge-Quiz-Builder.git
```

### Move into the project folder

```bash
cd AI-Powered-Knowledge-Quiz-Builder
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

Add your Gemini API key.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run the project

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## How to Use

1. Enter any topic (Example: Python, Photosynthesis, Neural NetworksL).
2. Click **Generate Quiz**.
3. Read the question and select an answer.
4. View instant feedback and explanation.
5. Move to the next question until the quiz is completed.

---

## Future Improvements

* Score calculation
* Progress bar
* Timer for each question
* Difficulty levels
* Quiz history
* User authentication
* Leaderboard

---

## Author

**Satyam Vishwakarma**

B.Tech Graduate (Computer Science)

GitHub: https://github.com/Satyamm22

