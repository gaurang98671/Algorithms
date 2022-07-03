class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[0 for y in range(n)] for x in range(n)]
        print(self.graph)

    def addEdge(self, i, j):
        self.graph[i-1][j-1] = 1

    def getGraph(self):
        return self.graph

    
    def dfs(self, node, visited):
        
        for i in range(self.n):
            
            if (node, i) not in visited and self.graph[node][i] == 1:
                visited.add((node, i))
                print("Visited : ", node, i )
                print("DFS for", i)
                self.dfs(i, visited)




if __name__ == "__main__":
    g = Graph(5)

    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(3, 5)


    print()
    for i in g.getGraph():
        print(i)

    g.dfs(0, set())

    


