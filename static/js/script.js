$( document ).ready(function (){
    $(".dropdown-trigger").dropdown();

});

document.getElementById("fade-button").addEventListener("click", function() {
    let image = document.getElementById("cover-image");
    image.style.transition = "opacity 10s";
    image.style.opacity = 0.8;
});

setTimeout(function() {
    let messages = document.getElementById('message-container');
    if (messages) {
        messages.style.transition = "opacity 10s";
        messages.style.opacity = "0";
        setTimeout(() => messages.remove(), 10000);
    }
}, 10000);


document.addEventListener("DOMContentLoaded", function() {

    deleteModal.addEventListener('show.bs.modal', function (event) {
        const link = event.relatedTarget;
        const serviceName = link.getAttribute("data-service-name");
        const bookingDate = link.getAttribute("data-booking-date");
        const deleteUrl = link.getAttribute("data-delete-url");
        document.getElementById('deleteMessage').innerHTML = 
        `Are you sure you want to delete the <strong>${serviceName}</strong> appointment on <strong>${bookingDate} |</strong> This action cannot be undone.`
        document.getElementById('deleteForm').setAttribute("action", deleteUrl);
    });

    document.addEventListener("DOMContentLoaded", function() {
        const form = document.getElementById("barber-form");
    
        if (form) {
            form.addEventListener("submit", function(event) {
                const barberId = document.getElementById("barber_id").value;
                console.log("Submitting form with barber_id:", barberId);
            });
        }
    });
    
    
});

document.addEventListener("DOMContentLoaded", function() {
    const dateInput = document.querySelector("input[name='date']");
    const timeInput = document.querySelector("input[name='time']");

    if (dateInput) {
        const datepicker = flatpickr(dateInput, {
            minDate: "today",
            dateFormat: "Y-m-d",
            defaultDate: ["2025-02-12"],
            onChange: function(selectedDates, dateStr, instance) {
                updateMinTime(dateStr);
            }
        });

        function updateMinTime(selectedDate) {
            if (timeInput) {
                const now = new Date();
                const selected = new Date(selectedDate);
                let minTimeValue = "00:00"; // Default for future dates

                if (selected.toDateString() === now.toDateString()) {
                    minTimeValue = now.getHours() + ":" + now.getMinutes();
                }

                timepicker.set("minTime", minTimeValue);
            }
        }
    }

    if (timeInput) {
        const timepicker = flatpickr(timeInput, {
            enableTime: true,
            noCalendar: true,
            dateFormat: "H:i",
            minuteIncrement: 30,
            time_24hr: false,
            defaultDate: "20:28",
            minTime: new Date().getHours() + ":" + new Date().getMinutes(),
        });
    }
});

