/* jshint esversion: 11 */

const navbar = document.querySelector('[data-navbar]');
const scrollToTop = document.querySelector('[data-scroll-up]');

if (scrollToTop) {
    window.addEventListener('scroll', () => {
        const scrollHeight = window.scrollY;
        const navHeight = navbar.getBoundingClientRect().height;
        const windowHeight = window.innerHeight;
        const bodyHeight = document.body.scrollHeight;
        const distanceFromBottom = bodyHeight - (scrollHeight + windowHeight);

        if (scrollHeight > (navHeight * 2) && distanceFromBottom > 200) {
            scrollToTop.classList.add('show-link');
        } else {
            scrollToTop.classList.remove('show-link');
        }
    });
}