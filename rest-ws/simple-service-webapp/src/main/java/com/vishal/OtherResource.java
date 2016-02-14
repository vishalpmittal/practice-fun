/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.vishal;

import javax.inject.Singleton;
import javax.ws.rs.GET;
import javax.ws.rs.Path;

@Singleton
@Path("/others")
public class OtherResource {
    private int count = 0;
    
    @Path("/counter")
    @GET
    public String count() {
        return "The count is " + count++;
    }
}