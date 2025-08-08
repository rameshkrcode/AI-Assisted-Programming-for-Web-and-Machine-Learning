
app.get('/products', async (req, res) => {
    const products = await db.query("SELECT * FROM products ORDER BY created_at DESC");
    res.json(products);
});
