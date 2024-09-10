document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registrationForm');

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        
        const firstName = document.getElementById('firstName').value;
        const lastName = document.getElementById('lastName').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const dob = document.getElementById('dob').value;
        const address = document.getElementById('address').value;
 
        if (!firstName || !lastName || !email || !phone || !dob || !address) {
            alert('Please fill in all fields.');
            return;
        }
        
        alert('Registration successful!');
        form.reset();
    });
});
