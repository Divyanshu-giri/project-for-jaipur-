document.addEventListener("DOMContentLoaded", () => {
    const careers = ["Web Developer", "AI Engineer", "Digital Marketer", "UX Designer"];
    const list = document.getElementById("career-list");
    careers.forEach(c => {
        const li = document.createElement("li");
        li.textContent = c;
        list.appendChild(li);
    });
});

function goToCourses() {
    window.location.href = "/courses";
}
