package designPatterns.creational.builder;

/**
 * Created by Vishal on 8/27/2015.
 */

public class LunchOrder_Builder {
    public static class Builder {
        private String bread;
        private String condiments;
        private String dressing;
        private String meat;

        public Builder() {
        }

        public LunchOrder_Builder build() {
            return new LunchOrder_Builder(this);
        }

        public Builder bread(String bread) {
            this.bread = bread;
            return this;
        }

        public Builder condiments(String condiments) {
            this.condiments = condiments;
            return this;
        }

        public Builder dressing(String dressing) {
            this.dressing = dressing;
            return this;
        }

        public Builder meat(String meat) {
            this.meat = meat;
            return this;
        }
    }

    private final String bread;
    private final String condiments;
    private final String dressing;
    private final String meat;

    private LunchOrder_Builder(Builder builder) {
        this.bread = builder.bread;
        this.condiments = builder.condiments;
        this.dressing = builder.dressing;
        this.meat = builder.meat;
    }

    public String getBread() {
        return bread;
    }

    public String getCondiments() {
        return condiments;
    }

    public String getDressing() {
        return dressing;
    }

    public String getMeat() {
        return meat;
    }

    public String toString(){
        return getBread() + ", " + getCondiments() + ", " + getDressing() + ", " + getMeat();
    }

    public static void main(String args[]) {
        LunchOrder_Builder.Builder builder = new LunchOrder_Builder.Builder();
        builder.bread("Wheat").condiments("Lettuce").dressing("Meyo").meat("Turkey");

        LunchOrder_Builder lunchOrder = builder.build();
        System.out.println(lunchOrder);
    }
}