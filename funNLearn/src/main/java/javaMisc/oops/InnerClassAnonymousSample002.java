package javaMisc.oops;

class Animal02 {
    public void m1() {
        System.out.println("From animal");
    }
}

class Horse02 extends Animal02 {
    public void m1() {
        System.out.println("From horse");
    }
}

public class InnerClassAnonymousSample002 {

    /* Anonymous inner class.
     * When a common method is classed, this will override the outer class */
    Animal02 a = new Animal02() {
        public void m1() {
            t1();
            System.out.println("Anonymous");
        }

        public void t1() {
            System.out.println("T1");
        }
    };

    /* This is like defining the class then and there itself for thread superclass
     * and overriding the run method. Same for Runnable */
    static Thread t = new Thread() {
        public void run() {
            System.out.println("thread");
        }
    };

    static Runnable r = new Runnable() {
        public void run() {
            System.out.println("r");
        }
    };

    public static void main(String[] args) {
        InnerClassAnonymousSample002 ax = new InnerClassAnonymousSample002();
        ax.a.m1();
        t.start();
        r.run();
    }

}
