
class Node:
    def __init__(self,tag=None):
        self.tag = tag 
        self.adj = []  
        self.color = 0 
    def neighbor_to_str(self):
        s = "" 
        for n in self.adj: 
            s= s + f"->{n.tag}"  
        return s
    def add_neighbor(self,node):
        self.adj.append(node) 

class Edge:
    def __init__(self,from_=None,to_=None,weight=None,active=True):
        self.from_ = from_ 
        self.to_ = to_ 
        self.weight = weight  
        self.active = active 
    
    def to_str(self):
        if self.weight is not None:
            return f"{'{'}{self.from_.tag},{self.to_.tag},{self.weight}{'}'}" 
        else:
            return f"{'{'}{self.from_.tag},{self.to_.tag}{'}'}" 

    
class Graph:

    def __init__(self,oriented=True):
        self.V = {} 
        self.E = {} 
        self.oriented = oriented 
       

    def print_me(self):
        for n in self.V: 
            node = self.V[n] 
            str_=''
            print(f"{node.tag} {node.neighbor_to_str()}") 
        for e in self.E: 
            print(self.E[e].to_str()) 

    def add_node(self,tag): 
        if tag in self.V: return
        node = Node(tag)
        self.V[tag] = node 
    
    def get_node(self,tag): 
        if tag not in self.V: 
            self.add_node(tag) 
        return self.V[tag] 

    def add_edge(self,tag_from,tag_to,weight= None):

        frm = self.get_node(tag_from)
        to = self.get_node(tag_to)

        frm.add_neighbor(to) 
        if not self.oriented: 
             to.add_neighbor(frm) 
        if weight is not None: 
            edge = Edge(frm, to, weight)
        else: 
            edge = Edge(frm, to)

        k1 = frm.tag+10000*to.tag 
        self.E[k1] = edge 

graph = Graph()

graph.add_node("0")
graph.add_node("1")
graph.add_node("2")
graph.add_node("3")
graph.add_node("4")

graph.add_edge("0", "3")
graph.add_edge("0", "2")
graph.add_edge("1", "3")
graph.add_edge("4", "1")
graph.add_edge("2", "4")


