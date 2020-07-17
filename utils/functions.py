import networkx as nx


def create_k_ary_graph(nodes_x, nodes_y, leaves):
    """
    Create a k-ary graph that reflects the problem space to traverse the grid network with nodes_x and nodes_y
    :param nodes_x:
    :param nodes_y:
    :param leaves:
    :return:
    """

    grid = nx.grid_2d_graph(nodes_x, nodes_y)

    diameter_grid = nx.diameter(grid)

    total_nodes = full_k_ary_graph(diameter_grid, leaves)

    k_ary = nx.full_rary_tree(r=leaves, n=total_nodes, create_using=nx.DiGraph)

    return k_ary


def full_k_ary_graph(diameter, leaves):
    if diameter == 0:
        return leaves ** diameter  # 1
    if diameter == 1:
        return leaves + 1
    else:
        return leaves**diameter + full_k_ary_graph(diameter - 1, leaves)
