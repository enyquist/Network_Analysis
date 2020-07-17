from pyvis.network import Network
import networkx as nx

from utils.functions import create_k_ary_graph

k_ary_tree = create_k_ary_graph(nodes_x=5, nodes_y=5, leaves=2)

net = Network("1080px", "1080px")

net.from_nx(k_ary_tree)

net.show_buttons(filter_=['physics', 'layout'])

net.show("nx.html")

grid_graph = nx.grid_2d_graph(5, 5)

grid_average_shortest_path = nx.average_shortest_path_length(grid_graph)
