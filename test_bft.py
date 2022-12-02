import pytest
import main as m


@pytest.fixture
def my_root():
    return m.Node('A')


@pytest.fixture
def my_nodes(my_root):

    my_nodes = [my_root]

    for letter in 'ABCDEFGH':
        my_nodes.append(m.Node(letter))

    return my_nodes


@pytest.fixture
def my_edges(my_nodes):
    A, B, C, D = my_nodes[:4]

    return m.Edge(A, B), m.Edge(A, C), m.Edge(C, B), m.Edge(D, B)


@pytest.fixture
def my_edges(my_nodes):
    A, B, C, D, E = my_nodes[:5]

    return m.Edge(A, B), m.Edge(A, C), m.Edge(B, E), m.Edge(C, D)


@pytest.fixture
def my_trace(my_nodes):
    A, B, C, D, E = my_nodes[:5]
    return [A, B, C, E, D]


def test_bft(my_root, my_nodes, my_edges, my_trace):
    my_graph = m.Graph.from_edge_list(my_edges)

    my_bft = m.BreadthFirstTraversal(my_graph, my_root)

    my_bft.run_to_end()

    assert my_bft.visited == my_trace
