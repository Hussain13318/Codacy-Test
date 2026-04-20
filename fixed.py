import os
import secrets
import sqlite3

# Fix 1, 5, 7: Remove hardcoded password — use environment variable
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Fix 2, 3, 6: Parameterized query prevents SQL Injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

def generate_token():
    # Fix 4: secrets module is cryptographically secure
    return str(secrets.randbelow(900000) + 100000)

print(get_user('admin'))
print(generate_token())