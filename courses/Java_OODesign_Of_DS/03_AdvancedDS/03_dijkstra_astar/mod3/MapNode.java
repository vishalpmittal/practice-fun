/**
 * @author UCSD MOOC development team and Vishal Mittal
 * 
 * A class which reprsents each node in a graph
 * each node has a GraphicalLocation and two lists. One for out going edges 
 * and the other one for incoming edges 
 */
package roadgraph;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import geography.GeographicPoint;

public class MapNode implements Comparable{
	private GeographicPoint location = null;
	private List<MapEdge> inEdges = null;
	private List<MapEdge> outEdges = null;
	private double distFromStart;
	private double preditedDist;

	public MapNode(GeographicPoint location) {
		this.location = location;
		this.inEdges = new ArrayList<MapEdge>();
		this.outEdges = new ArrayList<MapEdge>();
		this.distFromStart = 0.0;
		this.preditedDist = 0.0;
	}

	/*===============================
	 * Getters n Setters
	 ===============================*/
	public GeographicPoint getLocation() {
		return location;
	}

	public List<MapEdge> getInEdges() {
		return new ArrayList<MapEdge>(this.inEdges);
	}

	public void addInEdge(MapEdge inEdge) {
		this.inEdges.add(inEdge);
	}

	public List<MapEdge> getOutEdges() {
		return new ArrayList<MapEdge>(this.outEdges);
	}

	public int getNumOutEdges(){
		return this.outEdges.size();
	}
	
	public void addOutEdge(MapEdge outEdge) {
		this.outEdges.add(outEdge);
	}
	
	/*
	 * @return all the edges i.e. sum of incoming and outgoing edges 
	 */
	public int getTotalNumEdges() {
		return inEdges.size() + outEdges.size();
	}
	
	public double getDistFromStart() {
		return distFromStart;
	}

	public void setDistFromStart(double distFromStart, boolean useAsPredictionDist) {
		this.distFromStart = distFromStart;
		if(useAsPredictionDist){
			this.preditedDist = distFromStart;
		}
	}

	public double getPreditedDist() {
		return preditedDist;
	}

	public void setPreditedDist(double preditedDist) {
		this.preditedDist = preditedDist;
	}

	/*
	 * @return a set of vertices/nodes that can be reached from current node 
	 */	
	public Set<MapNode> getOutEdgeNodes(){
		Set<MapNode> connectedNodes = new HashSet<MapNode>();
		for (MapEdge outEdge: this.outEdges){
			connectedNodes.add(outEdge.getToNode());
		}
		return connectedNodes;
	}
	
	public String toString() {
		return "MapNode [location=" + location + ", inEdges=" + inEdges + ", outEdges=" + outEdges + "]";
	}

	@Override
	public int compareTo(Object o) {
		// Auto-generated method stub
		MapNode m = (MapNode)o; 
		return ((Double)this.getPreditedDist()).compareTo((Double) m.getPreditedDist());
	}
	
	public boolean equals(Object o)
	{
		if (!(o instanceof MapNode) || (o == null)) {
			return false;
		}
		MapNode node = (MapNode)o;
		return node.location.equals(this.location);
	}

}
