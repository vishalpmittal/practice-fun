package graph;

import java.util.ArrayList;

public class CapNode implements Cloneable{
	private int data = 0;
	private ArrayList<CapNode> outwardNodes = null;
	private ArrayList<CapNode> inwardNodes = null;
	
	public CapNode(int data) {
		this.data = data;
		this.outwardNodes = new ArrayList<CapNode>();
		this.inwardNodes = new ArrayList<CapNode>();
	}

	public int getData() {
		return data;
	}

	public void setData(int data) {
		this.data = data;
	}

	public int getOutDegree(){
		return this.outwardNodes.size();
	}
	
	public ArrayList<CapNode> getOutwardNodes() {
		return outwardNodes;
	}

	public void addOutwardNode(CapNode outwardNode) {
		this.outwardNodes.add(outwardNode);
	}

	public int getInDegree(){
		return this.inwardNodes.size();
	}
	
	public ArrayList<CapNode> getInwardNodes() {
		return inwardNodes;
	}

	public void addInwardNode(CapNode inwardNode) {
		this.inwardNodes.add(inwardNode);
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder("");
		sb.append("CapNode [data=" + data + "; outwardNodes=");
		for (CapNode outNode : this.outwardNodes){
			sb.append(outNode.getData()+", ");
		}
		sb.append(" ]");
		return sb.toString();
	}
	
}
