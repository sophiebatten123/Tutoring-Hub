window.onload = dateGenerator()

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
    document.getElementById("bookings-button").style.display="none";
    document.getElementById("exit-booking").addEventListener("click", closeBooking);
    document.getElementById("confirm-btn").addEventListener("click", confirmBooking);
    document.getElementById("create-review").addEventListener("click", openForm);
    document.getElementById("review-container").style.display = "none";

    
    function openBooking() {
        document.getElementById("bookings").style.display="block";
        document.getElementById("bookings-button").style.display="none";
        document.getElementById("tutor-profile").style.display="none";
        document.getElementById("qualifications").style.display="none";
    }

    function closeBooking() {
        document.getElementById("bookings").style.display="none";
        document.getElementById("tutor-profile").style.display="block";
        document.getElementById("bookings-button").style.display="block";
        document.getElementById("confirm-date").innerHTML = '';
        document.getElementById("confirm-time").innerHTML = '';
        clearBooking();
    }

    selectDate()
    checkBookings()
})

function selectDate(){
    date = document.getElementsByClassName("day-slot");
    confirmDay = document.getElementById("confirm-date");
    confirmTime = document.getElementById("confirm-time");
    tutor_one_bookings = document.getElementById("tutor_one_bookings");


    //Resets the innerhtml of the booking for time when a new date is selected.
    confirmTime.innerHTML = ''

    for (i=0; i < date.length; i++) {
        date[i].style.backgroundColor = "white";
        date[i].addEventListener("click", function(event) {
            squareClicked = event.target;
            squareClicked.style.backgroundColor = "green";
            confirmDay.innerHTML = squareClicked.innerHTML
            selectTime(squareClicked.innerHTML)
        })
    }
}

function selectTime(date){
    var i=0;
    document.getElementById("time-slots").style.opacity = "100%"
    time = document.getElementsByClassName("time-slot");
    tutorName = document.getElementById('tutor-name').innerHTML;
    tutor_one_dates = document.getElementsByClassName('tutor_one_dates');
    tutor_two_dates = document.getElementsByClassName('tutor_two_dates');
    tutor_three_dates = document.getElementsByClassName('tutor_three_dates');
    time = document.getElementsByClassName("time-slot");
    confirmTime = document.getElementById("confirm-time");

    for (j=0; j < time.length; j++) {
        time[j].style.backgroundColor = 'white';
        time[j].style.display = 'block';
        time[j].addEventListener("click", function(event) {
            squareClicked = event.target;
            squareClicked.style.backgroundColor = "green";
            confirmTime.innerHTML = squareClicked.innerHTML;
        })
    }

    if (tutorName == 'Barry Hyman') {
        for (i=0; i < tutor_one_dates.length; i++) {
            if (date == tutor_one_dates[i].innerHTML) {
                tutorOneTimes(i);
            } else {

            }
        }
    } else if (tutorName == "Jennifer Roberts") {
        for (i=0; i < tutor_two_dates.length; i++) {
            if (date == tutor_two_dates[i].innerHTML) {
                tutorTwoTimes(i);
            } else {
                
            }
        }
    } else {
        for (i=0; i < tutor_three_dates.length; i++) {
            if (date == tutor_three_dates[i].innerHTML) {
                tutorThreeTimes(i);
            } else {
                
            }
        }
    }
}

function tutorOneTimes(i){
    tutor_one_times = document.getElementsByClassName('tutor_one_times');
    time = document.getElementsByClassName("time-slot");
    confirmTime = document.getElementById("confirm-time");

    for (j=0; j < tutor_one_times.length; j++) {
        let j = i;
        for (k=0; k < time.length; k++) {
            time[k].style.backgroundColor = "white";
            if (time[k].innerHTML == tutor_one_times[j].innerHTML) {
                time[k].style.display = 'none'
            } else {
            }

            time[k].addEventListener("click", function(event) {
                squareClicked = event.target;
                squareClicked.style.backgroundColor = "green";
                confirmTime.innerHTML = squareClicked.innerHTML;
            })
        }
    }
}

function tutorTwoTimes(i){
    tutor_two_times = document.getElementsByClassName('tutor_two_times');
    time = document.getElementsByClassName("time-slot");
    confirmTime = document.getElementById("confirm-time");

    for (j=0; j < tutor_two_times.length; j++) {
        let j = i;
        for (k=0; k < time.length; k++) {
            time[k].style.backgroundColor = "white";
            if (time[k].innerHTML == tutor_two_times[j].innerHTML) {
                time[k].style.display = 'none'
            } else {
            }

            time[k].addEventListener("click", function(event) {
                squareClicked = event.target;
                squareClicked.style.backgroundColor = "green";
                confirmTime.innerHTML = squareClicked.innerHTML;
            })
        }
    }
}

