
function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

console.log(validateEmail("test@example.com")); // Output: true
console.log(validateEmail("invalid-email"));    // Output: false
