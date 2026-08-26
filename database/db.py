import
from config import  DATABASE

def get_db_connetion():
    conn =   sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connetion()


    conn.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT INIQUE NOT NULL,
        password TEXT NOT NULL,
    )''')
    
    conn.execute('''CREATE TABLE IF NOT EXISTS formular
        id INTEGER PRMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        cpf TEXT NOT NULL,
        genaro TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user (id)
    )''')

    conn.commit()
    conn.close()