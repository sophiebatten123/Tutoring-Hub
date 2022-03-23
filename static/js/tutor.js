document.addEventListener("DOMContentLoaded", () => {
    
    document.getElementById("booking-btn").addEventListener("click", openBooking);
    document.getElementById("tutor-profile").style.display="none";
    document.getElementById("bookings-button").style.display="none";
    document.getElementById("proile-btn").addEventListener("click", openProfile);
    document.getElementById("qualifications-btn").addEventListener("click", openQualifications);
    document.getElementById("qualifications").style.display="none";
    document.getElementById("exit-booking").addEventListener("click", closeBooking);
    document.getElementById("confirm-btn").addEventListener("click", confirmBooking)
    
    function openBooking() {
        document.getElementById("bookings").style.display="block";
        document.getElementById("bookings-button").style.display="none";
        document.getElementById("tutor-profile").style.display="none";
        document.getElementById("qualifications").style.display="none";
    }

    function openProfile() {
        document.getElementById("bookings").style.display="none";
        document.getElementById("tutor-profile").style.display="block";
        document.getElementById("bookings-button").style.display="block";
        document.getElementById("qualifications").style.display="none";
    }

    function openQualifications() {
        document.getElementById("qualifications").style.display="block";
        document.getElementById("bookings").style.display="none";
        document.getElementById("tutor-profile").style.display="none";
        document.getElementById("bookings-button").style.display="block";
    }

    function closeBooking() {
        document.getElementById("bookings").style.display="none";
        document.getElementById("tutor-profile").style.display="block";
        document.getElementById("bookings-button").style.display="block";
    }

})

function selectDate(){
    var date = document.getElementsByClassName("day-slot");
    var confirmDay = document.getElementById("confirm-date");

    for (i=0; i < date.length; i++) {
        date[i].style.backgroundColor = "white";
        date[i].addEventListener("click", function(event) {
            squareClicked = event.target;
            squareClicked.style.backgroundColor = "green";
            confirmDay.innerHTML = squareClicked.innerHTML
        })
    }
}

function selectTime(){
    var time = document.getElementsByClassName("time-slot");
    var confirmTime = document.getElementById("confirm-time");

    for (var i=0; i < time.length; i++) {
        time[i].style.backgroundColor = "white";
        time[i].addEventListener("click", function(event) {
            squareClicked = event.target;
            squareClicked.style.backgroundColor = "green";
            confirmTime.innerHTML = squareClicked.innerHTML
        })
    }
}

function confirmBooking(event){
    var confirmDate = document.getElementById("confirm-date");
    var confirmTime = document.getElementById("confirm-time");

    if (confirmDate.innerHTML === '' || confirmTime.innerHTML === '') {
        alert("Please select a date and time");
    } else {
        console.log(confirmDate.innerHTML);
        console.log(confirmTime.innerHTML);
    }
}