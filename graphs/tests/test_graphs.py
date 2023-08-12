import pytest 
from graphs import Graph


def test_add_vertex():
    graph = Graph()
    vertex = graph.add_vertex("A")
    assert vertex == "A"
    assert "A" in graph.get_vertices()


def test_add_edge():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B", weight=5)
    neighbors = graph.get_neighbors("A")
    assert ("B", 5) in neighbors
    neighbors = graph.get_neighbors("B")
    assert ("A", 5) in neighbors


def test_get_vertices():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    vertices = graph.get_vertices()
    assert "A" in vertices
    assert "B" in vertices


def test_get_neighbors():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B", weight=5)
    graph.add_edge("A", "C", weight=10)
    neighbors = graph.get_neighbors("A")
    assert ("B", 5) in neighbors
    assert ("C", 10) in neighbors


def test_size():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    assert graph.size() == 3


def test_single_vertex_edge():
    graph = Graph()
    vertex = graph.add_vertex("A")
    graph.add_edge("A", "A", weight=2)
    assert "A" in graph.get_vertices()
    neighbors = graph.get_neighbors("A")
    assert ("A", 2) in neighbors
    assert graph.size() ==1