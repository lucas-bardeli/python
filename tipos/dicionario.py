
aluno = {
    'nome': 'Lucas',
    'nota': 9.1,
    'ativo': True
}

print(type(aluno))
print(aluno['nome'])
print(aluno['nota'])
print(aluno['ativo'])
print(len(aluno))

for chave in aluno:
    print(chave, '--->', aluno[chave])

for chave, valor in aluno.items():
    print(chave, '--->', valor)

for valor in aluno.values():
    print(valor, end=', ')

for chave in aluno.keys():
    print(chave, end=', ')