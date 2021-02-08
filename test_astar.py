from astar import find_shortest_path, traverse_graph, manhattan_dist
from graph import Graph, Node
from pytest import approx, raises

def test_mahatan():
	g = Graph()
	A = g.add_node("A")
	B = g.add_node("B")

	A.update_data("coord", (-3, 5))
	B.update_data("coord", (12, -9))
	assert manhattan_dist(A, B) == 29

def test_purity():
	g = Graph()

	S = g.add_node("S")
	S.update_data("coord", (0, 0))
	A = g.add_node("A")
	A.update_data("coord", (3, 1))
	B = g.add_node("B")
	B.update_data("coord", (2, 3))
	g.add_edge(B, S, 3)
	g.add_edge(A, S, 7)
	g.add_edge(A, B, 12)

	traverse_graph(g, S, B, manhattan_dist)
	with raises(KeyError):
		B.get_data("previous")
	with raises(KeyError):
		A.get_data("previous")
	
	g = traverse_graph(g, S, B, manhattan_dist)
	assert g.get_node("A").get_data("previous").name == "S"
	assert g.get_node("B").get_data("previous").name == "S"


def test_small_graph():
	#graph from https://www.codingame.com/playgrounds/1608/shortest-paths-with-dijkstras-algorithm/dijkstras-algorithm
	#coordinates are highly approximate
	g = Graph()

	A = g.add_node("A")
	A.update_data("coord", (-2, 0))
	B = g.add_node("B")
	B.update_data("coord", (0, 1))
	C = g.add_node("C")
	C.update_data("coord", (-1, -2))
	D = g.add_node("D")
	D.update_data("coord", (1, -1))
	E = g.add_node("E")
	E.update_data("coord", (2, 2))

	g.add_edge(A, B, 3)
	g.add_edge(A, C, 1)
	g.add_edge(B, C, 7)
	g.add_edge(B, D, 5)
	g.add_edge(B, E, 1)
	g.add_edge(D, E, 7)


	assert find_shortest_path(g, C, E) == ["C", "A", "B", "E"]

def test_large_graph():
	#this is the graph from https://www.youtube.com/watch?v=GazC3A4OQTE
	#Co-ordinates are based off measuring number of pixels between nodes in a screengrab of video so shoudln't be too far off
	g = Graph()

	S = g.add_node("S")
	S.update_data("coord", (42, 11))
	A = g.add_node("A")
	A.update_data("coord", (18, 26))
	B = g.add_node("B")
	B.update_data("coord", (38, 29))
	C = g.add_node("C")
	C.update_data("coord", (83, 9))
	D = g.add_node("D")
	D.update_data("coord", (12, 44))
	F = g.add_node("F")
	F.update_data("coord", (18, 49))
	G = g.add_node("G")
	G.update_data("coord", (47, 54))
	H = g.add_node("H")
	H.update_data("coord", (34, 43))
	I = g.add_node("I")
	I.update_data("coord", (80, 35))
	J = g.add_node("J")
	J.update_data("coord", (101, 35))
	K = g.add_node("K")
	K.update_data("coord", (89, 45))
	L = g.add_node("L")
	L.update_data("coord", (95, 23))
	E = g.add_node("E")
	E.update_data("coord", (74, 63))

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
