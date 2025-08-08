
// Import required libraries
const express = require('express');
const mongoose = require('mongoose');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const app = express();
app.use(express.json()); // Middleware to parse JSON request bodies
// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/authDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});
// Define User Schema
const UserSchema = new mongoose.Schema({
    username: String,
    password: String
});
const User = mongoose.model('User', UserSchema);
// Register User Endpoint
app.post('/register', async (req, res) => {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({ username: req.body.username, password: hashedPassword });
    await user.save();
    res.json({ message: "User registered successfully" });
});
// Login User Endpoint
app.post('/login', async (req, res) => {
    const user = await User.findOne({ username: req.body.username });
    if (user && await bcrypt.compare(req.body.password, user.password)) {
        const token = jwt.sign({ username: user.username }, 'secret', { expiresIn: '1h' });
        return res.json({ token });
    }
    res.status(401).json({ message: "Invalid credentials" });
});
// Start the server
app.listen(5000, () => console.log(`Server is running on port 5000`));
