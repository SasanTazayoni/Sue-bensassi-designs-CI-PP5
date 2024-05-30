document.addEventListener('DOMContentLoaded', () => {
    const decrementBtn = document.querySelector('[data-decrement]');
    const incrementBtn = document.querySelector('[data-increment]');
    const quantityInput = document.querySelector('input[data-product]');

    const updateButtonState = () => {
        const currentValue = parseInt(quantityInput.value);
        const minValue = parseInt(quantityInput.min);
        const maxValue = parseInt(quantityInput.max);

        if (currentValue <= minValue) {
            decrementBtn.classList.add('disabled');
        } else {
            decrementBtn.classList.remove('disabled');
        }

        if (currentValue >= maxValue) {
            incrementBtn.classList.add('disabled');
        } else {
            incrementBtn.classList.remove('disabled');
        }
    };

    decrementBtn.addEventListener('click', e => {
        e.preventDefault();
        let currentValue = parseInt(quantityInput.value);
        if (currentValue > parseInt(quantityInput.min)) {
            quantityInput.value = currentValue - 1;
            updateButtonState();
        }
    });

    incrementBtn.addEventListener('click', e => {
        e.preventDefault();
        let currentValue = parseInt(quantityInput.value);
        if (currentValue < parseInt(quantityInput.max)) {
            quantityInput.value = currentValue + 1;
            updateButtonState();
        }
    });

    updateButtonState();
});