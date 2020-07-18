import random

from pyvis.network import Network
import networkx as nx

from utils.functions import create_k_ary_graph


#######################################################################################################################
# Global Variables
#######################################################################################################################

LOWER_VALUE = 0.8
UPPER_VALUE = 0.95
X_DIM = 10
Y_DIM = 10
OFF_CHANCE = 0.3
OFF_NODE_PERCENT = 0.1
OFF_NODE_VALUE = 9999

#######################################################################################################################
# Visualization of path options
#######################################################################################################################

# k_ary_tree = create_k_ary_graph(nodes_x=5, nodes_y=5, leaves=2)
#
# net = Network("900px", "900px")
#
# net.from_nx(k_ary_tree)
#
# net.show_buttons(filter_=['physics', 'layout'])
#
# net.show("nx.html")

#######################################################################################################################
# Create graph and apply weights, some nodes are turned "off" by setting the weight to some unreasonable number
#######################################################################################################################

grid_graph = nx.grid_2d_graph(X_DIM, Y_DIM)

total_off_nodes = round(len(grid_graph.edges) * OFF_NODE_PERCENT)

sampling = random.sample(grid_graph.edges, k=total_off_nodes)

for node_1, node_2 in grid_graph.edges:
    if (node_1, node_2) in sampling:
        grid_graph[node_1][node_2]['weight'] = OFF_NODE_VALUE
    else:
        grid_graph[node_1][node_2]['weight'] = random.uniform(LOWER_VALUE, UPPER_VALUE)

#######################################################################################################################
# Visualization of grid_graph
#######################################################################################################################

net = Network("900px", "900px")

net.from_nx(grid_graph)

net.show_buttons(filter_=['physics', 'layout'])

net.show("nx_gg.html")

#######################################################################################################################
# Average Shortest Path in Network, rounded to nearest Int
#######################################################################################################################

grid_average_shortest_path = nx.average_shortest_path_length(grid_graph, weight='weight')

# grid_average_shortest_path = nx.average_shortest_path_length(grid_graph)

#######################################################################################################################
# Path Finding
#######################################################################################################################

# shortest_path = nx.algorithms.shortest_paths.weighted.dijkstra_path(grid_graph, 0, 10)
