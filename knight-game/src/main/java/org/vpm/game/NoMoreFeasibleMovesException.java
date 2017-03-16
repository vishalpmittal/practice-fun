/*
* Author: Vishal Mittal
* Date: 06/14/2014, Saturday
* If there is point where no more feasible moves are possible
* for a piece in the game, this exception is thrown
*/

package org.vpm.game;

@SuppressWarnings("serial")
public class NoMoreFeasibleMovesException extends Exception{

	public NoMoreFeasibleMovesException(String exc) {
    	super(exc);
    }
    
    public String getMessage(){
    	return super.getMessage();
    }
    
    public void printDescription(){
    	System.out.println("Knight at location 2,2 and can not make any further moves");
    }
}