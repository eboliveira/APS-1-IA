import math

def distancia_euclidiana(x, y):
    return math.sqrt((x[1] - x[0])**2 + (y[1] - y[0])**2)

def formatar_coord(file):
    header = {}
    for i in range(5):
        content = file.readline().strip('\n').split(': ')
        header[content[0]] = content[1]
    file.readline()
    coordenadas = [0 for i in range(0, int(header['DIMENSION']) + 1)]

    for i in range(int(header['DIMENSION'])):
        line = file.readline()
        line = line.strip('\n')
        content = line.split(' ')
        id = content[0]
        coordenadas[int(id)] = content[1] + ' ' + content[2]

    return coordenadas, header

def gerar_matriz(header, coordenadas):
    matriz = [[0 for i in range(0, int(header['DIMENSION']) + 1)]
              for i in range(0, int(header['DIMENSION']) + 1)]
    for origem in range(1, int(header['DIMENSION']) + 1):
        for destino in range(1, int(header['DIMENSION']) + 1):
            if origem != destino:
                origem_cordenates = coordenadas[origem].split(' ')
                destino_cordenates = coordenadas[destino].split(' ')
                x = [float(origem_cordenates[0]), float(destino_cordenates[0])]
                y = [float(origem_cordenates[1]), float(destino_cordenates[1])]
                matriz[origem][destino] = distancia_euclidiana(x, y)
    return matriz