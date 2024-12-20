from services.usuario_services import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session
import os 

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    os.system("cls || clear")
    # Criando um usuário.
    service.criar_usuario("Marta23", "marta@gmail.com", "15")

    #Listando todos os usuários.
    print("\nListando todos os usuários.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} -{usuario.email} - {usuario.senha}")

if __name__ == "__main__":
    main() # Chamando para a função 