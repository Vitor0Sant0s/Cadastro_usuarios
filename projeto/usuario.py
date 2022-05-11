class Usuario:
    def __init__(self, nome, email, senha, super_user=False):
        self._nome = nome
        self._email = email
        self._senha = senha
        self._ativo = True
        self._super_user = self.validar_super_user(super_user)

    def validar_super_user(self, super_user):
        if super_user:
            senha_super = input("Digite a senha de super usuário: ")
            if senha_super == 'superusercreate':
                print("Usuário criado como super usuário")
                return True
            else:
                print(
                    'Acesso não permitido, as configurações de acesso estão limitadas ao usuario padrão')
                return False
        else:
            return False

    def __str__(self):
        return f'nome: {self._nome}, email: {self._email}, senha: {self._senha}, ativo: {self._ativo}, super_user: {self._super_user}'


meu_usuario = Usuario('Vitor', 'vitor@email.com', 'vitor', True)

print(meu_usuario)
