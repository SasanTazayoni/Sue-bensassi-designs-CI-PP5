/* jshint esversion: 11, jquery: true */

const logoutLink = document.getElementById('logout-link');

if (logoutLink) {
    logoutLink.addEventListener('click', e => {
        e.preventDefault();
        $('#logoutConfirmationModal').modal('show');
    });
}