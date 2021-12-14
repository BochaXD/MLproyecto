def _jaccard_distance(self):
    #Distancia de Jaccard
    node_list1, node_list2 = self._get_node_lists()
    node_set1 = set(node_list1)
    node_set2 = set(node_list2)
    return 1.0 * len(node_set1 & node_set2) / len(node_set1 | node_set2)
