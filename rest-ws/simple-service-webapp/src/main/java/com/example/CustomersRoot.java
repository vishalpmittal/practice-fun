package com.example;

import java.util.Date;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;

@Path("/customers")
public class CustomersRoot {
    
    @Path("/{id}")
    public CustomerNav getOneCustomer(@PathParam("id") String id) {
        System.out.println("In root, getOneCustomer");
        // Fake db lookup!!!!
        CustomerNav cn = new CustomerNav(new Customer("Fred Jones " + id, 10_000L, new Date()));
        return cn;
    }
    
//    @POST
//    @Consumes({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
//    @Produces({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
//    public Response createOneCustomer(CustomerTO inputCustomer) {
//        ResponseBuilder rb = Response.ok();
//
//        System.out.println("Received a customerTO: " + inputCustomer);
//        CustomerTO cto = new CustomerTO("Great Lord " + inputCustomer.name, 100_000L, inputCustomer.customerSince);
//        rb.entity(cto);
//        return rb.build();
//    }
}