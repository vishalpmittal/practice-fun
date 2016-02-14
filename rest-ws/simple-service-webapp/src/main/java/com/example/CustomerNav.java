package com.example;

// NO Path annotation

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.Response.ResponseBuilder;

public class CustomerNav {
    private Customer self;

    public CustomerNav(Customer self) {
        System.out.println("Constructing customer nav");
        this.self = self;
    }
    
    @Path("/name")
    @GET
    public String getName() {
        return self.getName();
    }
    
    @Path("/")
    @GET
    public Response getWhole() {
        System.out.println("in nav, getWhole");
        ResponseBuilder rb = Response.ok();
        rb.entity(new CustomerTO(self));
        return rb.build();
    }
}