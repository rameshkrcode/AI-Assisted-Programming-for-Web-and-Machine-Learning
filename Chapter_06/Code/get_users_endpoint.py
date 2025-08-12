@app.route('/users')
def get_users():
    users = db.query("SELECT * FROM users")  # Fetches all user data, causing slow response
    return jsonify(users)
