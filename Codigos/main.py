import sys
import utils
import genetico


def main(argv):
    file = open(argv[1], 'r')
    header = {}
    for i in range(5):
        content = file.readline().strip('\n').split(': ')
        header[content[0]] = content[1]
    file.readline()
    matriz = [[0 for i in range(0, int(header['DIMENSION']) + 1)] for i in range(0, int(header['DIMENSION']) + 1)]
    coordenadas = [0 for i in range(0, int(header['DIMENSION']) + 1)]

    for i in range(int(header['DIMENSION'])):
        line = file.readline()
        line = line.strip('\n')
        content = line.split(' ')
        id = content[0]
        coordenadas[int(id)] = content[1] + ' ' + content[2]

    
    for origem in range(1, int(header['DIMENSION']) + 1):
        for destino in range(1, int(header['DIMENSION']) + 1):
            if origem != destino:
                origem_cordenates = coordenadas[origem].split(' ')
                destino_cordenates = coordenadas[destino].split(' ')
                x = [float(origem_cordenates[0]), float(destino_cordenates[0])]
                y = [float(origem_cordenates[1]), float(destino_cordenates[1])]
                matriz[origem][destino] = utils.distancia_euclidiana(x, y)
    
    pop = genetico.gerar_populacao(100, int(header['DIMENSION']))
    genetico.random_select(pop, genetico.fitness, matriz)
    resultados = genetico.genetico(pop, genetico.fitness, 10000, 5, matriz)
    for resultado in resultados:
        print resultado


if __name__ == "__main__":
   main(sys.argv)
