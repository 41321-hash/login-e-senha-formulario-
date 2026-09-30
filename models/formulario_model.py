import sqlite3 
from database.db import get_db_connection  

class FormularioModel:
    
    @staticmethod
    def create_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()  
        try:
            conn.execute('''INSERT INTO formularios (user_id, nome, email, data_nascimento, cpf, genero)
                             VALUES (?, ?, ?, ?, ?, ?)''', 
                         (user_id, nome, email, data_nascimento, cpf, genero))
            conn.commit()  
            return True  
        except sqlite3.IntegrityError:
            return None  
        finally:
            conn.close()

    @staticmethod
    def get_formularios_by_user(user_id):
        conn = get_db_connection()
        formularios = conn.execute('SELECT * FROM formularios WHERE user_id = ?', (user_id,)).fetchall()
        conn.close()
        return [dict(f) for f in formularios]

    @staticmethod
    def update_formulario(form_id, user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''UPDATE formularios 
                          SET nome = ?, email = ?, data_nascimento = ?, cpf = ?, genero = ?
                          WHERE id = ? AND user_id = ?''', 
                       (nome, email, data_nascimento, cpf, genero, form_id, user_id))
        conn.commit()
        rows = cursor.rowcount
        conn.close()
        return rows > 0

    @staticmethod
    def delete_formulario(form_id, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM formularios WHERE id = ? AND user_id = ?', (form_id, user_id))
        conn.commit()
        rows = cursor.rowcount
        conn.close()
        return rows > 0