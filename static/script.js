let index = 0;
let total = 0;

function loadQuestion() {
    fetch(`/get_question/${index}`)
        .then(res => res.json())
        .then(data => {
            if (data.question) {
                total = data.total;
                document.getElementById("question-box").innerText = data.question;
            } else {
                document.getElementById("question-box").innerText = "Quiz Finished!";
                document.getElementById("answer-input").style.display = "none";
                document.querySelector("button").style.display = "none";
            }
        });
}

function submitAnswer() {
    if (index >= total) return;

    const answer = document.getElementById("answer-input").value;

    fetch("/check_answer", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({index, answer})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = data.correct ? "Correct!" : "Wrong!";
        index++;
        document.getElementById("answer-input").value = "";
        loadQuestion();
    });
}

loadQuestion();
