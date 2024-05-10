window.onscroll = function() {scrollFunction()};
    
function scrollFunction() {
    const navbar = document.querySelector('.navbar');
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Function to update margin-top of hero container
    function updateMarginTop() {
        // Get the height of the navbar
        const navbarHeight = document.querySelector('header').offsetHeight + 5; // Add 5 pixels

        // Set the margin-top of the hero container
        const heroContainer = document.querySelector('.hero-container');
        if (heroContainer) {
            heroContainer.style.marginTop = navbarHeight + 'px';
        }
    }

    // Initial update
    updateMarginTop();

    // Update when window is resized
    window.addEventListener('resize', updateMarginTop);
});