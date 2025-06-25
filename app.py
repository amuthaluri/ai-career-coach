import random
from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Motivational quotes
QUOTES = [
    "Success is not the key to happiness. Happiness is the key to success.",
    "Opportunities don't happen, you create them.",
    "The only way to do great work is to love what you do.",
    "Don't watch the clock; do what it does. Keep going.",
    "Believe you can and you're halfway there.",
    "Your dream job does not exist. You must create it."
]

# Coding challenges
CHALLENGES = [
    {"title": "FizzBuzz", "desc": "Write a program that prints the numbers from 1 to 100. But for multiples of three print 'Fizz' instead of the number and for the multiples of five print 'Buzz'. For numbers which are multiples of both three and five print 'FizzBuzz'."},
    {"title": "Palindrome Checker", "desc": "Write a function to check if a given string is a palindrome."},
    {"title": "Two Sum", "desc": "Given an array of integers, return indices of the two numbers such that they add up to a specific target."},
    {"title": "Reverse a Linked List", "desc": "Write a function to reverse a singly linked list."},
    {"title": "Valid Parentheses", "desc": "Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid."}
]

# Simulated AI responses
def ai_response(user_input):
    user_input = user_input.lower()
    if "interview" in user_input:
        return "Prepare by practicing coding problems, mock interviews, and reviewing common questions for your target role."
    elif "resume" in user_input:
        return "Keep your resume concise, highlight achievements, and tailor it to each job application."
    elif "python" in user_input:
        return "Practice Python coding challenges and review data structures, algorithms, and libraries like Flask or Django."
    elif "job" in user_input:
        return "Network on LinkedIn, apply widely, and keep learning new skills. Persistence is key!"
    elif "fail" in user_input or "rejected" in user_input:
        return "Rejection is redirection! Learn from feedback and keep improving. Every great developer has faced setbacks."
    elif "negotiat" in user_input:
        return "Research salary ranges, know your worth, and be confident but polite when negotiating offers."
    else:
        return "Stay curious, keep learning, and don't hesitate to ask for help. You're on the right path!"

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat" not in session:
        session["chat"] = []
    chat = session["chat"]
    quote = random.choice(QUOTES)
    challenge = random.choice(CHALLENGES)
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            chat.append(f"You: {user_input}")
            chat.append(f"Coach: {ai_response(user_input)}")
            session["chat"] = chat
        return redirect(url_for("index"))
    return render_template("index.html", quote=quote, challenge=challenge, chat=chat)

if __name__ == "__main__":
    app.run(debug=True)