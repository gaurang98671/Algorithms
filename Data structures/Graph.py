class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start is end:
            return path

        if start not in self.graph_dict:
            return []

        paths =[]
        for node in self.graph_dict[start]:

            if node not in path:
                new_path = self.get_paths(node, end, path)

                for p in new_path:
                    paths.append(p)
        return paths


if __name__ == '__main__':

    routes = [
        ("Mumbai", "Dubai"),
        ("Mumbai", "Paris"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    route_graph = Graph(routes)

    print(route_graph.get_paths('Mumbai', 'New York'))
    print(route_graph.graph_dict)