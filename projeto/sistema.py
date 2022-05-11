import psycopg2 as pg


class Sistema:
    def __init__(self, usuario, senha):
        pass


class Conexao:
    def __init__(self, host, database, usuario, senha):
        self.__host = host
        self.__database = database
        self.__usuario = usuario
        self.__senha = senha

    def conectar(self):
        try:
            con = pg.connect(
                user=self.__user,
                password=self.__password,
                host=self.__host,
                database=self.__dbname
            )
            return con
        except (Exception, pg.Error) as error:
            print('Failed to connect to PostgreSQL', error)

    def adicionar_usuario(self, usuario):
        try:
            con = self.connect()
            cur = con.cursor()

            query = """INSERT INTO usuarios (nome, email, senha, ativo, super_user) VALUES (%s, %s, %s, %s, %s)"""
            query_values = (usuario.nome, usuario.email,
                            usuario.senha, usuario.ativo, usuario.super_user)

            cur.execute(query, query_values)
            con.commit()
            print("Usuário adicionado com sucesso!")

        except (Exception, pg.Error) as error:
            print('Failed to insert record into table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")

    def atualizar_usuario(self, usuario):
        try:
            con = self.connect()
            cur = con.cursor()

            query = """UPDATE usuarios SET nome = %s, email = %s, senha = %s, super_user = %s WHERE id = %s"""
            query_values = (usuario.nome, usuario.email,
                            usuario.senha, usuario.super_user, id)

            cur.execute(query, query_values)
            con.commit()
            print("Usuário atualizado com sucesso!")

        except (Exception, pg.Error) as error:
            print('Failed to update record into table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")

    def deletar_usuario(self, usuario):
        try:
            con = self.connect()
            cur = con.cursor()

            query = """DELETE FROM usuarios WHERE id = %s"""
            query_values = (id,)

            cur.execute(query, query_values)
            con.commit()
            print("Usuário deletado com sucesso!")

        except (Exception, pg.Error) as error:
            print('Failed to delete record into table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")

    def usuarios(self):
        try:
            con = self.connect()
            cur = con.cursor()

            query = """SELECT * FROM usuarios"""

            cur.execute(query)
            con.commit()
            print("Usuários listados com sucesso!")

            return cur.fetchall()

        except (Exception, pg.Error) as error:
            print('Failed to get records from table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")

    def inativar_usuario(self, usuario):
        try:
            con = self.connect()
            cur = con.cursor()

            query = """UPDATE usuarios SET ativo = False WHERE id = %s"""
            query_values = (id,)

            cur.execute(query, query_values)
            con.commit()
            print("Usuário desativado com sucesso!")

        except (Exception, pg.Error) as error:
            print('Failed to update record into table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")

    def ativar_usuario(self, usuario):

        try:
            con = self.connect()
            cur = con.cursor()

            query = """UPDATE usuarios SET ativo = True WHERE id = %s"""
            query_values = (id,)

            cur.execute(query, query_values)
            con.commit()
            print("Usuário ativado com sucesso!")

        except (Exception, pg.Error) as error:
            print('Failed to update record into table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")

    def usuario_por_id(self, usuario):
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

        except (Exception, pg.Error) as error:
            print('Failed to get records from table', error)

        finally:
            if con:
                cur.close()
                con.close()
                print("Conexão fechada!")

    def id_usuario(self, usuario):
        try:
            con = self.connect()
            cur = con.cursor()

            query = """SELECT id FROM usuarios WHERE nome = %s, email = %s, senha = %s"""
            query_values = (usuario.nome, usuario.email, usuario.senha)

            cur.execute(query, query_values)
            con.commit()
        except (Exception, pg.Error) as error:
            print('Failed to get records from table', error)
