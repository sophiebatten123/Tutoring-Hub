function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

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

function confirmBooking(){
    
    var confirmDate = document.getElementById("confirm-date");
    var confirmTime = document.getElementById("confirm-time");
    var tutorName = document.getElementById("tutor-name");
    var subjectName = document.getElementById("subject");

    /* Upon click of the confirm booking button the users selection of date and time are recognised.
    If the user has not selected a date or time an error message will be displayed on the screen.
    If the user has selected a date and time this will be booked and the data will be sent to thier database.*/
    
    if (confirmDate.innerHTML === '' || confirmTime.innerHTML === '') {
        alert("Please select a date and time");
    } else {
        var date = confirmDate.innerHTML;
        var time = confirmTime.innerHTML;
        var tutor = tutorName.innerHTML;
        var subject = subjectName.innerHTML;


        // Date and time variables are sent to the users database via the fetch function.
        fetch("confirm_booking/", {
            method: "POST",
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/json; charset=UTF-8',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                date: date,
                time: time,
                tutor: tutor,
                subject: subject
            })
        })
        .then(response => {
            if(!response.ok) {
                console.log(response);
                throw Error("Error");
            }
            return response.json();
        })
        .then(data => {
            window.location.href = "/profile";
        })
        .catch(error => {
            console.log(error);
        });
    }
}