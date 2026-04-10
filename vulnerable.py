import random
import sqlite3

# Issue 1: Hardcoded password
DB_PASSWORD = "supersecret123"

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Issue 2: SQL Injection vulnerability
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    return cursor.fetchall()

def generate_token():
    # Issue 3: Insecure random number
    return str(random.randint(100000, 999999))

# Issue 4: Unused variable
unused_count = 42

print(get_user('admin'))
print(generate_token())