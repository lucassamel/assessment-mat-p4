V = ['tipo 1', 'tipo 2', 'tipo 3', 'tipo 4', 'tipo 5', 'tipo 1', 'tipo 1', 'tipo 3']


def rec(dado, vetor):
    if dado in vetor:
        return


def iterativa(vetor, dado):
    j = 0
    for i in vetor:
        if i == dado:
           j += 1
    print("O dado", dado, "foi encontrado ", j, "vezes.")


if __name__ == '__main__':

    dado = input("Digite o tipo de dado que deseja verificar: ")
    iterativa(V, dado)

    rec(dado, V)
