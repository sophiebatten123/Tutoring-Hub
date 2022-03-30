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

    document.getElementById("upcoming-lessons").style.display="none";
    document.getElementById("upcoming-lessons-btn").addEventListener("click", upcomingLessons);
    document.getElementById("previous-lessons").style.display="none";
    document.getElementById("previous-lessons-btn").addEventListener("click", previousLessons);
    document.getElementById("profile-btn").addEventListener("click", profilePage);
    document.getElementById("edit-btn").addEventListener("click", editProfile);
    document.getElementById("make-profile").style.display="none";
    document.getElementById("exit-btn").addEventListener("click", closeProfile);

    function upcomingLessons() {
        document.getElementById("upcoming-lessons").style.display="block";
        document.getElementById("previous-lessons").style.display="none";
        document.getElementById("about-me").style.display="none";
        document.getElementById("make-profile").style.display="none";
        document.getElementById("about-subject").style.display="none";
    }

    function previousLessons() {
        document.getElementById("previous-lessons").style.display="block";
        document.getElementById("upcoming-lessons").style.display="none";
        document.getElementById("about-me").style.display="none";
        document.getElementById("make-profile").style.display="none";
        document.getElementById("about-subject").style.display="none";
    }

    function profilePage() {
        document.getElementById("about-me").style.display="block";
        document.getElementById("previous-lessons").style.display="none";
        document.getElementById("upcoming-lessons").style.display="none";
        document.getElementById("make-profile").style.display="none";
        document.getElementById("about-subject").style.display="block";
    }

    function editProfile() {
        document.getElementById("make-profile").style.display="block";
        document.getElementById("about-me").style.display="none";
        document.getElementById("previous-lessons").style.display="none";
        document.getElementById("upcoming-lessons").style.display="none";
        document.getElementById("about-subject").style.display="none";
    }

    function closeProfile() {
        document.getElementById("make-profile").style.display="none";
        document.getElementById("about-me").style.display="block";
    }

    updateBookings()
    deleteBooking()
})

function deleteBooking() {
    delete_btn = document.getElementsByClassName("btn-delete")

    for (i=0; i < delete_btn.length; i++) {
        delete_btn[i].style.backgroundColor = "red";
        delete_btn[i].addEventListener("click", function(event) {
            squareClicked = event.target;
            squareClicked.style.backgroundColor = "green";
            id = squareClicked.value;

            fetch('delete_booking/', {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({
                    id: id,
                })
            })
            .then(data => {
                window.location.href = "/profile";
            })
        })
    }
}

function updateBookings() {
    var currentDate = new Date();
    var secondDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate() + 1);
    var monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    var secondDate = secondDay.getDate();
    var secondMonth = secondDay.getMonth();
    var secondDateTrial = secondDate + " " + monthNames[secondMonth];
    secondDateWithDayOfWeek = daysOfWeek[secondDay.getDay()] + " " + secondDateTrial;

    booking_dates = document.getElementsByClassName("booking-dates");
    booking_id = document.getElementsByClassName("booking-id");

    console.log(secondDateWithDayOfWeek);

    for (var i=0; i < booking_dates.length; i++) {
        if (booking_dates[i].innerHTML == secondDateWithDayOfWeek) {
            booking_dates[i].style.backgroundColor = "red";
        } else {
            return
        }
    }
}