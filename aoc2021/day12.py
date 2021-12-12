
import itertools

puzzle_input = [line.strip().split("-")
                for line in open('aoc2021/inputs/12.txt')]


class node:
    def __init__(self, name):
        self.name = name
        self.smallCave = False if name.isupper() else True
        self.connections = []
        self.paths = []

    def addConnection(self, cave):
        self.connections.append(cave)

    def visitNeighbors(self, visited, max_num=1):
        for connection in self.connections:

            g = [list(i) for j, i in itertools.groupby(sorted(visited))]
            g = [l for l in g if not l[0].isupper()]
            lengths = list(reversed(sorted([len(l) for l in g])))
            if len(lengths) >= 2:
                only_one = True if lengths[0] <= max_num and lengths[1] == 1 else False
            else:
                only_one = False

            if connection.name == 'end':
                nv = visited.copy()
                nv.append(connection.name)
                connection.paths.append(visited)
            elif connection.smallCave and (connection.name not in visited) or (only_one and connection.name != 'start'):
                nv = visited.copy()
                nv.append(connection.name)
                connection.visitNeighbors(nv)
            elif not connection.smallCave:
                nv = visited.copy()
                nv.append(connection.name)
                connection.visitNeighbors(nv, max_num)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


# add all nodes
nodes = dict()
for connection in puzzle_input:
    nodes[connection[0]] = node(connection[0])
    nodes[connection[1]] = node(connection[1])

# add connections
for connection in puzzle_input:
    nodes[connection[0]].addConnection(nodes[connection[1]])
    nodes[connection[1]].addConnection(nodes[connection[0]])

nodes['start'].visitNeighbors(['start'],)
paths = nodes['end'].paths
print(len(paths))
