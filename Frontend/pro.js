function checkPasswordStrength() {
    const password = document.getElementById("password").value;
    const strengthResult = document.getElementById("strengthResult");
    const quantumStatus = document.getElementById("quantumSecureStatus");

    // Password Strength Calculation
    let strength = "Weak";
    let suggestions = [];

    if (password.length >= 8 && /[A-Z]/.test(password) && /\d/.test(password) && /[\W_]/.test(password)) {
        strength = "Strong";
    } else if (password.length >= 6) {
        strength = "Medium";
        if (!/[A-Z]/.test(password)) suggestions.push("Add an uppercase letter");
        if (!/\d/.test(password)) suggestions.push("Add a number");
        if (!/[\W_]/.test(password)) suggestions.push("Add a special character");
    } else {
        suggestions.push("Make it at least 6 characters");
    }

    // Display Strength
    strengthResult.innerHTML = `<strong>Strength:</strong> ${strength}`;
    if (suggestions.length > 0) {
        strengthResult.innerHTML += `<br><small>Suggestions: ${suggestions.join(", ")}</small>`;
    }

    // Check for Quantum Security
    if (isQuantumSecure(password)) {
        quantumStatus.innerHTML = `<strong style="color: green;">Password is secure against quantum attacks.</strong>`;
    } else {
        quantumStatus.innerHTML = `<strong style="color: red;">Password is not secure against quantum attacks.</strong>`;
    }
}

// Quantum Security Placeholder
function isQuantumSecure(password) {
    // Example logic: Length and randomness-based check
    return password.length > 12 && /[A-Z]/.test(password) && /\d/.test(password) && /[\W_]/.test(password);
}

// Show Password Toggle
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("showPassword").addEventListener("change", function () {
        const passwordField = document.getElementById("password");
        passwordField.type = this.checked ? "text" : "password";
    });
});
