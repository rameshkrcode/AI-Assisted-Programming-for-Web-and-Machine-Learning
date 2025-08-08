
app.post('/login', async (req, res) => {
    const user = await User.findOne({ username: req.body.username });
    if (user.password === req.body.password) {  // Insecure comparison
        return res.json({ message: "Login successful" });
    }
    res.status(401).json({ message: "Invalid credentials" });
});
