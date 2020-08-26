class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices: # check if vertex exists
            self.vertices[vertex_id] = set() # add vertex

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v2 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) # add v1 neighbor -> v2
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the stack is not empty
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            last_vert = path[-1]
            # If that vertex has not been visited
            if last_vert not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                else:
                    # Mark as visited
                    visited.add(last_vert)
                    # Then add A PATH TO its neighbors to the back of the stack
                    for edge in self.get_neighbors(last_vert):
                        # COPY THE PATH
                        path_copy = list(path)
                        # APPEND THE NEIGHOR TO THE BACK
                        path_copy.append(edge)
                        s.push(path_copy)

def earliest_ancestor(ancestors, starting_node):
    # build list of vertices- removing dupes
    verts = list(set([i for j in ancestors for i in j]))

    # build a graph
    g = Graph()
    
    # iterate through ancestors
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        g.add_vertex(parent)
        g.add_vertex(child)
        g.add_edge(child, parent)

    # set lists for paths
    paths = []
    # traverse verts
    for vertex in verts:
        # if not at starting node and a path exists
        if vertex != starting_node and g.dfs(starting_node, vertex):
            # add path
            paths.append(g.dfs(starting_node, vertex))
    if len(paths) < 1: # no paths found
        return -1
    else:
        # otherwise, sort all the paths and return the last ancestor in path
        return max(paths, key=len)[-1]