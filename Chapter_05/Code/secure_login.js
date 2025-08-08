
const bcrypt = require('bcryptjs');
app.post('/login', async (req, res) => {
    const user = await User.findOne({ username: req.body.username });
    if (user && await bcrypt.compare(req.body.password, user.password)) {  // Secure comparison
        return res.json({ message: "Login successful" });
    }
    res.status(401).json({ message: "Invalid credentials" });
});
