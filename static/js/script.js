document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("make-profile").style.display ="none";

    function openTest() {
        document.getElementById("make-profile").style.display = "block";
    }

    document.getElementById('btn').addEventListener('click', openTest);
})