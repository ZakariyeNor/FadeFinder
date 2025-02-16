// Wait for the DOM to be fully loaded before executing the code
document.addEventListener("DOMContentLoaded", function() {

    // Select the input elements for date and time
    const dateInput = document.querySelector("input[name='date']");
    const timeInput = document.querySelector("input[name='time']");

    // If the date input exists, initialize the datepicker with the specified options
    if (dateInput) {
        /**
         * Initialize the flatpickr datepicker for the date input field. 
         * Set the minimum date
         * choose date format and default time
         */
        const datepicker = flatpickr(dateInput, {
            minDate: "today",
            dateFormat: "Y-m-d",
            defaultDate: ["2025-02-12"],
            onChange: function(selectedDates, dateStr, instance) {

                // When the date is changed, call the function to update the minimum time for the timepicker
                updateMinTime(dateStr);
            }
        });

        // function to update the minimum time value based on the selected date
        function updateMinTime(selectedDate) {
            if (timeInput) {
                // Get the current time and the selected date
                const now = new Date();
                const selected = new Date(selectedDate);
                
                // Set the default minimum time for future dates
                let minTimeValue = "00:00";

                // If the selected date is today, set the minimum time to the current time
                if (selected.toDateString() === now.toDateString()) {
                    minTimeValue = now.getHours() + ":" + now.getMinutes();
                }

                // Update the minimum time for the timepicker
                timepicker.set("minTime", minTimeValue);
            }
        }
    }

    // If the time input exists, initialize the timepicker with the specified options
    if (timeInput) {
        // Initialize the flatpickr timepicker for the time input field
        const timepicker = flatpickr(timeInput, {
            enableTime: true,          // Enable time selection
            noCalendar: true,          // Disable calendar selection (only time)
            dateFormat: "H:i",         // Define the format for the time
            minuteIncrement: 30,       // Set minute increment to 30 minutes
            time_24hr: false,          // Use 12-hour time format (AM/PM)
            defaultDate: "20:28",      // Set the default time
            minTime: new Date().getHours() + ":" + new Date().getMinutes(), // Set the minimum time to the current time
        });
    }
});