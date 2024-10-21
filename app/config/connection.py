"""
Docker => Ele traz imagens de versões diferentes com as mesmas instalações, independente do sistema seja diferente
porém a funciiionalidade se torna a mesma.

conteirners são imagens.
"""
import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

os.system("cls || clear")

#Parâmetros de conexão com MYSQL.
db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

#URL de conexão para BD MySQL.
# DATA_BASE_URL = f"mysqul+pymysql://usuario:senha@host:porta/nome_bd"
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"



# Conectando ao banco de dados.
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()

@contextmanager 
def get_db():
    db = Session()# Cria uma Sessão para ações no banco de dados 
    try:
        yield db # Caso a sessão realize todas as tarefas, salva a operação 
        db.commit()
    except Exception as erro:
        db.rollback() # Desfaz todas as alterações em caso de erro em alguma operação 
        raise erro # Lança uma exceção 
    finally: 
        db.close() # Fecha sessão com banco de dados 