from graphfileparser import parseHighwayGraphFile
from graphshw import WeightedGraph
import sys


if __name__ == "__main__":
    file = sys.argv[1]
    g = parseHighwayGraphFile(file)

    print(g.bellmanFord(0))
    print(g.dijkstra(0))