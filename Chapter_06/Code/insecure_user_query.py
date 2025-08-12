
def get_user_data(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"  # SQL Injection risk
    db.execute(query)  
    return db.fetchall()
