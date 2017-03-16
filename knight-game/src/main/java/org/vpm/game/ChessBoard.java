/*
* Author: Vishal Mittal
* Date: 06/14/2014, Saturday
*
*/

package org.vpm.game;

public class ChessBoard {
	public static int size;
	
	public ChessBoard(int size){
		if (size <1)
			throw new IllegalArgumentException
					("Chess Board size can not be less than 1");
		ChessBoard.size = size;
	}
    
    /*
    * Finds if the square fits inside the chess board or not
    */	
	public boolean hasSquare(CSquare square){
		if (square == null || 
				square.x_cord > size ||
				square.x_cord < 1 ||
				square.y_cord > size ||
				square.y_cord < 1 
				)
			return false;
		return true;
	}
}