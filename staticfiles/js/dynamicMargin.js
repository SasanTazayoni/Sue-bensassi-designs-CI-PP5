/* jshint esversion: 11 */

document.addEventListener('DOMContentLoaded', function() {
    function updateMarginTop() {
        const navbarHeight = document.querySelector('header').offsetHeight + 5;
        const topContainers = document.querySelectorAll('[data-top-block]');
        
        // If there are any containers, update their margin-top
        if (topContainers.length > 0) {
            topContainers.forEach(container => {
                container.style.marginTop = navbarHeight + 'px';
            });
        }
    }

    updateMarginTop();
    window.addEventListener('resize', updateMarginTop);
});