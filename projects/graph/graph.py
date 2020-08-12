"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_v in self.get_neighbors(v):
                    q.enqueue(next_v)

    def dft(self, starting_vertex):
        q = Stack()
        q.push(starting_vertex)
        visited = set()
        while q.size() > 0:
            v = q.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_v in self.get_neighbors(v):
                    q.push(next_v)

    def dft_recursive(self, starting_vertex, visited=[]):
        visited.append(starting_vertex)

        for next_v in self.vertices[starting_vertex]:
            if next_v not in visited:
                self.dft_recursive(next_v, visited)

        if visited[0] == starting_vertex:
            for item in visited:
                print(item)

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue([starting_vertex])

        visited = set()

        while q.size() > 0:
            p = q.dequeue()
            v = p[len(p)-1]

            if v not in visited:
                if v is destination_vertex:
                    print(p, 'this is the path')
                    return p
                else:
                    visited.add(v)

                    for next_v in self.get_neighbors(v):
                        c = []
                        c = [item for item in p]
                        c.append(next_v)
                        q.enqueue(c)

        return None

    def dfs(self, starting_vertex, destination_vertex):
        q = Stack()
        q.push([starting_vertex])

        visited = set()

        while q.size() > 0:
            p = q.pop()
            v = p[len(p)-1]

            if v not in visited:
                if v is destination_vertex:
                    print(p, 'this is the path')
                    return p
                else:
                    visited.add(v)

                    for next_v in self.get_neighbors(v):
                        c = []
                        c = [item for item in p]
                        c.append(next_v)
                        q.push(c)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=None):
        path += [starting_vertex]
        v = path[len(path)-1]
        if visited is None:
            visited = set()

        if v not in visited:
            if v is destination_vertex:
                if path[len(path) - 1] is destination_vertex:
                    return path
            else:
                visited.add(v)

                for next_v in self.get_neighbors(v):
                    c = []
                    c = [item for item in path]
                    temp = self.dfs_recursive(
                        next_v, destination_vertex, c, visited)
                    if temp is not None:
                        return temp


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6), "recursive")
