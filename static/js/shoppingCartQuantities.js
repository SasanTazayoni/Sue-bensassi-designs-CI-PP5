const decrementButtons = document.querySelectorAll('[data-decrement]');
const incrementButtons = document.querySelectorAll('[data-increment]');
const updateLinks = document.querySelectorAll('[data-update]');

const handleUpdate = (button) => {
    const form = button.closest('.update-form');
    const productId = form.querySelector('input[data-product]').getAttribute('data-product');
    const quantityInput = document.querySelector(`input[data-product="${productId}"]`);
    const value = quantityInput.getAttribute('value');
    console.log(value);
};

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

updateLinks.forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        handleUpdate(link);
    });
});

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

initialiseButtonState();