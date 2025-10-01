''' Essa função será usada para definir permições por grupo de usuarios em t0do nosso projeto.'''

def usuario_esta_no_grupo(usuario, nome_grupo):
    return usuario.groups.filter(name=nome_grupo).exists()
