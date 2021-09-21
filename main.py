V = ['tipo 1', 'tipo 2', 'tipo 3', 'tipo 4', 'tipo 5', 'tipo 1', 'tipo 1', 'tipo 3']


def rec(dado, vetor, i, j):
    if i >= (len(vetor)):
        return print("O dado", dado, "foi encontrado ", j, "vezes.")
    elif vetor[i] == dado:
        return rec(dado, vetor, i + 1, j + 1)
    return rec(dado, vetor, i + 1, j)


def iterativa(vetor, dado):
    j = 0
    for i in vetor:
        if i == dado:
            j += 1
    print("O dado", dado, "foi encontrado ", j, "vezes.")


if __name__ == '__main__':
    # dado = input("Digite o tipo de dado que deseja verificar: ")
    dado = "tipo 1"
    rec(dado, V, 0, 0)

    iterativa(V, dado)



