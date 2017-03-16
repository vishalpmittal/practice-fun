/*
* Author: Vishal Mittal
* Date: 06/14/2014, Saturday
* Exception if the location to move to is not valid, 
* i.e. negative locations, or out of chess board locations
*/

package org.vpm.game;

@SuppressWarnings("serial")
public class InvalidMoveException extends Exception{

	public InvalidMoveException(String exc) {
    	super(exc);
    }
    
    public String getMessage(){
    	return super.getMessage();
    }
    
    public void printDescription(){
    	System.out.println("Can not move the location provided");
    }
}