function tutorThreeTimes(i){
    tutor_three_times = document.getElementsByClassName('tutor_three_times');
    time = document.getElementsByClassName("time-slot");
    confirmTime = document.getElementById("confirm-time");

    for (j=0; j < tutor_three_times.length; j++) {
        let j = i;
        for (k=0; k < time.length; k++) {
            time[k].style.backgroundColor = "white";
            if (time[k].innerHTML == tutor_three_times[j].innerHTML) {
                time[k].style.display = 'none'
            } else {
            }

            time[k].addEventListener("click", function(event) {
                squareClicked = event.target;
                squareClicked.style.backgroundColor = "green";
                confirmTime.innerHTML = squareClicked.innerHTML;
            })
        }
    }
}

function confirmBooking(){
    
    var confirmDate = document.getElementById("confirm-date");
    var confirmTime = document.getElementById("confirm-time");
    var tutorName = document.getElementById("tutor-name");
    var subjectName = document.getElementById("subject");
    var time = document.getElementsByClassName("time-slot")

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
        .then(data => {
            window.location.href = "/profile";
        })
        .catch(error => {
            console.log(error);
        });
        
    }
}

function dateGenerator() {
    var day_one = document.getElementById("day-one");
    var day_two = document.getElementById("day-two");
    var day_three = document.getElementById("day-three");
    var day_four = document.getElementById("day-four");
    var day_five = document.getElementById("day-five");

    // Gets the next 7 week days
    var currentDate = new Date();
    var secondDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate() + 1);
    var thirdDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate() + 2);
    var fourthDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate() + 3);
    var fifthDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate() + 4);
    var sixthDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate() + 5);

    // Uses naming notation to get them written in long form
    var monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    var secondDate = secondDay.getDate();
    var secondMonth = secondDay.getMonth();

    var thirdDate = thirdDay.getDate();
    var thirdMonth = thirdDay.getMonth();

    var fourthDate = fourthDay.getDate();
    var fourthMonth = fourthDay.getMonth();

    var fifthDate = fifthDay.getDate();
    var fifthMonth = fifthDay.getMonth();

    var sixthDate = sixthDay.getDate();
    var sixthMonth = sixthDay.getMonth();

    // Denotes the new days of the week
    var secondDateTrial = secondDate + " " + monthNames[secondMonth];
    var thirdDateTrial = thirdDate + " " + monthNames[thirdMonth];
    var fourthDateTrial = fourthDate + " " + monthNames[fourthMonth];
    var fifthDateTrial = fifthDate + " " + monthNames[fifthMonth];
    var sixthDateTrial = sixthDate + " " + monthNames[sixthMonth];

    secondDateWithDayOfWeek = daysOfWeek[secondDay.getDay()] + " " + secondDateTrial;
    thirdDateWithDayOfWeek = daysOfWeek[thirdDay.getDay()] + " " + thirdDateTrial;
    fourthDateWithDayOfWeek = daysOfWeek[fourthDay.getDay()] + " " + fourthDateTrial;
    fifthDateWithDayOfWeek = daysOfWeek[fifthDay.getDay()] + " " + fifthDateTrial;
    sixthDateWithDayOfWeek = daysOfWeek[sixthDay.getDay()] + " " + sixthDateTrial;  

    day_one.innerHTML = secondDateWithDayOfWeek;
    day_two.innerHTML = thirdDateWithDayOfWeek;
    day_three.innerHTML = fourthDateWithDayOfWeek;
    day_four.innerHTML = fifthDateWithDayOfWeek;
    day_five.innerHTML = sixthDateWithDayOfWeek;

}

function clearBooking() {
    var date = document.getElementsByClassName("day-slot");
    var time = document.getElementsByClassName("time-slot");

    for (var i=0; i < date.length; i++) {
        date[i].style.backgroundColor = "white";
    }

    for (var i=0; i < time.length; i++) {
        time[i].style.backgroundColor = "white";
    }
}

function openForm() {
    document.getElementById("review-container").style.display = "block";
}
  
function closeForm() {
    document.getElementById("review-container").style.display = "none";
}
