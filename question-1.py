import networkx as nx
import matplotlib.pyplot as plt

def build_networkxGraph(roads):
    netGraph = nx.DiGraph()
    for city,neighbors in roads.items():
        for neigbor,distance in neighbors:
            netGraph.add_edge(city,neigbor,weight=distance)
    return netGraph
def visualize_graph(graph):
    edge_labels = nx.get_edge_attributes(graph,'weight')
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red', font_size=8)
    plt.title("Travel Ethiopia")
    plt.show()

def main(graph):
    netGraph = build_networkxGraph(graph)
    visualize_graph(netGraph)

if __name__ == '__main__':
    cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
    roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
    }
    main(roads)


