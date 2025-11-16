const questions = [
    "Tell me about a project where you used Python.",
    "How do you approach debugging?",
    "Explain OOP in simple terms."
];
let current = 0;

function submitAnswer() {
    const answer = document.getElementById("answer").value;
    let feedback = "Confidence: Medium | Relevance: Good";
    if (answer.length > 100) feedback = "Confidence: High | Relevance: Excellent";
    document.getElementById("feedback").innerText = feedback;
    current++;
    if (current < questions.length) {
        document.getElementById("question-area").innerText = questions[current];
        document.getElementById("answer").value = "";
    } else {
        document.getElementById("question-area").innerText = "Interview Complete!";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("question-area").innerText = questions[current];
});
