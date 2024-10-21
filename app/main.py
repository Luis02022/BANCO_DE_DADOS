from services.usuario_services import UsuarioService
from repositeries.usuario_repositery import UsuarioRepository
from config.connection import Session


def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Criando um usuário.
    service.criar_usuario("Marta", "marta@gmail.com", "15")

    #Listando todos os usuários.
    print("\nListando todos os usuários.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} -{usuario.email} - {usuario.senha}")

if __name__ == "__main__":
    main() # chamando para a função