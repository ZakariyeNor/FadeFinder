document.addEventListener("DOMContentLoaded", function() {
    const dateInput = document.querySelector("input[name='date']");
    const timeInput = document.querySelector("input[name='time']");
    const deleteModal = document.getElementById('deleteModal');

    if (dateInput) {
        flatpickr(dateInput, {
            minDate: "today",
            dateFormat: "Y-m-d",
            defaultDate: ["2025-02-12"],
        });
    }

    if (timeInput) {
        flatpickr(timeInput, {
            enableTime: true,
            noCalendar: true,
            dateFormat: "H:i",
            minuteIncrement: 30,
            time_24hr: false,
            defaultDate: "10:00",
            minTime: new Date().toLocaleTimeString([], {hour: '2-digit', minute: '2-digit'})
        });
    }
    
    
});
