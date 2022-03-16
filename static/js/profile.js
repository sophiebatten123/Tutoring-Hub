document.addEventListener("DOMContentLoaded", () => { 

    document.getElementById("upcoming-lessons").style.display="none";
    document.getElementById("upcoming-lessons-btn").addEventListener("click", upcomingLessons);
    document.getElementById("previous-lessons").style.display="none";
    document.getElementById("previous-lessons-btn").addEventListener("click", previousLessons);
    document.getElementById("profile-btn").addEventListener("click", profilePage);
    document.getElementById("edit-btn").addEventListener("click", editProfile);
    document.getElementById("make-profile").style.display="none";
    document.getElementById("exit-btn").addEventListener("click", closeProfile)


    function upcomingLessons() {
        document.getElementById("upcoming-lessons").style.display="block";
        document.getElementById("previous-lessons").style.display="none";
        document.getElementById("about-me").style.display="none";
        document.getElementById("make-profile").style.display="none";
    }

    function previousLessons() {
        document.getElementById("previous-lessons").style.display="block";
        document.getElementById("upcoming-lessons").style.display="none";
        document.getElementById("about-me").style.display="none";
        document.getElementById("make-profile").style.display="none";
    }

    function profilePage() {
        document.getElementById("about-me").style.display="block";
        document.getElementById("previous-lessons").style.display="none";
        document.getElementById("upcoming-lessons").style.display="none";
        document.getElementById("make-profile").style.display="none";
    }

    function editProfile() {
        document.getElementById("make-profile").style.display="block";
        document.getElementById("about-me").style.display="none";
        document.getElementById("previous-lessons").style.display="none";
        document.getElementById("upcoming-lessons").style.display="none";
    }

    function closeProfile() {
        document.getElementById("make-profile").style.display="none";
        document.getElementById("about-me").style.display="block";
    }

})