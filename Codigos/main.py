import sys
import utils
import genetico


def main(argv):
    file = open(argv[1], 'r')
    coordenadas, header = utils.formatar_coord(file)        #formata as coordenadas numa matriz, retorna coordenadas e o cabecalho do arquivo
    matriz = utils.gerar_matriz(header, coordenadas)        #gera a matriz de distancias entre os pontos
    pop = genetico.gerar_populacao(10, int(header['DIMENSION']))
    resultados = genetico.genetico(
        pop, genetico.fitness, 100, 5, matriz, elitismo=True)
    for resultado in resultados:
        print(resultado)


if __name__ == "__main__":
    main(sys.argv)
