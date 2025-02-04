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