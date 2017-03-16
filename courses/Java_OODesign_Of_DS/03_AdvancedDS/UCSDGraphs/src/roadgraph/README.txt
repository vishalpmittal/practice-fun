=======================================================
Class: MapGraph
-------------------
Modifications made to MapGraph (what and why):

-  Fields
	HashMap<GeographicPoint, MapNode> vertices
	
-  Methods
	-  Implemented all the provided TODO methods.
	-  In addition I added following methods
		-  toString()
		-  private LinkedList<GeographicPoint> reconstructPath(GeographicPoint start, 
			GeographicPoint goal, HashMap<GeographicPoint, GeographicPoint> parentMap)

			This is a private helper method which returns the traceback path to
			the goal from start provided the parent map. It is called from bfs search method.
	
this class contains a hash map with keys as GeographicalPoints and values as
their respective MapNodes. Total graph is represented with the help of all these 
MapNodes which in turn contains lists of incoming and outgoing edges. 
Thus representing a graph using Adjacency Lists

=======================================================
Class name: MapNode
-------------------
Purpose and description of class:
-  Fields
	private GeographicPoint location
	private List<MapEdge> inEdges
	private List<MapEdge> outEdges
-  Methods
	-  getters and setters and toString()
	-  public int getTotalNumEdges()
		returns sum of incoming and outgoing edges
	-  public Set<MapNode> getOutEdgeNodes()
		return a set of vertices/nodes that can be reached from current node
	
class which represents each node in a graph each node has a GraphicalLocation 
and two lists. One for out going edges and the other one for incoming edges
=======================================================
Class name: MapEdge
-------------------
Purpose and description of class:

-  Fields
	private MapNode fromNode
	private MapNode toNode
	private String streetName
	private String streetType
	private double distance
-  Methods
	getters, setters and toString

class which represents an edge in a graph each edge has from and to nodes, 
edge name, type and distance distance can also be visualized as weight. 
	
=======================================================
Overall Design Justification:
--------------------------------------

I used adjacency list representation of the graph. In this representation the MapGraph contains 
pointers to all the MapNodes which in turn contains pointers to all the connected nodes with the 
help of two lists. These lists maintains the pointers to inward edges and outward edges. 
I could have used one list for edges but in future if we need to extend this class it would be good
to maintain in and out edges separately. Also as we already have edge objects created and these lists
are just storing pointer to them so consuming no extra space. But giving flexibility of information at 
all times.
=======================================================
