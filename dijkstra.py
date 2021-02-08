from math import inf
from copy import deepcopy
def traverse_graph(graph, start_node):
	'''
	Carries out Dijkstra's algorithm
	:param graph: Graph object
	:param start_node: Node object, the node you are starting from
	:returns: A copy of the graph, whose node objects have cost and previous fields
	'''

	#copy the graph so the function is pure
	graph = deepcopy(graph)
	#we want the node in the copy with the same name as the node from the original
	start_node = graph.get_node(start_node.name)

	unvisited = []
	visited = []
	for node in graph.nodes:
		 node.update_data("cost", inf)
		 node.update_data("previous", None)
		 unvisited.append(node)
	start_node.update_data("cost", 0)

	while len(unvisited) != 0:
		lowest_cost = min([node.get_data("cost") for node in unvisited])
		current = [node for node in unvisited if node.get_data("cost") == lowest_cost][0]
		cost_of_current = current.get_data("cost")
		unvisited.remove(current)
		visited.append(current)

		for neighbour in current.neighbours:
			if neighbour not in visited:
				new_cost = current.get_edge_weight(neighbour) + cost_of_current
				if new_cost < neighbour.get_data("cost"):
					neighbour.update_data("cost", new_cost)
					neighbour.update_data("previous", current)
	return graph

def find_shortest_path(graph, start_node, end_node):
	'''
	Finds the shortest path from a node to another node
	:param graph: A Graph object
	:param start_node: A Node object
	:param end_node: A Node object
	:returns: List of Strings, the names of the nodes that make up the shortest path, starts with start_node and ends with end_node
	'''
	graph = traverse_graph(graph, start_node)
	#traverse_graph returns a copy of the graph
	#we need the nodes in the copy with the same names as the nodes in the original
	start_node = graph.get_node(start_node.name)
	end_node = graph.get_node(end_node.name)

	route = []
	curr = end_node
	route.append(curr)

	while curr != start_node:
		curr = curr.get_data("previous")
		route.append(curr)

	return [node.name for node in reversed(route)]
