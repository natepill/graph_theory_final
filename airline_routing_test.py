import sys
from graph import Graph, Vertex, build_graph, read_file
import unittest


class VertexTest(unittest.TestCase):


    def test_dfs_found(self):
        """ Testing DFS recursive search when a path can be found"""

        graph = Graph(directed=False)

        graph.add_vertex('LA')
        graph.add_vertex('San Fran')
        graph.add_vertex('Dallas')
        graph.add_vertex('Houston')
        graph.add_vertex('E')
        graph.add_vertex('F')
        graph.add_vertex('G')

        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'A')
        graph.add_edge('C', 'D')
        graph.add_edge('D', 'E')
        graph.add_edge('E', 'F')
        graph.add_edge('F', 'D')

        from_vertex = 'A'
        to_vertex = 'D'

        path = graph.dfs_paths(from_vertex, to_vertex)

        assert len(path) == 4

    def test_dfs_not_found(self):
        """ Testing DFS recursive search when a path CANNOT be found"""

        graph = Graph(directed=False)

        # Add Verts and Edges to graph

        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_vertex('D')
        graph.add_vertex('E')
        graph.add_vertex('F')
        graph.add_vertex('G')

        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'A')
        graph.add_edge('C', 'D')
        graph.add_edge('F', 'D')

        from_vertex = 'A'
        to_vertex = 'E'

        path = graph.dfs_paths(from_vertex, to_vertex)

        # No path found, so length of path 0
        assert len(path) == 0
