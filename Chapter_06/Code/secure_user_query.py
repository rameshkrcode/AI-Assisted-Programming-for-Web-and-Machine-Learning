
def get_user_data(username):
    query = "SELECT * FROM users WHERE username = %s"
    db.execute(query, (username,))  # Secure query execution
    return db.fetchall()
