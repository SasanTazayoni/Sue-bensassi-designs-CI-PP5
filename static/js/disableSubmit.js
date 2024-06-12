/* jshint esversion: 11 */

document.addEventListener("DOMContentLoaded", () => {
    const submitButton = document.getElementById("submitButton");
    const resetForm = document.getElementById("resetForm");

    submitButton.addEventListener("click", () => {
        submitButton.disabled = true;
        resetForm.submit();
    });

    setTimeout(() => {
        submitButton.disabled = false;
    }, 3000);
});