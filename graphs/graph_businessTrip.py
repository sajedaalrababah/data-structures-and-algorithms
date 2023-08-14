from collections import defaultdict


def buildGraph(graph_edges):
    """
    Build a graph from the given graph edges.

    Args:
        graph_edges (list): List of tuples representing graph edges. Each tuple contains
            source city, destination city, and the cost of the flight.

    Returns:
        defaultdict: The built graph represented as a defaultdict of dictionaries.
            Each source city maps to a dictionary of destination cities and their corresponding costs.
    """
    graph = defaultdict(dict)
    for edge in graph_edges:
        source, destination, cost = edge
        graph[source][destination] = cost
    return graph


def businessTrip(graph, cities):
    """
    Determine whether the trip is possible with direct flights and calculate the total cost.

    Args:
        graph (defaultdict): The graph representing flights between cities.
            It is represented as a defaultdict of dictionaries.
            Each source city maps to a dictionary of destination cities and their corresponding costs.
        cities (list): List of city names representing the trip.

    Returns:
        int or None: The cost of the trip if it's possible with direct flights, or None if it's not possible.
    """
    total_cost = 0

    for i in range(len(cities) - 1):
        current_city = cities[i]
        next_city = cities[i + 1]

        if next_city in graph[current_city]:
            total_cost += graph[current_city][next_city]
        else:
            return None

    return total_cost