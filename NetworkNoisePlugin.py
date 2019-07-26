import networkx
import random
import math
random.seed(1234)
def connectible(G, n1, n2, positive=False):
   badred = False
   badgreen = False
   for i in G.nodes():
      # Forms a triad.  Find which edge cannot be added.
      if (i != n1 and i != n2 and
         ((i, n1) in G.edges() or (n1, i) in G.edges()) and
         ((i, n2) in G.edges() or (n2, i) in G.edges())):
            if ((i, n1) in G.edges()):
               w1 = G.adj[i][n1]['weight']
            else:
               w1 = G.adj[n1][i]['weight']
            if ((i, n2) in G.edges()):
               w2 = G.adj[i][n2]['weight']
            else:
               w2 = G.adj[n2][i]['weight']
            if (w1 < 0 and w2 < 0):
               badred = True
            elif ((w1 < 0 and w2 > 0) or (w1 > 0 and w2 < 0)):
               badgreen = True
               if (positive):
                  return False
            else:
               badred = True
   if (badred and badgreen):
      return False
   else:
      return True
 

def formsBadTriad(G, n1, n2, weight):
   badred = False
   badgreen = False
   for i in G.nodes():
      # Forms a triad.  Find which edge cannot be added.
      if (i != n1 and i != n2 and
         ((i, n1) in G.edges() or (n1, i) in G.edges()) and
         ((i, n2) in G.edges() or (n2, i) in G.edges())):
            if ((i, n1) in G.edges()):
               w1 = G.adj[i][n1]['weight']
            else:
               w1 = G.adj[n1][i]['weight']
            if ((i, n2) in G.edges()):
               w2 = G.adj[i][n2]['weight']
            else:
               w2 = G.adj[n2][i]['weight']
            if (w1 < 0 and w2 < 0):
               badred = True
            elif ((w1 < 0 and w2 > 0) or (w1 > 0 and w2 < 0)):
               badgreen = True
            else:
               badred = True
   if ((badred and weight < 0) or (badgreen and weight > 0)):
      return True
   else:
      return False

class NetworkNoisePlugin:
   def input(self, file):
      self.G = networkx.read_gml(file)

   def run(self):
      n = len(self.G.nodes())
      nodes = list(self.G.nodes())
      for i in range(0, math.floor(n/2)):
         coin = random.randint(1, 2)
         if (coin == 1):
          n1 = nodes[random.randint(0, n-1)]
          n2 = nodes[random.randint(0, n-1)]
          while ((n1, n2) in self.G.edges() or (n2, n1) in self.G.edges() or
                 not connectible(self.G, n1, n2)):
            n1 = nodes[random.randint(0, n-1)]
            n2 = nodes[random.randint(0, n-1)]
          #w = random.random() * 0.5
          w = random.random() - 0.5
          if (formsBadTriad(self.G, n1, n2, w)):
             w *= -1
          self.G.add_edge(n1, n2, weight=w)
         else:
          edge = list(self.G.edges())[random.randint(0, len(self.G.edges())-1)]
          self.G.remove_edge(edge[0], edge[1])

   def output(self, file):  
      networkx.write_gml(self.G, file)

