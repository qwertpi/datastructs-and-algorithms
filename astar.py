from math import inf
from copy import deepcopy
from functools import partial

def manhattan_dist(start_node, node):
	'''
	An example heuristic function. All heuristics must take these paramaters in this order
	Calculates the manhattan distance between the start node and another node
	:param start_node: Node object
	:param node: Node object
	:returns: Int or Float
	'''
	return abs(start_node.get_data("coord")[0] - node.get_data("coord")[0]) + abs(start_node.get_data("coord")[1] - node.get_data("coord")[1])

def traverse_graph(graph, start_node, end_node, heuristic):
	'''
	Carries out Dijkstra's algorithm
	:param graph: Graph object
	:param start_node: Node object, the node you are starting from
	:param end_node: Node object, the node you want to end up at
	:param heuristic: a function of the form f(start_node, node)
	:returns: A copy of the graph, whose node objects have cost and previous fields
	'''

	#copy the graph so the function is pure
	graph = deepcopy(graph)
	#we want the node in the copy with the same name as the node from the original
	start_node = graph.get_node(start_node.name)
	end_node = graph.get_node(end_node.name)

	#start node will always be the same
	h = partial(heuristic, start_node)

	unvisited = []
	visited = []
	for node in graph.nodes:
		 node.update_data("g", inf)
		 node.update_data("f", inf)
		 node.update_data("previous", None)
		 unvisited.append(node)
	start_node.update_data("g", 0)
	start_node.update_data("f", h(start_node))

	current = start_node
	while True:
		lowest_cost = min([node.get_data("f") for node in unvisited])
		current = [node for node in unvisited if node.get_data("f") == lowest_cost][0]
		unvisited.remove(current)
		visited.append(current)
		if current == end_node:
			return graph

		g_of_current = current.get_data("g")
		for neighbour in current.neighbours:
			if neighbour not in visited:
				new_g = current.get_edge_weight(neighbour) + g_of_current
				if new_g < neighbour.get_data("g"):
					neighbour.update_data("g", new_g)
					neighbour.update_data("f", new_g + h(neighbour))
					neighbour.update_data("previous", current)

def find_shortest_path(graph, start_node, end_node, heuristic=manhattan_dist):
	'''
	Finds the shortest path from a node to another node
	:param graph: A Graph object
	:param start_node: A Node object
	:param end_node: A Node object
	:param heuristic: a function of the form f(start_node, node), if not passed uses a built in Manhattan distance heuristic
	:returns: List of Strings, the names of the nodes that make up the shortest path, starts with start_node and ends with end_node
	'''
	graph = traverse_graph(graph, start_node, end_node, heuristic)
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
