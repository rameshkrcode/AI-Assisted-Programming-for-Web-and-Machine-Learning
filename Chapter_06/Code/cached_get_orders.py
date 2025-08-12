
@cache.memoize(timeout=60)  # ✅ AI recommends caching for 60 seconds
def get_orders(user_id):
    return db.query("SELECT * FROM orders WHERE user_id = %s", (user_id,))
