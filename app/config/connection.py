"""
Docker => Ele traz imagens de versões diferentes com as mesmas instalações, independente do sistema seja diferente
porém a funciiionalidade se torna a mesma.

conteirners são imagens.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

#URL de conexão para BD MySQL.
DATA_BASE_URL = f"mysqul+pymysql://usuario:senha@host:porta/nome_bd"