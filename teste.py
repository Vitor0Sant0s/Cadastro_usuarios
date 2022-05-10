import psycopg2

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

    def add_user(self, nome, email, senha, super_user):
        try:
            con = self.connect()
            cur = con.cursor()

            query = """INSERT INTO usuarios (nome, email, senha, ativo, super_user) VALUES (%s, %s, %s, %s, %s)"""
            query_values = (nome, email, senha, True, super_user)

            cur.execute(query, query_values)
            con.commit()
            print("Usuário adicionado com sucesso!")

        except (Exception, psycopg2.Error) as error:
            print('Failed to insert record into table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")

    def update_user(self, id, nome, email, senha, super_user):
        try:
            con = self.connect()
            cur = con.cursor()

            query = """UPDATE usuarios SET nome = %s, email = %s, senha = %s, super_user = %s WHERE id = %s"""
            query_values = (nome, email, senha, super_user, id)

            cur.execute(query, query_values)
            con.commit()
            print("Usuário atualizado com sucesso!")

        except (Exception, psycopg2.Error) as error:
            print('Failed to update record into table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")

    def delete_user(self, id):
        try:
            con = self.connect()
            cur = con.cursor()

            query = """DELETE FROM usuarios WHERE id = %s"""
            query_values = (id,)

            cur.execute(query, query_values)
            con.commit()
            print("Usuário deletado com sucesso!")

        except (Exception, psycopg2.Error) as error:
            print('Failed to delete record into table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")

    def get_users(self):
        try:
            con = self.connect()
            cur = con.cursor()

            query = """SELECT * FROM usuarios"""

            cur.execute(query)
            con.commit()
            print("Usuários listados com sucesso!")

            return cur.fetchall()

        except (Exception, psycopg2.Error) as error:
            print('Failed to get records from table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")

    def desable_user(self, id):
        try:
            con = self.connect()
            cur = con.cursor()

            query = """UPDATE usuarios SET ativo = False WHERE id = %s"""
            query_values = (id,)

            cur.execute(query, query_values)
            con.commit()
            print("Usuário desativado com sucesso!")

        except (Exception, psycopg2.Error) as error:
            print('Failed to update record into table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")

    def enable_user(self, id):

        try:
            con = self.connect()
            cur = con.cursor()

            query = """UPDATE usuarios SET ativo = True WHERE id = %s"""
            query_values = (id,)

            cur.execute(query, query_values)
            con.commit()
            print("Usuário ativado com sucesso!")

        except (Exception, psycopg2.Error) as error:
            print('Failed to update record into table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")

    def get_user_by_id(self, id):
        try:
            con = self.connect()
            cur = con.cursor()

            query = """SELECT * FROM usuarios WHERE id = %s"""
            query_values = (id,)

            cur.execute(query, query_values)
            con.commit()

            user = cur.fetchall()

            if user:
                print("Usuário encontrado!")
                return user
            else:
                raise Exception("Usuário não encontrado!")

        except (Exception, psycopg2.Error) as error:
            print('Failed to get records from table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")


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
