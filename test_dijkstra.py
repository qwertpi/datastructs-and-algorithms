from dijkstra import find_shortest_path, traverse_graph
from graph import Graph, Node
from pytest import approx, raises

def test_purity():
	g = Graph()

	S = g.add_node("S")
	A = g.add_node("A")
	B = g.add_node("B")
	g.add_edge(B, S, 3)
	g.add_edge(A, S, 7)
	g.add_edge(A, B, 12)

	traverse_graph(g, S)
	with raises(KeyError):
		B.get_data("previous")
	with raises(KeyError):
		A.get_data("previous")
	
	g = traverse_graph(g, S)
	assert g.get_node("A").get_data("previous").name == "S"
	assert g.get_node("B").get_data("previous").name == "S"

def test_small_graph():
	g = Graph()

	nodes = list(map(g.add_node, ("A", "B", "C", "D", "E")))

	g.add_edge(nodes[0], nodes[1], 3)
	g.add_edge(nodes[0], nodes[2], 1)
	g.add_edge(nodes[1], nodes[2], 7)
	g.add_edge(nodes[1], nodes[3], 5)
	g.add_edge(nodes[1], nodes[4], 1)
	g.add_edge(nodes[3], nodes[4], 7)


	assert find_shortest_path(g, nodes[2], nodes[4]) == ["C", "A", "B", "E"]

def test_large_graph():
	#this is the graph from https://www.youtube.com/watch?v=GazC3A4OQTE
	g = Graph()

	S = g.add_node("S")
	A = g.add_node("A")
	B = g.add_node("B")
	C = g.add_node("C")
	D = g.add_node("D")
	F = g.add_node("F")
	G = g.add_node("G")
	H = g.add_node("H")
	I = g.add_node("I")
	J = g.add_node("J")
	K = g.add_node("K")
	L = g.add_node("L")
	E = g.add_node("E")

	g.add_edge(A, B, 3)
	g.add_edge(A, D, 4)
	g.add_edge(A, S, 7)
	g.add_edge(B, H, 1)
	g.add_edge(B, D, 4)
	g.add_edge(B, S, 2)
	g.add_edge(C, S, 3)
	g.add_edge(C, L, 2)
	g.add_edge(D, F, 5)
	g.add_edge(E, G, 2)
	g.add_edge(E, K, 5)
	g.add_edge(F, H, 3)
	g.add_edge(G, H, 2)
	g.add_edge(I, J, 6)
	g.add_edge(I, L, 4)
	g.add_edge(I, K, 4)


	assert find_shortest_path(g, S, E) == ["S", "B", "H", "G", "E"]
