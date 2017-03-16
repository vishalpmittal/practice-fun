/**
 * @author UCSD MOOC development team and YOU
 * 
 * A class which reprsents a graph of geographic locations
 * Nodes in the graph are intersections between 
 *
 */
package roadgraph;


import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map.Entry;
import java.util.PriorityQueue;
import java.util.Set;
import java.util.function.Consumer;
import java.util.Queue;

import geography.GeographicPoint;
import util.GraphLoader;

/**
 * @author UCSD MOOC development team and YOU
 * 
 * A class which represents a graph of geographic locations
 * Nodes in the graph are intersections between 
 *
 */
public class MapGraph {
	/*
	 * The graph is a adjacency list graph. Here we maintain a HashMap of 
	 * all the vertices. Mapnodes have list of nodes connected to them.*/
	HashMap<GeographicPoint, MapNode> vertices = null;
	
	/** 
	 * Create a new empty MapGraph 
	 */
	public MapGraph()
	{
		// Initialize an empty graph with no vertices
		vertices = new HashMap<GeographicPoint, MapNode>();
	}
	
	/**
	 * Get the number of vertices (road intersections) in the graph
	 * @return The number of vertices in the graph.
	 */
	public int getNumVertices()
	{
		return vertices.size();
	}
	
	/**
	 * Return the intersections, which are the vertices in this graph.
	 * @return The vertices in this graph as GeographicPoints
	 */
	public Set<GeographicPoint> getVertices()
	{
		/**
		 * returns a new hash set that contains all the vertices
		 */
		return new HashSet<GeographicPoint>(this.vertices.keySet());
	}
	
	/**
	 * Get the number of road segments in the graph
	 * @return The number of edges in the graph.
	 */
	public int getNumEdges()
	{
		/*
		 * Add up all the connected nodes and return the total number
		 */
		int totalEdges = 0;
		for (Entry<GeographicPoint, MapNode> entry : vertices.entrySet())
			totalEdges += entry.getValue().getNumOutEdges();

		return totalEdges;
	}
	
	/** Add a node corresponding to an intersection at a Geographic Point
	 * If the location is already in the graph or null, this method does 
	 * not change the graph.
	 * @param location  The location of the intersection
	 * @return true if a node was added, false if it was not (the node
	 * was already in the graph, or the parameter is null).
	 */
	public boolean addVertex(GeographicPoint location)
	{
		/*
		 * add new vertex if not already present
		 */
		if (location == null || this.vertices.containsKey(location))
			return false;
		
		this.vertices.put(location, new MapNode(location));
		return true;
	}
	
	/**
	 * Adds a directed edge to the graph from pt1 to pt2.  
	 * Precondition: Both GeographicPoints have already been added to the graph
	 * @param from The starting point of the edge
	 * @param to The ending point of the edge
	 * @param roadName The name of the road
	 * @param roadType The type of the road
	 * @param length The length of the road, in km
	 * @throws IllegalArgumentException If the points have not already been
	 *   added as nodes to the graph, if any of the arguments is null,
	 *   or if the length is less than 0.
	 */
	public void addEdge(GeographicPoint from, GeographicPoint to, String roadName,
			String roadType, double length) throws IllegalArgumentException {

		// Check for null params
		if (from == null || to == null || roadName == null || roadType == null)
			throw new IllegalArgumentException("Null Argument!!");
		
		// check if negative edge length
		if (length <0)
			throw new IllegalArgumentException("Edge length less than zero!!");
		
		// check if vertices are not present in the map
		if (!this.vertices.containsKey(from) || !this.vertices.containsKey(to))
			throw new IllegalArgumentException("Geographic points not present in the map!!");
		
		MapNode fromNode = this.vertices.get(from);
		MapNode toNode = this.vertices.get(to);

		// create new edge object and add object pointers to respective nodes 
		MapEdge edge = new MapEdge(fromNode, toNode, roadName, roadType, length);
		fromNode.addOutEdge(edge);
		toNode.addInEdge(edge);
	}

	/** Find the path from start to goal using breadth first search
	 * 
	 * @param start The starting location
	 * @param goal The goal location
	 * @return The list of intersections that form the shortest (unweighted)
	 *   path from start to goal (including both start and goal).
	 */
	public List<GeographicPoint> bfs(GeographicPoint start, GeographicPoint goal) {
		// Dummy variable for calling the search algorithms
        Consumer<GeographicPoint> temp = (x) -> {};
        return bfs(start, goal, temp);
	}
	
