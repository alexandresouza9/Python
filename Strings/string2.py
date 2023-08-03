nome = "Alexandre"
idade = 40
profissao = "Programador"
linguagem = "Python"

print("Nome: %s idade %d" % (nome, idade))
print("Nome: {} idade {}" .format (nome, idade))
print("Nome: {1} idade {0}" .format (idade, nome))
print("Nome: {1} idade {0} nome: {1} {1}" .format (idade, nome))
print("Nome: {nome} idade {idade}" .format (nome=nome, idade=idade))