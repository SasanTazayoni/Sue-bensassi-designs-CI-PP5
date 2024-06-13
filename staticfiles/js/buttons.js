/* jshint esversion: 11 */

const btns = document.querySelectorAll('.button');

btns.forEach(btn => {
    btn.addEventListener('mousemove', e => {
        let rect = e.target.getBoundingClientRect();
        let x = e.clientX * 1.5 - rect.left;
        btn.style.setProperty('--x', x + 'deg');
    })
})