	/** Find the path from start to goal using breadth first search
	 * 
	 * @param start The starting location
	 * @param goal The goal location
	 * @param nodeSearched A hook for visualization.  See assignment instructions for how to use it.
	 * @return The list of intersections that form the shortest (unweighted)
	 *   path from start to goal (including both start and goal).
	 */
	public List<GeographicPoint> bfs(GeographicPoint start, 
			 					     GeographicPoint goal, Consumer<GeographicPoint> nodeSearched)
	{
		// Initialize: queue, visited HashSet and parent HashMap		
		HashMap<GeographicPoint, GeographicPoint> parentMap = new HashMap<GeographicPoint, GeographicPoint>();
		Set<MapNode> visited = new HashSet<MapNode>();
		Queue<MapNode> queue = new LinkedList<MapNode>();
		boolean found = false;
		
		// Enqueue start onto the queue and add to visited
		queue.add(this.vertices.get(start));
		visited.add(this.vertices.get(start));
		
		// Hook for visualization.
		nodeSearched.accept(start);
		
		// while queue is not empty:
		while(queue.size() > 0){
			// dequeue node curr from front of the queue
			MapNode curr = queue.poll();
			if (curr.getLocation().equals(goal)){
				found = true;
				break;
			}
			
			Set<MapNode> outNodes = curr.getOutEdgeNodes();
			for(MapNode outNode : outNodes){
				if (!visited.contains(outNode)){
					// Hook for visualization.
					nodeSearched.accept(outNode.getLocation());
					visited.add(outNode);
					parentMap.put(outNode.getLocation(), curr.getLocation());
					queue.add(outNode);
				}
			}
		}
		
		if (!found)
			return null;
		
		return reconstructPath(start, goal, parentMap);
	}
	
	private LinkedList<GeographicPoint> reconstructPath(GeographicPoint start, 
			GeographicPoint goal, HashMap<GeographicPoint, GeographicPoint> parentMap){

		// Initialize path as linked list
		LinkedList<GeographicPoint> path = new LinkedList<GeographicPoint>();
		GeographicPoint curr = goal;

		// trace the path from goal to start and add it to linked list
		while (!curr.equals(start)){
			path.addFirst(curr);
			curr = parentMap.get(curr);
		}

		// add the start vertex
		path.addFirst(start);
		return path;
	}

	/** Find the path from start to goal using Dijkstra's algorithm
	 * 
	 * @param start The starting location
	 * @param goal The goal location
	 * @return The list of intersections that form the shortest path from 
	 *   start to goal (including both start and goal).
	 */
	public List<GeographicPoint> dijkstra(GeographicPoint start, GeographicPoint goal) {
		// Dummy variable for calling the search algorithms
		// You do not need to change this method.
        Consumer<GeographicPoint> temp = (x) -> {};
        return dijkstra(start, goal, temp);
	}
	
	/** Find the path from start to goal using Dijkstra's algorithm
	 * 
	 * @param start The starting location
	 * @param goal The goal location
	 * @param nodeSearched A hook for visualization.  See assignment instructions for how to use it.
	 * @return The list of intersections that form the shortest path from 
	 *   start to goal (including both start and goal).
	 */
	public List<GeographicPoint> dijkstra(GeographicPoint start, 
										  GeographicPoint goal, Consumer<GeographicPoint> nodeSearched)
	{
		// Implement this method in WEEK 3
		int anaylyzedNodesNum = 0;
		
		// Initialize : Priority queue(PQ), visited HashSet, parent Hashmap, 
		HashMap<GeographicPoint, GeographicPoint> parentMap = new HashMap<GeographicPoint, GeographicPoint>();
		Set<MapNode> visited = new HashSet<MapNode>();
		PriorityQueue<MapNode> pqueue = new PriorityQueue<MapNode>();
		boolean found = false;

		//Initialize DistFromStart to infinity
		for (MapNode initMapNode : this.vertices.values()){
			initMapNode.setDistFromStart(Double.POSITIVE_INFINITY, true);
		}
		this.vertices.get(start).setDistFromStart(0.0, true);
		
		// Enqueue start onto the queue and add to visited
		pqueue.add(this.vertices.get(start));
		
		// while PQ is not empty
		while(pqueue.size() > 0){
			// dequeue node curr from front of queue
			MapNode curr = pqueue.poll();
			// Hook for visualization.
			nodeSearched.accept(curr.getLocation());
			anaylyzedNodesNum++;
			
			if (!visited.contains(curr)){
				visited.add(curr);

				if (curr.getLocation().equals(goal)){
					found = true;
					break;
				}
				
				List<MapEdge> currOutEdges = curr.getOutEdges();				
				for(MapEdge outEdge : currOutEdges){
					MapNode outNode = outEdge.getToNode();
					if (visited.contains(outNode))
						continue;
					
					double distThroughCurr = curr.getDistFromStart() + outEdge.getDistance();
					if(distThroughCurr < outNode.getDistFromStart()){
						outNode.setDistFromStart(distThroughCurr, true);
						parentMap.put(outNode.getLocation(), curr.getLocation());
						pqueue.add(outNode);
					}
				}
			}
		}
		
		System.out.println("dijkstra; Total vertices analyzed: "+ anaylyzedNodesNum);
		if (!found)
			return null;
		
		return reconstructPath(start, goal, parentMap);
	}

