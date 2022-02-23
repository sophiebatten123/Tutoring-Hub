
document.addEventListener("DOMContentLoaded", () => {
    
    document.getElementById("make-profile").style.display ="none";
    document.getElementById("exit-btn").style.display="none";
    document.getElementById('create-btn').addEventListener('click', openTest);
    document.getElementById('exit-btn').addEventListener('click', closeTest);

    function openTest() {
        document.getElementById("make-profile").style.display = "block";
        document.getElementById("exit-btn").style.display = "inline";
        document.getElementById("create-btn").style.display = "none";
        document.getElementById("create-btn-div").style.display = "none";
    }

    function closeTest() {
        document.getElementById("make-profile").style.display = "none";
        document.getElementById("exit-btn").style.display = "none";
        document.getElementById("create-btn").style.display = "inline";
        document.getElementById("create-btn-div").style.display = "flex";
    }
})