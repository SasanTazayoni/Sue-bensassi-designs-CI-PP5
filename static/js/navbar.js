document.addEventListener('DOMContentLoaded', function() {
    // Function to update margin-top of the top container
    function updateMarginTop() {
        // Get the height of the navbar
        const navbarHeight = document.querySelector('header').offsetHeight + 5; // Add 5 pixels

        // Get the container element with the data attribute
        const container = document.querySelector('[data-top-block]');
        
        // If container exists, update its margin-top
        if (container) {
            container.style.marginTop = navbarHeight + 'px';
        }
    }

    // Initial update when the page is loaded
    updateMarginTop();

    // Update when window is resized
    window.addEventListener('resize', updateMarginTop);
});