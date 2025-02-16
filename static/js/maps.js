// Initialize and add map
let map;

// Asynchronous map fetch
async function initMap() {
    // The barber booking center location
    const position = { lat: 57.708870, lng: 11.974560 };

    // Request necessary libraries
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    // Center the map at the barber booking position
    map = new Map(document.getElementById("map"), {
        zoom: 13,
        center: position,
        mapId: "a578d8204d3bd0b1"
    });

    // Marker position at the barber booking center
    const marker = new AdvancedMarkerElement({
        map: map,
        position: position,  // Set position of the marker
        title: "Barber Booking Center",  // Marker title
    });
    
    
}

// Initialize the map when the page is loaded
initMap();

// Function to toggle the visibility of the subcategory 
function toggleSubCategory() {
    //Get the value of the category input and the element that represents the developer subcategory secion
    const category = document.getElementById('categoryInput').value;
    const developerSubCategory = document.getElementById('developerSubCategory');

    // Now this logic checks if the selected category is developer
    if (category === 'Developer') {

        // show if the develoer is selected
        developerSubCategory.style.display = 'block';
    } else {

        // Otherwise, hide the developer subcategory 
        developerSubCategory.style.display = 'none';
    }
}

