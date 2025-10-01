'''Esse arquivo e baseado na '''
from django.contrib.auth.mixins import UserPassesTestMixin
from FaustinoPizza.funcoes import usuario_esta_no_grupo


class UsuarioEAdministrador(UserPassesTestMixin):
    def test_func(self):  # aqui vamos definir como deve ser o usuario para ter acesso
        return usuario_esta_no_grupo(self.request.user, 'Administrador') or self.request.user.is_staff

