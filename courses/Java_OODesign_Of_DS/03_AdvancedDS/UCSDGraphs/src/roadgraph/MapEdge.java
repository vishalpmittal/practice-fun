/**
 * @author UCSD MOOC development team and Vishal Mittal
 * 
 * A class which reprsents an edge in a graph
 * each edge has from and to nodes, edge name, type and distance
 * distance can also be visualized as weightage 
 */
package roadgraph;

public class MapEdge {
	private MapNode fromNode = null;
	private MapNode toNode = null;
	private String streetName = null;
	private String streetType = null;
	private double distance = 0.0;

	public MapEdge(MapNode fromNode, MapNode toNode) {
		this.fromNode = fromNode;
		this.toNode = toNode;
		this.streetName = "";
		this.streetType = "";
		this.distance = 0.0;
	}

	public MapEdge(MapNode fromNode, MapNode toNode, String streetName, String streetType, double distance) {
		this.fromNode = fromNode;
		this.toNode = toNode;
		this.streetName = streetName;
		this.streetType = streetType;
		this.distance = distance;
	}
	
	/*===============================
	 * Getters n Setters
	 ===============================*/
	public MapNode getFromNode() {
		return fromNode;
	}

	public void setFromNode(MapNode fromNode) {
		this.fromNode = fromNode;
	}

	public MapNode getToNode() {
		return toNode;
	}

	public void setToNode(MapNode toNode) {
		this.toNode = toNode;
	}

	public String getStreetName() {
		return streetName;
	}

	public void setStreetName(String streetName) {
		this.streetName = streetName;
	}

	public String getStreetType() {
		return streetType;
	}

	public void setStreetType(String streetType) {
		this.streetType = streetType;
	}

	public double getDistance() {
		return distance;
	}

	public void setDistance(double distance) {
		this.distance = distance;
	}

	@Override
	public String toString() {
		return "MapEdge [fromNode=" + fromNode.getLocation() + ", toNode=" + toNode.getLocation() + ", streetName=" + streetName + ", streetType="
				+ streetType + ", distance=" + distance + "]";
	}
	
}
