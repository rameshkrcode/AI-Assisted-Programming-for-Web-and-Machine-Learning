
// AI-generated JSX code using GitHub Copilot (corrected)
import React, { useState } from "react";
const AILoginForm = () => {
    const [email, setEmail] = useState("");
    const [error, setError] = useState("");
    const validateEmail = (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    const handleSubmit = (e) => {
        e.preventDefault();
        if (!validateEmail(email)) {
            setError("Invalid email address");
        } else {
            setError("");
            alert("Login Successful!");
        }
    };
    return (
        <form onSubmit={handleSubmit} className="max-w-md mx-auto p-4 border rounded shadow-lg">
            <label>Email:</label>
            <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="border px-2 py-1 w-full"
            />
            {error && <p className="text-red-500">{error}</p>}
            <button type="submit" className="mt-3 bg-blue-500 text-white px-4 py-2 rounded">
                Login
            </button>
        </form>
    );
};
export default AILoginForm;
