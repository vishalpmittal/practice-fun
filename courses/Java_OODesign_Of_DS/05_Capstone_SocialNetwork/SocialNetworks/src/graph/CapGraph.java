/**
 * 
 */
package graph;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map.Entry;
import java.util.Queue;
import java.util.Stack;

/**
 * @author Your name here.
 * 
 *         For the warm up assignment, you must implement your Graph in a class
 *         named CapGraph. Here is the stub file.
 *
 */
public class CapGraph implements Graph {

	HashMap<Integer, CapNode> graph = new HashMap<Integer, CapNode>();
	CapNode sepNode = new CapNode(-1);
	/*
	 * (non-Javadoc)
	 * 
	 * @see graph.Graph#addVertex(int)
	 */
	@Override
	public void addVertex(int num) {
		// Auto-generated method stub
		if (!this.graph.containsKey(num)) {
			this.graph.put(num, new CapNode(num));
		}
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see graph.Graph#addEdge(int, int)
	 */
	@Override
	public void addEdge(int from, int to) {
		// Auto-generated method stub
		this.addVertex(from);
		this.addVertex(to);
		CapNode fromNode = this.graph.get(from);
		CapNode toNode = this.graph.get(to);

		fromNode.addOutwardNode(toNode);
		toNode.addInwardNode(fromNode);
	}

	public CapNode getVertex(int data) {
		return this.graph.get(data);
	}

	public Stack<CapNode> getVertices() {
		Stack<CapNode> vertices = new Stack<CapNode>();
//
//		vertices.push(this.graph.get(65));
//		vertices.push(this.graph.get(50));
//		vertices.push(this.graph.get(44));
//		vertices.push(this.graph.get(32));
//		vertices.push(this.graph.get(25));
//		vertices.push(this.graph.get(23));
//		vertices.push(this.graph.get(18));

		 for(Entry<Integer, CapNode> entry: this.graph.entrySet()) {
			 vertices.push(entry.getValue());
		 }
		return vertices;
	}

	public Graph getTransposedGraph() {
		Graph gt = new CapGraph();
		for (Integer node : this.graph.keySet()) {
			gt.addVertex(node.intValue());
		}

		for (Integer node : this.graph.keySet()) {
			for (CapNode outNode : this.graph.get(node).getOutwardNodes()) {
				gt.addEdge(outNode.getData(), node);
			}
		}
		return gt;
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see graph.Graph#getEgonet(int)
	 */
	@Override
	public Graph getEgonet(int center) {
		// Auto-generated method stub
		Graph egoNetGraph = new CapGraph();
		if (!this.graph.containsKey(center))
			return egoNetGraph;

		HashSet<Integer> egoSet = new HashSet<Integer>();
		egoSet.add(center);

		for (CapNode connNode : this.graph.get(center).getOutwardNodes()) {
			egoSet.add(connNode.getData());
		}

		for (int currInt : egoSet) {
			egoNetGraph.addVertex(currInt);

			for (CapNode relayNode : this.graph.get(currInt).getOutwardNodes()) {
				if (egoSet.contains(relayNode.getData())) {
					egoNetGraph.addEdge(currInt, relayNode.getData());
				}
			}
		}
		return egoNetGraph;
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see graph.Graph#getSCCs()
	 */
	@Override
	public List<Graph> getSCCs() {
		// Initialize sccGraphs list and vertices stack
		//------------------------------------------------
		List<Graph> sccGraphs = new ArrayList<Graph>();
		Stack<CapNode> vertices = getVertices();
		
		// Call DFS once
		//------------------------------------------------
		Stack<CapNode> retFinished = DFS(this, vertices);

		// Get the transpose of graph and get vertices stack for transposed graph
		//------------------------------------------------
		Graph gt = this.getTransposedGraph();		
		Stack<Integer> tempStack = new Stack<Integer>();
		vertices = new Stack<CapNode>();
		while (!retFinished.isEmpty()) {
			CapNode cn = retFinished.pop();
			if(cn != sepNode)
				tempStack.push(cn.getData());
		}
		while (!tempStack.isEmpty()) {
			vertices.push(((CapGraph) gt).getVertex(tempStack.pop()));
		}
		
		// call DFS on transpose graph
		//------------------------------------------------
		retFinished = DFS(gt, vertices);
		
		// Construct the return list graphs
		//------------------------------------------------
		while(!retFinished.empty()){
			HashSet<Integer> sccNodes = new HashSet<Integer>(); 
			Graph sccGraph = new CapGraph();
			
			CapNode sccNode = retFinished.pop();
			while(sccNode != sepNode){
				sccNodes.add(sccNode.getData());
				sccNode = retFinished.pop();
			}
			for(Integer node : sccNodes){
				sccGraph.addVertex(node);
				for (CapNode outNode : this.graph.get(node).getOutwardNodes()){

					if(sccNodes.contains(outNode.getData())){
						sccGraph.addVertex(outNode.getData());
						sccGraph.addEdge(node, outNode.getData());
					}
				}
			}
			sccGraphs.add(sccGraph);
		}

		return sccGraphs;
	}

	public Stack<CapNode> DFS(Graph g, Stack<CapNode> vertices) {
		HashSet<CapNode> visited = new HashSet<CapNode>();
		Stack<CapNode> finished = new Stack<CapNode>();

		while (!vertices.empty()) {
			CapNode tempNode = vertices.pop();
			if (!visited.contains(tempNode)) {
				finished.push(sepNode);
				dfsVisit(g, tempNode, visited, finished);
			}
		}
		return finished;
	}

	private void dfsVisit(Graph g, CapNode v, HashSet<CapNode> visited, Stack<CapNode> finished) {
		visited.add(v);
		for (CapNode outNode : v.getOutwardNodes()) {
			if (!visited.contains(outNode)) {
				dfsVisit(g, outNode, visited, finished);
			}
		}
		finished.push(v);
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see graph.Graph#exportGraph()
	 */
	@Override
	public HashMap<Integer, HashSet<Integer>> exportGraph() {
		// Auto-generated method stub
		HashMap<Integer, HashSet<Integer>> expGraph = new HashMap<Integer, HashSet<Integer>>();
		for (int node : this.graph.keySet()) {
			HashSet<Integer> tmphashset = new HashSet<Integer>();
			for (CapNode connNode : this.graph.get(node).getOutwardNodes()) {
				tmphashset.add(connNode.getData());
			}
			expGraph.put(node, tmphashset);
		}

		return expGraph;
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder("");
		for (int i : this.graph.keySet()) {
			sb.append(this.graph.get(i).toString() + "\n");
		}
		return sb.toString();
	}

	public static void main(String args[]) {
//		Graph myg = new CapGraph();
//		util.GraphLoader.loadGraph(myg, "./data/facebook_1000.txt");
//
////		myg.addVertex(32);
////		myg.addVertex(50);
////		myg.addVertex(44);
////		myg.addVertex(25);
////		myg.addVertex(23);
////		myg.addVertex(65);
////		myg.addVertex(18);
////
////		myg.addEdge(32, 44);
////		myg.addEdge(32, 50);
////		myg.addEdge(44, 50);
////		myg.addEdge(25, 23);
////		myg.addEdge(25, 65);
////		myg.addEdge(25, 18);
////		myg.addEdge(23, 25);
////		myg.addEdge(23, 18);
////		myg.addEdge(65, 23);
////		myg.addEdge(18, 44);
////		myg.addEdge(18, 23);
//
////		System.out.println(myg);
////		System.out.println(((CapGraph) myg).getTransposedGraph());
//		List<Graph> sccs = myg.getSCCs();
//		for (Graph scc : sccs)
//			System.out.println(scc + "=========\n");
//
//		System.out.println(sccs.size());
	}
}
