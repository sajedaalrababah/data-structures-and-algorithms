class Graph:

    def __init__(self):
        self.graph = {}


    def add_node(self, node):
        """
        Add a node to the graph.

        Args:
            node (hashable): The node to be added to the graph.
        """
        self.graph[node] = []


    def add_edge(self, node1, node2):
        """
        Add an edge between two nodes in the graph.

        If the nodes do not exist in the graph, they will be added.

        Args:
            node1 (hashable): The first node.
            node2 (hashable): The second node.
        """
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)


    def depth_first(self, start_node):
        """
        Perform depth-first traversal starting from the given node.

        Args:
            start_node (hashable): The node to start the depth-first traversal from.

        Returns:
            list: A list containing nodes in their pre-order depth-first traversal order.
        """
        visited = set()
        result = []


        def dfs(node):
            """
            Recursive function for depth-first traversal.

            Args:
                node (hashable): The current node being visited.
            """
            visited.add(node)
            result.append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)


        dfs(start_node)
        return result