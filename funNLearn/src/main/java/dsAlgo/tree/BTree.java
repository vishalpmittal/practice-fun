package dsAlgo.tree;

class BTreeNode {
    int[] keys;
    int t;
    BTreeNode[] childerns;
    int n;
    boolean leaf;

    public BTreeNode(int t, boolean leaf) {
        this.t = t;
        this.leaf = leaf;
        this.keys = new int[2 * t - 1];
        this.childerns = new BTreeNode[2 * t];
        this.n = 0;
    }


    public void traverse(){
        for (int i = 0; i<this.n; i++){
            if (! this.leaf)
                childerns[i].traverse();
            
                System.out.print(keys[i] + " ");
        }
        
    }


}

public class BTree {

}