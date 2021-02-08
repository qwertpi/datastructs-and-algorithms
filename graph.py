from math import inf

class Node():
	'''
	A single node on a graph, intended to be instantiated by the add_node method of a Graph object

	Attributes
	----------
	name: String, the human readable name of the node
	neighbours: List of Node objects, all the nodes that are directly connected to self

	Methods
	-------
	add_edge(node, edge_weight)
		Adds an edge from self to another node with the specified weight. Use Graph.add_edge instead of this
	get_edge_weight(node)
		Gets the weight of the edge from self to node
	update_data(field_name, new_value)
		Stores new_value and allows you to retrieve it by calling get_data(field_name). 
		Allows arbitrary data to be associated with a specific node
	get_data(field_name)
	    Retrieves data associated with the node
	'''
	def __init__(self, name):
		'''
		:param name: String, the human readable name of the node
		'''
		self.name = name
		self.__adjecent_nodes = {}
		self.__data = {}

	@property
	# pylint: disable=locally-disabled, missing-function-docstring
	def neighbours(self):
		return self.__adjecent_nodes.keys()


	def add_edge(self, node, edge_weight, know_what_im_doing=False):
		'''
		Adds an edge connecting self to another node object
		IMPORTANT: If using an undirected graph, Graph.add_edge is preferred as it will add the edge from node to self for you. 
		If you still want to use Node.add_edge call it using Node.add_edge(node, weight, True)
		:param edge_weight: Float or Int, the weight to be associated with the edge
		'''
		if know_what_im_doing:
			self.__adjecent_nodes[node] = edge_weight
		else:
			raise Exception("Graph.add_edge is preferred to Node.add_edge, especially for undirected graphs, see the Node.add_edge docstring for more info")

	def get_edge_weight(self, node):
		'''
		Gets the weight of the edge connecting self to another node
		:param node: Node object, the node the edge you are interested in points towards
		:returns: Float or Int, the weight of the edge
		'''
		try:
			return self.__adjecent_nodes[node]
		except KeyError:
			return inf


	def update_data(self, field_name, new_value):
		'''
		Allows a new field to be created or the value of an existing field to be updated
		:param field_name: String, the name you want to use to access the field in the future
		:param new_value: Anything you want, the data to associate with field_name
		'''
		self.__data[field_name] = new_value

	def get_data(self, field_name):
		'''
		Retrieves the data that was associated with a field
		:param field_name: String, the field you wish to retrieve
		:returns: The data associated with field name
		'''
		return self.__data[field_name]


class Graph():
	'''
	A series of nodes connected by edges
	Can be directed or undirected but must be weighted

	Attributes
	----------
	nodes: Iterable of Node objects, the nodes that make up the graph
	node_names: Iterable of Strings, the human readable names of the nodes that make up the graph
	undirected: Boolean, defaults to True

	Methods
	-------
	add_node(node_name):
		Creates a new Node object with name node_name and adds it to the graph
	get_node(node_name):
		Returns the node object with human readable name node_name
	add_edge(node_a_name, node_b_name, edge_weight)
			Adds an edge connecting the node with name node_a_name to the node with name node_b_name with weight edge_weight
			If the graph is undirected, also adds an edge connecting node_b_name to node_a_name with weight edge_wegiht
	'''
	def __init__(self, directed=False):
		'''
		:param directed: Boolean, whether the graph is directed, defaults to False
		'''
		self.__nodes = {}
		self.undirected = not directed

	@property
	# pylint: disable=locally-disabled, missing-function-docstring
	def nodes(self):
		return self.__nodes.values()

	@property
	# pylint: disable=locally-disabled, missing-function-docstring
	def node_names(self):
		return self.__nodes.keys()


	def add_node(self, node_name):
		'''
		Creates a new node and adds it to the graph
		:param node_name: String, the human readable name to associate with the node
		:returns: Node object, the node you just created. There's no need to store this though as you can always call get_node
		'''
		if node_name in self.node_names:
			print("A node already exists with name", node_name)
			raise ValueError
		new_node = Node(node_name)
		self.__nodes[node_name] = new_node
		return new_node

	def get_node(self, node_name):
		'''
		Converts a human readable node_name into the corresponding Node object
		:param node_name: String
		:returns: A Node object
		'''
		try:
			return self.__nodes[node_name]
		except KeyError as e:
			print("No nodes exist with name", node_name)
			raise e

			
	def add_edge(self, node_a, node_b, edge_weight):
		'''
		Adds an edge connecting a node to another node
		:param node_a: Node object, the node the edge is from
		:param node_b: Node object,  the node the edge is towards
		:param edge_weight: Float or Int
		'''
		node_a.add_edge(node_b, edge_weight, True)
		if self.undirected:
			node_b.add_edge(node_a, edge_weight, True)
