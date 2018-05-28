import sys
import utils
import genetico


def main(argv):
    file = open(argv[1], 'r')
    # formata as coordenadas numa matriz, retorna coordenadas e
    # o cabecalho do arquivo
    coordenadas, header = utils.formatar_coord(file)

    # gera a matriz de distancias entre os pontos
    matriz = utils.gerar_matriz(header, coordenadas)

    # gera uma populacao inicial
    pop = genetico.gerar_populacao(200, int(header['DIMENSION']))

    resultados = genetico.genetico(
        pop, genetico.fitness, 15, 5, matriz, elitismo=False, use_crossover_alternativo=True, id_mutacao=2)
    print(header['NAME'])
    for resultado in resultados:
        print(resultado)


if __name__ == "__main__":
    main(sys.argv)
