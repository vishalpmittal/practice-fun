package coreSpring.unit001;

public class Triangle {

    private String trgType;
    private int height;

    public Triangle(String trgType) {
        this.trgType = trgType;
    }

    public Triangle(int height) {
        this.height = height;
    }

    public Triangle(String trgType, int height) {
        this.trgType = trgType;
        this.height = height;
    }

    public String getTrgType() {
        return trgType;
    }

    public void setTrgType(String trgType) {
        this.trgType = trgType;
    }

    public int getHeight() {
        return height;
    }

    public void draw() {
        System.out.println(this.getTrgType() + " Triangle Drawn of height "
                + this.getHeight());
    }
}
