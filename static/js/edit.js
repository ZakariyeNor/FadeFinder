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
