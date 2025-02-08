$( document ).ready(function (){
    $(".dropdown-trigger").dropdown();

});

setTimeout(function() {
    let messages = document.getElementById('message-container');
    if (messages) {
        messages.style.transition = "opacity 10s";
        messages.style.opacity = "0";
        setTimeout(() => messages.remove(), 10000);
    }
}, 10000);

document.getElementById("fade-button").addEventListener("click", function() {
    let image = document.getElementById("cover-image");
    image.style.transition = "opacity 10s";
    image.style.opacity = 0;
    setTimeout(() => image.remove(), 10000);
});

document.addEventListener("DOMContentLoaded", function() {
    const dateInput = document.querySelector("input[name='date']");
    const timeInput = document.querySelector("input[name='time']");
    const deleteModal = document.getElementById('deleteModal');

    if (dateInput) {
        flatpickr(dateInput, {
            minDate: "today",
            dateFormat: "Y-m-d",
            defaultDate: ["2025-02-05"],
        });
    }

    if (timeInput) {
        flatpickr(timeInput, {
            enableTime: true,
            noCalendar: true,
            dateFormat: "H:i",
            minuteIncrement: 30,
            time_24hr: false,
            defaultDate: "09:30",
            minTime: new Date().toLocaleTimeString([], {hour: '2-digit', minute: '2-digit'})
        });
    }

    deleteModal.addEventListener('show.bs.modal', function (event) {
        const link = event.relatedTarget;
        const serviceName = link.getAttribute("data-service-name");
        const bookingDate = link.getAttribute("data-booking-date");
        const deleteUrl = link.getAttribute("data-delete-url");
        document.getElementById('deleteMessage').innerHTML = 
        `Are you sure you want to delete the <strong>${serviceName}</strong> appointment on <strong>${bookingDate} |</strong> This action cannot be undone.`
        document.getElementById('deleteForm').setAttribute("action", deleteUrl);
    });
    
});
