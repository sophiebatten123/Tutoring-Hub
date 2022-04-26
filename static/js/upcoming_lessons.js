const csrftoken = getCookie('csrftoken');

document.addEventListener("DOMContentLoaded", () => { 

    deleteBooking();
    updateBookings();
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function deleteBooking() {
    delete_btn = document.getElementsByClassName("btn-delete");
    console.log("delelete")

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
                window.location.href = "/profile/upcoming_lessons";
            });
        });
    }
}

function updateBookings() {
    var currentDate = new Date();
    var previousDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate() - 1);
    var monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    var previousDate = previousDay.getDate();
    var previousMonth = previousDay.getMonth();
    var previousDateTrial = previousDate + " " + monthNames[previousMonth];
    previousDateWithDayOfWeek = daysOfWeek[previousDay.getDay()] + " " + previousDateTrial;

    booking_dates = document.getElementsByClassName('booking-dates');
    delete_btn = document.getElementsByClassName("btn-delete");

    for (let i=0; i < booking_dates.length; i++) {
        for (let j=0; j < delete_btn.length; j++) {
            if (booking_dates[i].innerHTML == previousDateWithDayOfWeek) {
                delete_btn[j].click();
                deleteBooking();
            } else {
                booking_dates[i].style.backgroundColor = "white";
            }
        }
    }
}