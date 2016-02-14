package com.example;

import java.net.URI;
import java.util.List;
import java.util.Map;
import javax.ws.rs.DELETE;
import javax.ws.rs.DefaultValue;
import javax.ws.rs.GET;
import javax.ws.rs.HeaderParam;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.HttpHeaders;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.PathSegment;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.Response.ResponseBuilder;
import javax.ws.rs.core.Response.Status;
import javax.ws.rs.core.UriInfo;

/**
 * Root resource (exposed at "myresource" path)
 */
@Path("myresource")
public class MyResource {

    
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String getIt(@Context UriInfo uriInfo) {
        URI p = uriInfo.getAbsolutePath();
        return "Got it from path " + p;
    }
    
    @DELETE
    public String deleteOne() {
        System.out.println("Deleted an entry");
        return "Ouch!";
    }
    
    @Path("/{id: \\d+}")
    @GET
    public String getAResource(@PathParam("id") int theId) {
        return "Ninety Nine! no, really it's " + theId;
    }
    
    @Path("/{id}")
    @GET
    public String getAResource(@PathParam("id") String theId) {
        return "unconstrained: " + theId;
    }
    
    @Path("/dodgy")
    @GET
    public Response getDodgyResult() {
        ResponseBuilder rb = Response.ok();
        if (Math.random() > 0.5) {
            rb.entity("Whoo hoo, it worked!");
        } else {
            rb.entity("Ouch, that failed.");
            rb.header("x-why-it-broke", "random bad luck");
            rb.status(Status.NOT_FOUND);
        }
        return rb.build();
    }
    
    @Path("/queriestuff")
    @GET
    public String getWithQueries(@DefaultValue("UNKNOWN") @QueryParam("name") String name, 
            @QueryParam("address") String address,
            @HeaderParam("x-interesting") String interesting) {
        return name + " lives at " + address + " and it's interesting that: " + interesting;
    }
    
       
    @GET
    @Path("/{path: [a-zA-Z0-9/]+}")
    public String getSegments(@Context UriInfo uriInfo) {
        List<PathSegment> lps = uriInfo.getPathSegments();
        StringBuilder sb = new StringBuilder();
        for (PathSegment p : lps) {
            sb.append(p.getPath()).append("\n");
        }
        return "SEgmented path " + sb.toString();
    }
    
    @GET
    @Path("/headers")
    public String getAllHeader(@Context HttpHeaders headers) {
        Map<String, List<String>> hdrs = headers.getRequestHeaders();
        final StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, List<String>> e : hdrs.entrySet()) {
            for (String s : e.getValue()) {
                sb.append(e.getKey()).append(" : ").append(s).append("\n");
            }
        }
        return "headers:\n" + sb;
    }
    
    @POST
    @Path("/makeaname")
    public Response makeAName(String name) {
        ResponseBuilder rb = Response.ok();
        System.out.println("Received input entity: " + name);
        rb.entity("You sent the name " + name);
        rb.header("location", "newname");
        rb.status(Status.CREATED);
        
        return rb.build();
    }
}