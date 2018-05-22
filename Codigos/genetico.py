import random
import copy


def gerar_populacao(tam, dimensao):
    populacao = []
    for i in range(tam):
        populacao.append(random.sample(range(1, dimensao+1), dimensao))
    return populacao


def fitness(vet, matriz_distancias):
    soma = 0
    for i in range(0, len(vet)-1):
        soma += matriz_distancias[vet[i]][vet[i+1]]
    return soma + matriz_distancias[vet[0]][vet[-1]]


def acumular(v):
    res = []
    acum = 0
    for i in v:
        res.append(i + acum)
        acum = res[-1]
    return res


def random_select(pop, f, matriz):
    fit = []
    for p in pop:
        fit.append(1/f(p, matriz))
    soma = sum(fit)
    norm = map(lambda x: x/soma, fit)

    acm = acumular(norm)
    r = random.random()  # retorna um numero entre 0 e 1

    for i in range(len(acm)):
        if r < acm[i]:  # verifica em qual intervalo o numero aleatorio esta
            return pop[i]


def crossover(p1, p2):
    # cria um filho
    filho = copy.copy(p1)

    # inicia p com um uma quantidade aleatoria de numeros aleatorios e ordena
    p = random.sample(range(0, len(p1)), random.randint(1, len(p1)-1))
    p.sort()

    s = []

    # para cada elemento de p.. inserir em s o elemento correspondente em p1
    for i in p:
        s.append(p1[i])

    p_ord = []

    # para cada elemento de p2.. se este aparece em s.. entao seu index em s eh inserido ao final de p_ord
    for i in p2:
        if i in s:
            p_ord.append(s.index(i))

    for i in range(len(s)):
        filho[p[i]] = s[p_ord[i]]

    return filho


def crossover_alternativo(p1, p2):
    # cria um filho
    filho = copy.copy(p1)

    corte = random.randrange(1, len(p1))

    for i in range(corte, len(p1)):
        if (p2[i] not in filho[0:i]):
            filho[filho.index(p2[i])] = filho[i]
            filho[i] = p2[i]
    return filho


def mutacao(x):

    rand = random.random()
    if rand >= 0.5:
        # mutacao 1
        index = random.sample(range(0, len(x)), 2)
        aux = x[index[0]]
        x[index[0]] = x[index[1]]
        x[index[1]] = aux
    else:
        #mutacao 2
        index = random.randrange(0,len(x))
        aux = index     #index do vet a ser trocado
        if x[index] %2 == 0:
            while x[aux%len(x)] %2 != 0:
                aux+=1
            aux2 = x[aux]
            x[aux] = x[index]
            x[index] = aux2
        else:
            while x[aux%len(x)] %2 == 0:
                aux+=1
            aux2 = x[aux]
            x[aux] = x[index]
            x[index] = aux2
    return x




def genetico(pop_inicial, f, n_iter, tx_mutacao, matriz, crossover_alternativo=False, elitismo=False):
    pop = pop_inicial
    fit = map((lambda x: f(x, matriz)), pop)

    fit_melhor_caminho = min(fit)

    melhor_caminho = pop[fit.index(fit_melhor_caminho)]

    n = 0
    for gen in range(n_iter):
        p_nova = []
        for i in range(len(pop_inicial)):
            n += 1
            print(n)
            x = random_select(pop, f, matriz)
            y = random_select(pop, f, matriz)

            if crossover_alternativo:
                novo = crossover_alternativo(x, y)
            else:
                novo = crossover(x, y)

            r = random.randrange(0, 100)
            if r < tx_mutacao:
                mutacao(novo)
            p_nova.append(novo)

        if elitismo:

            pop_sort = copy.copy(fit)
            pop_sort.sort(reverse=True)

            filhos = []
            for i in p_nova:
                filhos.append(f(i, matriz))

            for pai in pop_sort:
                menor = float('inf')
                for filho in filhos:
                    if pai > filho:
                        if (p_nova[filhos.index(filho)] not in pop):
                            if filho < menor:
                                menor = filho
                if menor != float('inf'):
                    pop[fit.index(pai)] = p_nova[filhos.index(menor)]
        else:
            pop = p_nova
        fit = map((lambda x: f(x, matriz)), pop)

        if min(fit) < fit_melhor_caminho:
            fit_melhor_caminho = min(fit)
            melhor_caminho = pop[fit.index(fit_melhor_caminho)]

    return fit_melhor_caminho, melhor_caminho


if __name__ == '__main__':
    print(mutacao([1, 3, 5, 8, 2, 9, 6, 7, 4, 10]))
