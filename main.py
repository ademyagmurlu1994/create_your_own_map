from map import Map
if __name__ == "__main__":
    mp = Map()
    """mp.add_node("G")
    print(mp.nodes)
    #mp.add_connection("F", "G", 5)
    print(mp.connections)"""
    source_node = "G"
    target_node = "E"
    shortest_weight, shortest_path = mp.find_shortes_path(source_node=source_node, target_node=target_node)
    print("### from ", source_node, " to ", target_node, " ###")
    print("_"*30)
    print("shortest weight: ", shortest_weight)
    print("shortest path: ", shortest_path)
