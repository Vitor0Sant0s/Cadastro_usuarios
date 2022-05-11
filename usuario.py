import psycopg2


class User:
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password


USER = "postgres"
PASSWORD = "postgres"
DBNAME = "sistema_cadastro_usuarios"
HOST = "localhost"


class Connection:
    def __init__(self, user, password, dbname, host):
        self.__user = user
        self.__password = password
        self.__dbname = dbname
        self.__host = host

    def connect(self):
        try:
            con = psycopg2.connect(
                user=self.__user,
                password=self.__password,
                host=self.__host,
                database=self.__dbname
            )
            return con

        except (Exception, psycopg2.Error) as error:
            print('Failed to connect to PostgreSQL', error)


connect = Connection(user=USER, password=PASSWORD,
                     dbname=DBNAME, host=HOST)


lista = []

for user in connect.get_users():
    usuario = connect.get_user_by_id(user[0])
    print(f'''
        usuario: {usuario[0][1]}
        email: {usuario[0][2]}
        senha: {usuario[0][3]}
        ativo: {usuario[0][4]}
        super_user: {usuario[0][5]}
        ''')
    lista.append(usuario[0][2])
# [(id, nome, email, senha, ativo, super_user)]

print(lista)
