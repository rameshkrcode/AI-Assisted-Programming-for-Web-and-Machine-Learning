@app.route('/users')
def get_users():
    # Get 'page' and 'limit' from query parameters with default values
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit
    # Use LIMIT and OFFSET for pagination
    users = db.query("SELECT * FROM users LIMIT %s OFFSET %s", (limit, offset))
    return jsonify(users)
