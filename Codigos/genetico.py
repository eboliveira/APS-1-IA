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
    p = [3, 5, 6, 9]
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


def mutacao(x):
    i = random.randint(1, 2)
    if i == 1:
        # mutacao 1
        index = random.sample(range(0, len(x)), 2)
        aux = x[index[0]]
        x[index[0]] = x[index[1]]
        x[index[1]] = aux
    else:
        # mutacao 2
        pass

    return x

def genetico(pop_inicial, f, n_iter, tx_mutacao, matriz, elitismo=False):
    pop = pop_inicial
    fit = map((lambda x: f(x, matriz)), pop)
    
    fit_melhor_caminho = min(fit)

    melhor_caminho = pop[fit.index(fit_melhor_caminho)]


    for gen in range(n_iter):
        p_nova = []
        for i in range(len(pop_inicial)):
            x = random_select(pop, f, matriz)
            y = random_select(pop, f, matriz)
            novo = crossover(x, y)
            r = random.randrange(0, 100)
            if r < tx_mutacao:
                novo = mutacao(novo)
            p_nova.append(novo)
        pop = p_nova
        fit = map((lambda x: f(x, matriz)), pop)
        
        if min(fit) < fit_melhor_caminho:
            fit_melhor_caminho = min(fit)
            melhor_caminho = pop[fit.index(fit_melhor_caminho)]

    return fit_melhor_caminho, melhor_caminho


if __name__ == '__main__':
    print crossover([1, 3, 5, 8, 2, 9, 6, 7, 4, 10], [5, 1, 8, 2, 9, 10, 7, 3, 4, 6])
