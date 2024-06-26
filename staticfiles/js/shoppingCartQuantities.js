/* jshint esversion: 11 */

document.addEventListener('DOMContentLoaded', () => {
    const decrementButtons = document.querySelectorAll('[data-decrement]');
    const incrementButtons = document.querySelectorAll('[data-increment]');
    const updateLinks = document.querySelectorAll('[data-update]');
    let newValue = 0;

    // Set button initial state
    const initialiseButtonState = () => {
        decrementButtons.forEach(button => {
            const productId = button.closest('.update-form').querySelector('input[data-product]').getAttribute('data-product');
            const quantityInput = document.querySelector(`input[data-product="${productId}"]`);
            updateButtonState(quantityInput);
        });

        incrementButtons.forEach(button => {
            const productId = button.closest('.update-form').querySelector('input[data-product]').getAttribute('data-product');
            const quantityInput = document.querySelector(`input[data-product="${productId}"]`);
            updateButtonState(quantityInput);
        });
    };

    // Decrease quantity input
    decrementButtons.forEach(button => {
        button.addEventListener('click', e => {
            e.preventDefault();
            const productId = button.closest('.update-form').querySelector('input[data-product]').getAttribute('data-product');
            const quantityInput = document.querySelector(`input[data-product="${productId}"]`);

            let currentValue = parseInt(quantityInput.value);
            if (currentValue > parseInt(quantityInput.min)) {
                newValue = currentValue - 1;
                quantityInput.value = newValue;
                updateButtonState(quantityInput);
            }
        });
    });

    // Increase quantity input
    incrementButtons.forEach(button => {
        button.addEventListener('click', e => {
            e.preventDefault();
            const productId = button.closest('.update-form').querySelector('input[data-product]').getAttribute('data-product');
            const quantityInput = document.querySelector(`input[data-product="${productId}"]`);

            let currentValue = parseInt(quantityInput.value);
            if (currentValue < parseInt(quantityInput.max)) {
                newValue = currentValue + 1;
                quantityInput.value = newValue;
                updateButtonState(quantityInput);
            }
        });
    });

    // Disable button if minimum/maximum quantity reached
    const updateButtonState = (quantityInput) => {
        const currentValue = parseInt(quantityInput.value);
        const minValue = parseInt(quantityInput.min);
        const maxValue = parseInt(quantityInput.max);
        const decrementButton = quantityInput.parentNode.querySelector('[data-decrement]');
        const incrementButton = quantityInput.parentNode.querySelector('[data-increment]');

        if (currentValue === minValue) {
            decrementButton.classList.add('disabled');
        } else {
            decrementButton.classList.remove('disabled');
        }

        if (currentValue === maxValue) {
            incrementButton.classList.add('disabled');
        } else {
            incrementButton.classList.remove('disabled');
        }
    };

    updateLinks.forEach(link => {
        link.addEventListener('click', e => {
            e.preventDefault();
            handleUpdate(link);
        });
    });

    // Handle form submission and update cart quantity of the specified item
    const handleUpdate = (button) => {
        const form = button.closest('.update-form');
        const productId = form.querySelector('input[data-product]').getAttribute('data-product');
        const quantityInput = document.querySelector(`input[data-product="${productId}"]`);
        const value = parseInt(quantityInput.getAttribute('value'));
        newValue = parseInt(quantityInput.value);

        if (newValue !== value) {
            quantityInput.setAttribute('value', newValue);
            form.submit();
        } else {
            console.log("Value hasn't changed, not submitting the form.");
        }
    };

    initialiseButtonState();
});