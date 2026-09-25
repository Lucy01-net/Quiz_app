from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

quiz = [
    {"question": "What does BTS stand for in Korean?", "answer": "Beyond The Scene"},
    {"question": "Which girl group sings the global hit song Gnarly", "answer": "Katseye"},
    {"question": "What is the official fandom name for BLACKPINK", "answer": "Blink"},
    {"question": "What does the common K-drama phrase Saranghae mean", "answer": "I love you"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_question/<int:index>")
def get_question(index):
    if index < len(quiz):
        return jsonify({"question": quiz[index]["question"]})
    return jsonify({"question": None})

@app.route("/check_answer", methods=["POST"])
def check_answer():
    data = request.json
    index = data["index"]
    user_answer = data["answer"].strip().lower()
    correct_answer = quiz[index]["answer"].lower()

    return jsonify({"correct": user_answer == correct_answer})

if __name__ == "__main__":
    app.run(debug=True)