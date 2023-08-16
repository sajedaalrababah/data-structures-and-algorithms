import pytest 
from graph_depthFirst import Graph


@pytest.fixture
def graph():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "D")
    g.add_edge("B", "C")
    g.add_edge("B", "G")
    g.add_edge("D", "E")
    g.add_edge("D", "F")
    g.add_edge("F", "H")
    return g


def test_depth_first(graph):
    assert graph.depth_first("A") == ["A", "B", "C", "G", "D", "E", "F", "H"]
    assert graph.depth_first("B") == ["B", "A", "D", "E", "F", "H", "C", "G"]
    assert graph.depth_first("D") == ["D", "A", "B", "C", "G", "E", "F", "H"]


def test_add_node():
    g = Graph()
    g.add_node("X")
    assert "X" in g.graph


def test_add_edge():
    g = Graph()
    g.add_edge("X", "Y")
    assert "X" in g.graph
    assert "Y" in g.graph["X"]
    assert "Y" in g.graph
    assert "X" in g.graph["Y"]