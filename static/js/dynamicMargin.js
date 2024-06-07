document.addEventListener('DOMContentLoaded', function() {
    function updateMarginTop() {
        // Get the height of the navbar
        const navbarHeight = document.querySelector('header').offsetHeight + 5; // Add 5 pixels

        // Get all container elements with the data attribute
        const topContainers = document.querySelectorAll('[data-top-block]');
        
        // If there are any containers, update their margin-top
        if (topContainers.length > 0) {
            topContainers.forEach(container => {
                container.style.marginTop = navbarHeight + 'px';
            });
        }
    }

    // Initial update when the page is loaded
    updateMarginTop();

    // Update when window is resized
    window.addEventListener('resize', updateMarginTop);
});