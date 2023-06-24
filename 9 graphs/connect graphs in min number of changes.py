class Solution:
    def makeConnected(self, n, connections) :
        if len(connections) < n - 1: return -1

        dsu = DSU(range(n))
        for u, v in connections: dsu.union(u, v)
        return dsu.ds_count() - 1

T = Hashable
class DSU:
    def __init__(self, xs):
        self.parents = list(range(xs+1))
        self.sizes = [1]*(xs+1)
        self.count =  len(self.parents)

    def find(self, u):
        self.parents[u] = u if self.parents[u] == u else self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u, v):
        ur, vr = self.find(u), self.find(v)
        if ur == vr: return
        low, high = (ur, vr) if self.sizes[ur] < self.sizes[vr] else (vr, ur)
        self.parents[low] = high
        self.sizes[high] += self.sizes[low]
        self.count -= 1
    
    def is_connected(self, u, v):
        return self.find(u) == self.find(v)
    
    def ds_count(self):
        return self.count
