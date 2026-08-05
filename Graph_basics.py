"""
#creating graph undirectional adjacent list
class Graph:
    def __init__(self,vertices):
        self.graph = {}
    def insert(self,u,v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

obj = Graph(vertices =0)
obj.insert("R","K")
obj.insert("R","p")
obj.insert("K","S")
obj.insert("S","P")
print(obj.graph)





#creating graph using adjacent matrix
class Graph:
    def __init__(self,size):
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        self.dic ={ "K" : 0,"S" : 1,"P" :2 ,"R" :3 }
        self.size = size
    def insert(self,u,v):
        u_index = self.dic[u]
        v_index = self.dic[v]
        self.graph[u_index][v_index] = 1
        self.graph[v_index][u_index] = 1
    def display(self):
        for row in self.graph:
            print(row)
g = Graph(4)
g.insert("K", "R")
g.insert("R", "P")
g.insert("P", "S")
g.display()

 """                           
    
        




"""

#creating graph undirectional adjacent list
class Graph:
    def __init__(self,vertices):
        self.graph = {}
    def insert(self,u,v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

obj = Graph(vertices =0)
obj.insert("0","1")
obj.insert("0","3")
obj.insert("1","2")
obj.insert("2","7")
obj.insert("2","8")
obj.insert("3","4")
obj.insert("3","5")
obj.insert("4","5")
obj.insert("5","6")
obj.insert("8","9")
print(obj.graph)
"""






"""
#bfs using adjacent list
def bfs(graph,start):
    visited = []
    queue = [start]
    while queue:
        cur = queue.pop(0)
        if cur not in visited:
            visited.append(cur)
            queue.extend(graph[cur])
    print(visited)
graph ={ "A" : ["B" , "P"],
  "B" : ["A","C","K"],
  "P" : ["A","G"],
  "C" : ["B","T"],
  "K" : ["B","T"],
  "G" : ["P"],
  "T" : ["C","K"]}
bfs(graph,"A")
"""









"""

#dfs using adjacent list
def dfs(graph,start):
    visited = []
    queue = [start]
    while queue:
        cur = queue.pop()
        if cur not in visited:
            visited.append(cur)
            queue.extend(graph[cur])
    print(visited)
    

graph ={ "A" : ["B" , "P"],
  "B" : ["A","C","K"],
  "P" : ["A","G"],
  "C" : ["B","T"],
  "K" : ["B","T"],
  "G" : ["P"],
  "T" : ["C","K"]}
dfs(graph,"A")
"""



"""
#bfs using adjacent matrix

def bfs(graph,start):
    visited = []
    queue = [start]
    dic = {"A" :0,"B":1,"C":2,"D":3}
    while queue:
        cur = queue.pop(0)
        if cur not in visited:
            visited.append(cur)
            cur_index = dic[cur]
            for v,i in dic.items():
                if graph[cur_index] == 1:
                    queue.append(v)
    print(visited)
graph = [[0,1,1,0],
         [1,0,0,1],
         [1,0,0,0],
         [0,1,0,0]]
bfs(graph,"A")
"""




#connected components
def connected_components(graph):
    visited = []
    count = 0 
    def bfs(start):           
        queue = [start]
        while queue:
            cur = queue.pop(0)
            if cur not in visited:
                visited.append(cur)
                queue.extend(graph[cur])
    for key in graph:
        if key not in visited:         
            bfs(key)
            count += 1
    return count
graph = { "A":["B","C"],
          "B":["A"],
          "C":["A"],
          "D":[],
          "E":["F"],
          "F":["E"],
          }
print(connected_components(graph))
          



































