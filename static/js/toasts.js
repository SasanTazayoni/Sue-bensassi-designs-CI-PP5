/* jshint esversion: 11 */
/* globals bootstrap */

document.addEventListener('DOMContentLoaded', () => {
    const toastElements = document.querySelectorAll('.toast');
    
    toastElements.forEach(function(toastElement) {
        const toast = new bootstrap.Toast(toastElement);
        toast.show();

        document.addEventListener('click', e => {
            if (!toastElement.contains(e.target)) {
                toast.hide();
            }
        });

        toastElement.addEventListener('click', e => {
            e.stopPropagation();
        });

        const closeButton = toastElement.querySelector('.btn-close');

        if (closeButton) {
            closeButton.addEventListener('click', e => {
                e.stopPropagation();
                toast.hide();
            });
        }
    });
});