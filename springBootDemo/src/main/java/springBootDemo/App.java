package springBootDemo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class App {

    public static void main(String[] args) {
        /* Static class SpringApplication. What happens when run is called on this class:
         * - Sets up default configuration
         * - Starts spring application context
         * - performs class path scan
         * - Starts Tomcat server */
        SpringApplication.run(App.class, args);
    }

}
