const navbar = document.querySelector('[data-navbar]');
const scrollToTop = document.querySelector('[data-scroll-up]');

if (scrollToTop) {
    window.addEventListener('scroll', () => {
        const scrollHeight = window.scrollY;
        const navHeight = navbar.getBoundingClientRect().height;
        if (scrollHeight > (navHeight * 2)) {
            scrollToTop.classList.add('show-link');
        } else {
            scrollToTop.classList.remove('show-link');
        }
    });
}