	/** Find the path from start to goal using A-Star search
	 * 
	 * @param start The starting location
	 * @param goal The goal location
	 * @return The list of intersections that form the shortest path from 
	 *   start to goal (including both start and goal).
	 */
	public List<GeographicPoint> aStarSearch(GeographicPoint start, GeographicPoint goal) {
		// Dummy variable for calling the search algorithms
        Consumer<GeographicPoint> temp = (x) -> {};
        return aStarSearch(start, goal, temp);
	}
	
	/** Find the path from start to goal using A-Star search
	 * 
	 * @param start The starting location
	 * @param goal The goal location
	 * @param nodeSearched A hook for visualization.  See assignment instructions for how to use it.
	 * @return The list of intersections that form the shortest path from 
	 *   start to goal (including both start and goal).
	 */
	public List<GeographicPoint> aStarSearch(GeographicPoint start, 
											 GeographicPoint goal, Consumer<GeographicPoint> nodeSearched)
	{
		// Implement this method in WEEK 3
		int anaylyzedNodesNum = 0;
		
		// Initialize : Priority queue(PQ), visited HashSet, parent Hashmap, 
		HashMap<GeographicPoint, GeographicPoint> parentMap = new HashMap<GeographicPoint, GeographicPoint>();
		Set<MapNode> visited = new HashSet<MapNode>();
		PriorityQueue<MapNode> pqueue = new PriorityQueue<MapNode>();
		boolean found = false;

		//Initialize DistFromStart to infinity
		for (MapNode initMapNode : this.vertices.values()){
			initMapNode.setDistFromStart(Double.POSITIVE_INFINITY, true);
		}
		this.vertices.get(start).setDistFromStart(0.0, true);
		
		// Enqueue start onto the queue and add to visited
		pqueue.add(this.vertices.get(start));
		
		// while PQ is not empty
		while(pqueue.size() > 0){
			// dequeue node curr from front of queue
			MapNode curr = pqueue.poll();
			// Hook for visualization.
			nodeSearched.accept(curr.getLocation());
			anaylyzedNodesNum++;
			
			if (!visited.contains(curr)){
				visited.add(curr);

				if (curr.getLocation().equals(goal)){
					found = true;
					break;
				}
				
				List<MapEdge> currOutEdges = curr.getOutEdges();				
				for(MapEdge outEdge : currOutEdges){
					MapNode outNode = outEdge.getToNode();
					if (visited.contains(outNode))
						continue;
					
					double distThroughCurr = curr.getDistFromStart() + outEdge.getDistance();
					double outNodePredDist = distThroughCurr + outNode.getLocation().distance(goal);
					if(outNodePredDist < outNode.getPreditedDist()){
						outNode.setDistFromStart(distThroughCurr, false);
						outNode.setPreditedDist(outNodePredDist);
						parentMap.put(outNode.getLocation(), curr.getLocation());
						pqueue.add(outNode);
					}
				}
			}
		}
			
		System.out.println("aStar; Total vertices analyzed: "+ anaylyzedNodesNum);
		if (!found)
			return null;
		
		return reconstructPath(start, goal, parentMap);		
	}
	
	@Override
	public String toString() {
		return "MapGraph [vertices=" + vertices + "]";
	}

	public static void main(String[] args)
	{
		System.out.print("Making a new map...");
		MapGraph theMap = new MapGraph();
		System.out.print("DONE. \nLoading the map...");
		GraphLoader.loadRoadMap("data/testdata/simpletest.map", theMap);
		System.out.println(theMap);
		System.out.println("DONE.");
		
		// You can use this method for testing.  
		
		// Use this code in Week 3 End of Week Quiz
		MapGraph theMap2 = new MapGraph();
		System.out.print("DONE. \nLoading the map...");
		GraphLoader.loadRoadMap("data/maps/utc.map", theMap2);
		System.out.println("DONE.");

		GeographicPoint start = new GeographicPoint(32.8648772, -117.2254046);
		GeographicPoint end = new GeographicPoint(32.8660691, -117.217393);
		
		
		List<GeographicPoint> route = theMap2.dijkstra(start,end);
		List<GeographicPoint> route2 = theMap2.aStarSearch(start,end);

		
		
	}
	
}
