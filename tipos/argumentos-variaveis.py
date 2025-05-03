
def soma(*nums):
    print(type(nums))
    total = 0

    for n in nums:
        total = total + n
    
    return total


def resultado_final(**kwargs):
    print(type(kwargs))
    print(kwargs['nome'])
    print(kwargs['nota'])
    status = 'aprovado(a)' if kwargs['nota'] >= 6 else 'reprovado(a)'

    return f"{kwargs['nome']} foi {status}!"


print(soma(1, 2, 3, 4, 5))
print()
print(resultado_final(nome='Lucas', nota=9.1))