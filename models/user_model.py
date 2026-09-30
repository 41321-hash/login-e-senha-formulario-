import sqlite3  
from database.db import get_db_connection  

class UserModel:
    
    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()  
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()  
        return user  

    @staticmethod
    def create_user(username, password):
        conn = get_db_connection()  
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()  
            return True  
        except sqlite3.IntegrityError:
            return None  
        finally:
            conn.close()  
    @staticmethod
    def get_user_by_id(user_id):
        conn = get_db_connection()
        user = conn.execute('SELECT id, username FROM users WHERE id = ?', (user_id,)).fetchone()
        conn.close()
        return dict(user) if user else None

    @staticmethod
    def update_user(user_id, username, password):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('UPDATE users SET username = ?, password = ? WHERE id = ?', (username, password, user_id))
            conn.commit()
            return cursor.rowcount > 0
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM formularios WHERE user_id = ?', (user_id,))
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        rows = cursor.rowcount
        conn.close()
        return rows > 0