#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""

from queue import Queue


class Vertex(object):

    def __init__(self, data):
        """Initialize a vertex and its neighbors.
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.data = data
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""

        self.neighbors[vertex] = weight

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f'{self.data} adjacent to {[x.data for x in self.neighbors]}'

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return self.neighbors.keys()

    def get_id(self):
        """Return the data of this vertex."""
        return self.data

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # vertex to the given vertex.
        return self.neighbors[vertex] if vertex in self.neighbors else None


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""

# NOTE: id is the key and vertecies are the values


class Graph:
    def __init__(self, directed=False):
        """Initialize a graph object with an empty dictionary."""
        self.vert_dict = {}
        self.edge_list = []  # unique edge_list
        self.num_vertices = 0
        self.num_edges = 0
        self.DEFAULT_WEIGHT = 0
        self.directed = directed

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax:
        for v in g"""
        return iter(self.vert_dict.values())

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return
        the vertex."""

        if key in self.vert_dict:
            print(f'Vertex {key} already exists')
            return

        # create a new vertex
        new_vertex = Vertex(key)
        self.vert_dict[key] = new_vertex
        self.num_vertices += 1

        return new_vertex

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        # return the vertex if it is in the graph
        if key in self.vert_dict.keys():
            return key
        return None

    def get_neighbors_of(self, vertex):
        """Grabs all the neighbors of the current vertex
        Args:
            vertex (str): a given vertex
        Returns:
            vertex (Vertex): Vertex object if found
        """
        if vertex in self.vert_dict:
            return self.vert_dict[vertex]
        raise KeyError("The vertex not found in the Graph!")

    def add_edge(self, from_vertex, to_vertex, weight=None):

        if from_vertex == to_vertex:
            print(f'You cant add the vertex to itself!')
            return

        if from_vertex not in self.vert_dict or to_vertex not in self.vert_dict:
            raise ValueError("One of the vertex doesn't exist!")

        # assigning the weight
        if weight is None:
            weight = self.DEFAULT_WEIGHT
        else:
            weight = int(weight)

        edge = (from_vertex, to_vertex, weight)
        # handling duplicated edges in input file
        if edge in self.get_edges():
            raise ValueError("You can't add duplicated edges!")

        from_vert_obj = self.vert_dict[from_vertex]
        to_vert_obj = self.vert_dict[to_vertex]

        if self.directed:  # directed graph
            from_vert_obj.add_neighbor(to_vert_obj, weight)
        else:
            # connect the edges in both ways
            from_vert_obj.add_neighbor(to_vert_obj, weight)
            to_vert_obj.add_neighbor(from_vert_obj, weight)

        # add edges to unique edge_list

        self.edge_list.append(edge)

    def get_vertices(self):
        """Return all the vertices in the graph"""
        return list(self.vert_dict.keys())

    def get_edges(self):
        """Return number of all edges in the graph"""
        edges = []
        for v in self.vert_dict.values():
            for w in v.neighbors:
                edges.append((v.data, w.data, v.get_edge_weight(w)))
        return edges

    def find_shortest_path(self, from_vertex, to_vertex):
        """Search for the shortest path from vertex a to b using Breadth first search
        Args:
            from_vertex (str) : starting point on the graph
            to_vertex (str) : the distanation or end of the path
        Returns:
            shortest path (tuple): List of vertices in the path and len
                                    Empty list if path does not exist
        """

        if from_vertex not in self.vert_dict or to_vertex not in self.vert_dict:
            raise KeyError(
                "One of the given vertices does not exist in graph!")

        # check if you are at the location
        if from_vertex == to_vertex:
            vert_obj = self.vert_dict[from_vertex]
            return ([vert_obj.data], 0)

        # grab the start location from graph
        current_vertex = self.vert_dict[from_vertex]

        # initialize the queue, visited nodes set, a dictionary
        # to keep track of parent
        queue = Queue(maxsize=len(self.get_vertices()))
        seen_vertex = set()
        parent_pointers = {}

        # start the traversal
        queue.put(current_vertex)
        seen_vertex.add(current_vertex.data)

        path = []
        path_found = False
        parent = None
        current_vertex.parent = parent
        # alternative way of storing the references to parent  pointers
        parent_pointers[current_vertex.data] = None

        while not queue.empty():
            # dequeue the front element
            current_vertex = queue.get()
            path.append(current_vertex)

            # check if we are at destination
            if current_vertex.data == to_vertex:
                path_found = True  # found the goal
                break

            # otherwise
            for neighbor in current_vertex.neighbors:

                if neighbor.data not in seen_vertex:
                    queue.put(neighbor)
                    seen_vertex.add(neighbor.data)
                    neighbor.parent = current_vertex
                    parent_pointers[neighbor.data] = current_vertex.data

        if path_found:
            path = []

            while current_vertex is not None:
                path.append(current_vertex.data)
                current_vertex = current_vertex.parent

            return (path[::-1], len(path) - 1)
        # if there is no path from source to destination return -1
        return ([], -1)

    def dfs_recursive(self, from_vertex, visited=None, order=None):
        """Traverse the graph and get all vertices using DFS algorithm
        """

        if from_vertex not in self.vert_dict:
            raise KeyError(
                "One of the given vertices does not exist in graph!")

        current_vertex = self.vert_dict[from_vertex]
        # check if its first iteration
        if visited is None and order is None:
            visited = set()
            order = []

        visited.add(current_vertex.data)
        order.append(current_vertex.data)

        for neigbor in current_vertex.neighbors:
            if neigbor.data not in visited:
                self.dfs_recursive(neigbor.data, visited, order=order)

        # print(order)
        return order

    def dfs_paths(self, from_vertex, to_vertex, visited=None):
        """Find a path between two vertices using Depth First Search
        (It is just a path not necessarily the shortest path.)
        """
        if from_vertex not in self.vert_dict or to_vertex not in self.vert_dict:
            raise KeyError(
                "One of the given vertices does not exist in graph!")

        # check if you are at the location
        if from_vertex == to_vertex:
            return [from_vertex]
        if visited is None:
            visited = set()
        current_vertex = self.vert_dict[from_vertex]
        visited.add(current_vertex.data)

        for neighbor in current_vertex.neighbors:

            if neighbor.data not in visited:
                path = self.dfs_paths(neighbor.data, to_vertex, visited)
                # print("after path updated")
                if path:
                    path.append(current_vertex.data)
                    return path

        return []


    def find_maximal_clique(self, vertex):
        """Return a maximal clique of a given vertex."""

        # Raise TypeError when graph is directed
        if self.directed == True:
            raise TypeError("directed graphs cannot have cliques")

        # Clique: set of vertices
        clique = set([vertex])

        for neighbor in neighbors:

            # Track clique vertecies that are adjacent to their neighbors
            clique_counter = 0

            # Confirm vertex adjacency
            for clique_vertex in clique:
                # neighbor not adjacent
                if neighbor not in clique_vertex.get_neighbors():
                    # Move to next neighbor
                    break

                # Vertex is adjacent
                clique_counter += 1

                # If all clique verticies are adjacent to the current neighor,
                # then add that neighbor to the clique
                if clique_counter == len(clique):
                    clique.add(neighor)
                    break

        # After all neighors checked, return the clique
        return clique

    def is_eulerian(self):

        # check if the there is vertices
        if self.directed == True:
            raise TypeError("Can not be called on directed graph")

        # Check all vertices in self for their degree
        for vertex in self.vert_dict.values():
            # If a vertex has an odd degree, the graph is not Eulerian
            if len(vertex.get_neighbors()) % 2 == 1:
                return False

        # If all vertices have an even degree, the graph is Eulerian
        return True


    def highest_degree(self):
        """ Find the vertex with the highest degree in the Graph - The greatest
            number of adjacent neigbors.

            Return: Vertex object
        """

        # Tracking the vertex with highest degree
        highest_vertex_degree = 0

        # Update highest_vertex_degree with verticies in the graph's vertex dictionary
        for vertex in self.vert_dict:
            if len(vertex.neighbors) > highest_vertex_degree:
                highest_vertex_degree = vertex

        return highest_vertex_degree




def read_file(filename):
    """Read the txt file containg graph information and return them
    in a list
    Args:
        filename (txt): takes a text file to read from
    Returns:
        graph (tuple): graph object, list of vertices and list of edges
    """
    edges = []
    with open(filename, 'r') as file:
        for counter, line in enumerate(file):
            # get type of the graph
            if counter == 0:
                graph_type = line.strip()
                # create undirected graph
                if graph_type == 'G':
                    graph = Graph(directed=False)
                elif graph_type == 'D':
                    graph = Graph(directed=True)
                else:
                    raise ValueError(
                        "Graph type is not specified, type can be 'G' or 'D'!")

            # get vertices
            elif counter == 1:
                vertices = line.strip().split(',')

            # grab all the edges
            else:

                edge = line.strip('()\n').split(',')
                if len(edge) > 3 or len(edge) < 2:
                    raise Exception("Edges must contain 2 or 3 values!")
                edges.append(edge)

    return graph, vertices, edges



def build_graph(graph: Graph, vertices, edges):
    """Build a graph using given vertices and edges
    Args:
        graph (Graph): graph object
        vertices (list): list of vertices
        edges (list): list of edges containing vertices and weights
    Returns:
        graph (Graph): graph objects containing vertices and edges
    """

    # add the vertices
    for vertex in vertices:
        graph.add_vertex(vertex)

    # add the edges
    for edge in edges:
        # unpack the edge, and add
        graph.add_edge(*edge)

    return graph
