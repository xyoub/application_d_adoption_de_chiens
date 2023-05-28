let currentTitle = document.title;
window.addEventListener("blur", () => {
    document.title = "Adopte_mo 🐕‍🦺🐶";
});
window.addEventListener("focus", () => {
    document.title = currentTitle;
});
