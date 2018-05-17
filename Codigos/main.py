import sys
import graph
# import sklearn


def main(argv):
    file = open(argv[1], 'r')
    header = {}
    for i in range(5):
        content = file.readline().strip('\n').split(': ')
        header[content[0]] = content[1]
    file.readline()
    tsp = graph.Graph()
    for i in range(int(header['DIMENSION'])):
        line = file.readline()
        line = line.strip('\n')
        content = line.split(' ')
        name = content[0]
        value = content[1] + ' ' + content[2]
        tsp.add_vertex(name, value)

    for origem in range(1, int(header['DIMENSION']) + 1):
        for destino in range(1, int(header['DIMENSION']) + 1):
            if origem != destino:
                vertex_origem = tsp.get_vertex(str(origem))
                vertex_destino = tsp.get_vertex(str(destino))
                tsp.add_edge(vertex_origem, vertex_destino,
                            #  value=sklearn.metrics.pairwise.paired_distances(
                            #      vertex_origem.get_value().split(' '),
                            #      vertex_destino.get_value().split(' '),
                            #      metric='euclidian')
                                 )
        tsp.print_adjacent_list()



if __name__ == "__main__":
   main(sys.argv)
