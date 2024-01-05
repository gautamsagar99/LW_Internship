
function validateForm() {
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;
    var email = document.getElementById('email').value;
console.log('inside');
    // Ensure passwords match
    if (password !== confirmPassword) {
        alert("Passwords do not match");
        return;
    }

    // Validate email format
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("Invalid email format");
        return;
    }

    // Display success message
    // alert("Registration successful!");

    submitForm();
}



async function submitForm() {
    const form = document.getElementById("registrationForm");
    const formData = new FormData(form);

    const jsonObject = {};
    formData.forEach((value, key) => {
        jsonObject[key] = value;
    });
   
    try {
        const response = await fetch("http://127.0.0.1:8000/register", {
            method: "POST",
            body: JSON.stringify({ "user": jsonObject }),
        });

        if (response.ok) {
            alert("Registration successful!");
            form.reset(); // Clear the form after successful registration
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
        }
    } catch (error) {
        console.error("Error submitting the form:", error);
        alert("An error occurred while processing your request. Please try again later.");
    }
}