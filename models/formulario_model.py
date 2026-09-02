import sqlite3
from database.db import get_db_connection

class FormularioModel:

    @staticmethod
    def create_formulario(user_id,nome, email, data_nascimento,cpf,genero):
        conn = get_db_connection()
        try:
            conn.execute('''INSERT INTO formulario (user_id, nome,cpf,data_nascimento,genero)
                            VALUES(?,?,?,?,?,?)''',
                        (user_id,name,email,data_nascimento,cpf,genero))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()