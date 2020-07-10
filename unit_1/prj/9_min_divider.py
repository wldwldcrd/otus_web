from memory_profiler import profile
from guppy import hpy
import objgraph
from graphviz import Graph

@profile
def MinDivisor(n):
    i = 2
    while (i <= int(n ** 0.5)):
        if not (n % i):
            return i
        i += 1
    h = hpy()
    print(h.heap())
    objgraph.show_refs([i], filename='sample-graph.png')
    return n


n = int(input())
print(MinDivisor(n))
