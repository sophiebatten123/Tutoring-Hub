document.addEventListener("DOMContentLoaded", () => { 

    document.getElementById("profile-btn").addEventListener("click", profilePage);
    document.getElementById("edit-btn").addEventListener("click", editProfile);
    document.getElementById("make-profile").style.display="none";
    document.getElementById("exit-btn").addEventListener("click", closeProfile);
    document.getElementById("");


    function profilePage() {
        document.getElementById("about-me").style.display="block";
        document.getElementById("make-profile").style.display="none";
    }

    function editProfile() {
        document.getElementById("make-profile").style.display="block";
        document.getElementById("about-me").style.display="none";
    }

    function closeProfile() {
        document.getElementById("make-profile").style.display="none";
        document.getElementById("about-me").style.display="block";
    }

});