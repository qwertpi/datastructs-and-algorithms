from graph import Graph, Node

from pytest import approx, raises
from math import inf

def test_get_non_existant_node():
	g = Graph()
	with raises(KeyError):
		g.get_node("A")
def test_add_node():
	g = Graph()
	g.add_node("A")
	assert list(g.node_names) == ["A"]

def test_several_nodes():
	g = Graph()
	g.add_node("A")
	g.add_node("B")
	g.add_node("C")
	assert sorted(g.node_names) == ["A", "B", "C"]

def test_add_same_node():
	g = Graph()
	g.add_node("A")
	with raises(ValueError):
		g.add_node("A")

def test_edges():
	g = Graph()
	a = g.add_node("A")
	b = g.add_node("B")
	c = g.add_node("C")
	g.add_edge(a, b, 5)
	assert b.get_edge_weight(a) == 5
	g.add_edge(g.get_node("C"), g.get_node("B"), 3)
	assert g.get_node("C").get_edge_weight(g.get_node("B")) == 3

def test_node_edge():
	g = Graph()
	a = g.add_node("A")
	b = g.add_node("B")
	with raises(Exception):
		a.add_edge(b, 5)
	assert a.add_edge(b, 5, True) == None
def test_weight_non_existant_edge():
	g = Graph()
	a = g.add_node("A")
	b = g.add_node("B")
	c = g.add_node("C")
	g.add_edge(a, b, 5)
	g.add_edge(b, c, 3)
	assert a.get_edge_weight(c) == inf


def test_neigbours():
	g = Graph()
	a = g.add_node("A")
	b = g.add_node("B")
	c = g.add_node("C")
	d = g.add_node("D")
	g.add_edge(a, b, 5)
	g.add_edge(c, b, 3)
	assert sorted([node.name for node in b.neighbours]) == ["A", "C"]
	assert len(d.neighbours) == 0

def test_data_storage():
	g = Graph()
	a = g.add_node("A")

	a.update_data("foo", 4)
	a.update_data("bar", 2)

	assert [a.get_data("foo"), a.get_data("bar")] == [4, 2]

def test_undirected():
	g = Graph(directed=True)
	a = g.add_node("A")
	b = g.add_node("B")
	g.add_edge(a, b, 10)
	assert a.get_edge_weight(b) == 10
	assert b.get_edge_weight(a) == inf
	g.add_edge(b, a, 3)
	assert a.get_edge_weight(b) == 10
	assert b.get_edge_weight(a) == 3