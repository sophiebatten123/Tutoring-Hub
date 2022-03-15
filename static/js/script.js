
document.addEventListener("DOMContentLoaded", () => {
    
    document.getElementById("make-profile").style.display ="none";
    document.getElementById("exit-btn").style.display="none";
    document.getElementById("exit-hide").style.display = "none";
    document.getElementById('create-btn').addEventListener('click', openTest);
    document.getElementById('exit-btn').addEventListener('click', closeTest);
    document.getElementById('bookings').style.display="none";
    document.getElementById('booking-btn').addEventListener('click', openBookings);
    document.getElementById('upcoming-lessons').style.display="none";
    document.getElementById('previous-lessons').style.display="none";

    function openTest() {
        document.getElementById("make-profile").style.display = "block";
        document.getElementById("exit-hide").style.display = "flex";
        document.getElementById("exit-btn").style.display = "inline";
        document.getElementById("create-btn").style.display = "none";
        document.getElementById("create-btn-div").style.display = "none";
    }

    function closeTest() {
        document.getElementById("make-profile").style.display = "none";
        document.getElementById("exit-hide").style.display = "none";
        document.getElementById("exit-btn").style.display = "none";
        document.getElementById("create-btn").style.display = "inline";
        document.getElementById("create-btn-div").style.display = "flex";
    }

    function openBookings() {
        document.getElementById('bookings').style.display = "block";
        document.getElementById('bookings-button').style.display="none";
    }

})