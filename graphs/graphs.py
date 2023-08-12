class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        """
        Adds a new vertex to the graph.

        Args:
            value: The value of the vertex to be added.

        Returns:
            The value of the added vertex.

        """
        if value not in self.vertices:
            self.vertices[value] = []
        return value

    def add_edge(self, vertex1, vertex2, weight=None):
        """
        Adds an undirected edge between two vertices in the graph.

        Args:
            vertex1: The first vertex.
            vertex2: The second vertex.
            weight (optional): The weight of the edge. Default is None.

        Raises:
            ValueError: If either of the vertices is not present in the graph.

        """
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append((vertex2, weight))
            self.vertices[vertex2].append((vertex1, weight))
        else:
            raise ValueError("Both vertices should already be in the graph.")

    def get_vertices(self):
        """
        Returns a list of all vertices in the graph.

        Returns:
            A list of vertices.

        """
        return list(self.vertices.keys())

    def get_neighbors(self, vertex):
        """
        Returns a list of neighboring vertices for a given vertex.

        Args:
            vertex: The vertex for which to retrieve the neighbors.

        Returns:
            A list of neighboring vertices and their weights.

        """
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return []

    def size(self):
        """
        Returns the number of vertices in the graph.

        Returns:
            The number of vertices.

        """
        return len(self.vertices)