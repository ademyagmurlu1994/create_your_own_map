import sys
import pickle

class Map:
    def __init__(self):
        self.nodes = []
        self.connections = dict()
        self.get_nodes()  # load nodes
        self.get_route_conn()  # load connection

    def get_route_conn(self, path="route_conn.pkl"):
        file = open(path, "rb")
        self.connections = pickle.load(file)

    def save_route_conn(self, path="route_conn.pkl"):
        file = open(path, "wb")
        pickle.dump(self.connections, file)

    def get_nodes(self, path="nodes.pkl"):
        file = open(path, "rb")
        self.nodes = pickle.load(file)

    def save_nodes(self, path="nodes.pkl"):
        file = open(path, "wb")
        pickle.dump(self.nodes, file)

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes += node

        self.save_nodes()

    def add_connection(self, node_1, node_2, weight):
        if node_1 in self.nodes and node_2 in self.nodes:
            self.connections[(self.nodes.index(node_1), self.nodes.index(node_2))] = weight
        else:
            print(node_1, " or ", node_2 , "is not exist!\n Please add node or nodes")

        self.save_route_conn()

    def str_path(self, path):
        conn = ""
        for index in path:
            conn += self.nodes[index]
            conn += " --> "

        return conn[0: len(conn) - 5] # delete "-->" in end

    def find_shortes_path(self, source_node, target_node):
        if source_node in self.nodes and target_node in self.nodes:
            source_node = (self.nodes.index(source_node))
            target_node = (self.nodes.index(target_node))

            distance = [sys.maxsize] * len(self.nodes)  # set like infinity(max int) distance
            distance[source_node] = 0

            paths = {node: [] for node in range(len(self.nodes))}
            paths[source_node] = []
            for _ in range(len(self.nodes) - 1):
                for (current_node, next_node), w_edge in self.connections.items():  # visited: current_node, unvisited: next_node
                    if distance[next_node] > distance[current_node] + w_edge:
                        distance[next_node] = distance[current_node] + w_edge
                        paths[next_node] = paths[current_node] + [current_node]

                    if distance[current_node] > distance[next_node] + w_edge:
                        distance[current_node] = distance[next_node] + w_edge
                        paths[current_node] = paths[next_node] + [next_node]

            path = self.str_path(paths[target_node] + [target_node])

            return distance[target_node], path

        else:
            print(source_node, " or ", target_node, "is not exist")



