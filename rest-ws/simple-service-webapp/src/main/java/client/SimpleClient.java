package client;

import com.example.CustomerTO;
import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.client.Invocation.Builder;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

public class SimpleClient {
    public static void main(String [] args) {
        Client c = ClientBuilder.newClient();
        WebTarget whole = c.target("http://localhost:8080/simple-service-webapp/webapi/customers/123");
        WebTarget t = whole.path("name");
        Builder b = t.request();
        Response r = b.buildGet().invoke();
        String name = r.readEntity(String.class);
        int status = r.getStatus();
        System.out.println("Status code " + status + " name is " + name);
        
        b = whole.request();
        b = b.accept(MediaType.APPLICATION_XML);
        r = b.buildGet().invoke();
//        CustomerTO cto = r.readEntity(CustomerTO.class);
//        System.out.println("Customer is " + cto);
//        
        System.out.println("As raw XML: " +r.readEntity(String.class));
    }
}