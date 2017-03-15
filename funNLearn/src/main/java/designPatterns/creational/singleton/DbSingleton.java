package designPatterns.creational.singleton;

/**
 * Created by Vishal on 8/27/2015.
 */
public class DbSingleton {
    // Lazily loaded as null initially
    private static DbSingleton instance = null;

    // Private no argument constructor
    private DbSingleton() {
    }

    // singleton getInstance should always be without any argument
    public static DbSingleton getInstance() {
        // Lazily loaded as instance created only when needed
        if(instance==null){
            // Make it thread safe
            synchronized(DbSingleton.class){
                // Double check the null for each thread
                if(instance==null)
                    instance = new DbSingleton();
            }
        }
        return instance;
    }
}
