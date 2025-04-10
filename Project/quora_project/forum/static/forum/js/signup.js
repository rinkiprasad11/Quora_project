document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    
    form.addEventListener('submit', function(e) {
        let isValid = true;
        
        
        const errorMessages = document.querySelectorAll('.error');
        errorMessages.forEach(msg => msg.remove());
        
        const password = document.getElementById('id_password');
        const confirmPassword = document.getElementById('id_confirm_password');
        
        if (password.value !== confirmPassword.value) {
            isValid = false;
            const error = document.createElement('div');
            error.classList.add('error');
            error.innerText = "Passwords do not match!";
            confirmPassword.parentElement.appendChild(error);
        }

        if (!isValid) {
            e.preventDefault();
        }
    });
});
