document.addEventListener("DOMContentLoaded", () => { 

    document.getElementById("edit-btn").addEventListener("click", editProfile);
    document.getElementById("edit-profile").style.display="none";
    document.getElementById("exit-btn").addEventListener("click", closeProfile);
    document.getElementById("about-me-text").style.display="block";


    function editProfile() {
        document.getElementById("edit-profile").style.display="block";
        document.getElementById("about-me-text").style.display="none";
    }

    function closeProfile() {
        document.getElementById("edit-profile").style.display="none";
        document.getElementById("about-me-text").style.display="block";
    }

});