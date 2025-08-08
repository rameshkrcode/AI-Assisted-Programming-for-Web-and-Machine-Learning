
const cache = new Map();
app.get('/products', async (req, res) => {
    if (cache.has("products")) {
        return res.json(cache.get("products"));
    }
    const products = await db.query("SELECT * FROM products ORDER BY created_at DESC");
    cache.set("products", products);
    
    res.json(products);
});
