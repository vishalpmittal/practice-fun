package com.vishal;

import javax.ws.rs.GET;
import javax.ws.rs.HeaderParam;
import javax.ws.rs.POST;

import java.util.List;
import java.util.Map;

import javax.ws.rs.DELETE;
import javax.ws.rs.DefaultValue;
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

    /**
     * Method handling HTTP GET requests. The returned object will be sent
     * to the client as "text/plain" media type.
     *
     * @return String that will be returned as a text/plain response.
     */
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String getIt() {
        return "Got it!";
    }
    
    @DELETE
    public String deleteOne(){
    	System.out.println("Deleted an entry!!");
    	return "Deleted it!...";
    }

    @Path("/myPath")
    @GET
    public String myPathMethod(){
    	// called as
    	// GET http://localhost:8080/simple-service-webapp/webapi/myresource/myPath
    	
    	return "My path method invoked";
    }
    
    
//    @Path("/{id}")
//    @GET
//    public String getAResource(@PathParam("id") String theId){
//    	// called as
//    	// GET http://localhost:8080/simple-service-webapp/webapi/myresource/xyz
//    	return "I got the generic id as: " + theId;
//    }
    
    @Path("/{id: \\d+}")
    @GET
    public String regexMethod(@PathParam("id") int theId){
    	return "I got the integer id as: " + theId;
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
