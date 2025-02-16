// Wait for the document to be fully loaded before executing the code
$( document ).ready(function (){
    $(".dropdown-trigger").dropdown();

    // Change the opacity of the cover image only when user clicks on the go to booking button
    document.getElementById("fade-button").addEventListener("click", function() {

        // Get the image, set the transition effect for opacity and change the opacity value
        let image = document.getElementById("cover-image");
        image.style.transition = "opacity 10s";
        image.style.opacity = 0.8;
    });

    // Fade out the message container and remove it after 10 seconds
    setTimeout(function() {
        let messages = document.getElementById('message-container');
        if (messages) {
            messages.style.transition = "opacity 10s";
            messages.style.opacity = "0";
            setTimeout(() => messages.remove(), 10000);
        }
    }, 10000);

    // Modal to show the deletion confirmation message
    deleteModal.addEventListener('show.bs.modal', function (event) {

        //Get data attributes 
        const link = event.relatedTarget;
        const serviceName = link.getAttribute("data-service-name");
        const bookingDate = link.getAttribute("data-booking-date");
        const deleteUrl = link.getAttribute("data-delete-url");

        // Set the modal message and action URL
        document.getElementById('deleteMessage').innerHTML = 
        `Are you sure you want to delete the <strong>${serviceName}</strong> appointment on <strong>${bookingDate} |</strong> This action cannot be undone.`
        document.getElementById('deleteForm').setAttribute("action", deleteUrl);
    });

    // Date and Time Picker using flatpickr
    const dateInput = document.querySelector("input[name='date']");
    const timeInput = document.querySelector("input[name='time']");

    if (dateInput) {
        const datepicker = flatpickr(dateInput, {
            minDate: "today", // Disable past dates
            dateFormat: "Y-m-d", // Date format
            defaultDate: ["2025-02-13"], // Set a default date
            onChange: function(selectedDates, dateStr, instance) {
                updateMinTime(dateStr); // Update minimum time when date is changed
            }
        });

        function updateMinTime(selectedDate) {
            if (timeInput) {
                const now = new Date();
                const selected = new Date(selectedDate);
                let minTimeValue = "00:00"; // Default time for future dates

                if (selected.toDateString() === now.toDateString()) {
                    minTimeValue = now.getHours() + ":" + now.getMinutes();
                }

                timepicker.set("minTime", minTimeValue); // Set the minimum time allowed
            }
        }
    }

    if (timeInput) {
        const timepicker = flatpickr(timeInput, {
            enableTime: true, // Enable time selection
            noCalendar: true, // Hide calendar
            dateFormat: "H:i", // Time format
            minuteIncrement: 30, // 30-minute intervals
            time_24hr: false, // 12-hour time format
            defaultDate: "20:28", // Default time
            minTime: new Date().getHours() + ":" + new Date().getMinutes(), // Set minimum time to current time
        });
    }

    // Initialize Bootstrap tooltips for elements with 'data-bs-toggle="tooltip"'
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        new bootstrap.Tooltip(tooltipTriggerEl);
    });
});
