
def create_index_on_username():
    query = "CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);"
    db.execute(query)

def get_user_data(username):
    query = "SELECT * FROM users WHERE username = %s"
    db.execute(query, (username,))
    return db.fetchall()
