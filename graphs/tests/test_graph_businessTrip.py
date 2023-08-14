import pytest
from graph_businessTrip import buildGraph, businessTrip


def test_businessTrip_DirectFlights():
    graph_edges = [
        ("Pandora", "Arendelle", 150),
        ("Pandora", "Metroville", 82),
        ("Arendelle", "Metroville", 99),
        ("Arendelle", "Monstropolis", 42),
        ("Metroville", "Monstropolis", 105),
        ("Metroville", "Narnia", 37),
        ("Metroville", "Naboo", 26),
        ("Monstropolis", "Naboo", 73),
        ("Narnia", "Naboo", 250),
    ]
    graph = buildGraph(graph_edges)
    assert businessTrip(graph, ["Pandora", "Metroville"]) == 82


def test_businessTrip_NoDirectFlights():
    graph_edges = [
        ("Pandora", "Arendelle", 150),
        ("Arendelle", "Metroville", 99),
        ("Arendelle", "Monstropolis", 42),
        ("Metroville", "Monstropolis", 105),
        ("Metroville", "Narnia", 37),
        ("Metroville", "Naboo", 26),
        ("Monstropolis", "Naboo", 73),
        ("Narnia", "Naboo", 250),
    ]
    graph = buildGraph(graph_edges)
    assert businessTrip(graph, ["Naboo", "Pandora"]) is None
    assert businessTrip(graph, ["Narnia", "Arendelle", "Naboo"]) is None


def test_businessTrip_invalidCity():
    graph_edges = [
        ("Pandora", "Arendelle", 150),
        ("Pandora", "Metroville", 82),
        ("Arendelle", "Metroville", 99),
        ("Arendelle", "Monstropolis", 42),
        ("Metroville", "Monstropolis", 105),
        ("Metroville", "Narnia", 37),
        ("Metroville", "Naboo", 26),
        ("Monstropolis", "Naboo", 73),
        ("Narnia", "Naboo", 250),
    ]
    graph = buildGraph(graph_edges)
    assert businessTrip(graph, ["Pandora", "Atlantis"]) is None


def test_businessTrip_singleCity():
    graph_edges = [
        ("Pandora", "Arendelle", 150),
        ("Pandora", "Metroville", 82),
        ("Arendelle", "Metroville", 99),
        ("Arendelle", "Monstropolis", 42),
        ("Metroville", "Monstropolis", 105),
        ("Metroville", "Narnia", 37),
        ("Metroville", "Naboo", 26),
        ("Monstropolis", "Naboo", 73),
        ("Narnia", "Naboo", 250),
    ]
    graph = buildGraph(graph_edges)
    assert businessTrip(graph, ["Pandora"]) == 0