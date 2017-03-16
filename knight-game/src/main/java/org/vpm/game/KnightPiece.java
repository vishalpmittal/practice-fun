/*
* Author: Vishal Mittal
* Date: 06/14/2014, Saturday
*
*/

package org.vpm.game;

import java.util.ArrayList;
import java.util.List;

public class KnightPiece implements Piece{
	CSquare location;
	ChessBoard board = null;

	public KnightPiece(CSquare knight_loc, ChessBoard board) {
		if(knight_loc == null)
			throw new IllegalArgumentException("Knights base location can not be Null");
		else if(board == null)
			throw new IllegalArgumentException("Board object can not be Null");
		else if(!board.hasSquare(knight_loc))
			throw new IllegalArgumentException("Invalid Location : "+ knight_loc);
		this.board = board;
		this.location = knight_loc;
	}

    /*
    * Moves Knight to new location. 
    * Throws InvalidMoveException if new location is not valid
    */	
	public void move(CSquare new_loc) throws InvalidMoveException{
		if (ChessBoard.size<3 ||
				(ChessBoard.size==3 && this.location.equals(2, 2))){
			throw new InvalidMoveException("No more moves feasible for Knight");
		}
		this.location = new_loc;
	}

    /*
    * Returns an ArrayList of Chess Square objects that are feasible 
    * to move to by Knight with respect to current position
    */	
	public List<CSquare> getPossibleMoves() throws NoMoreFeasibleMovesException{
		List<CSquare> moves = new ArrayList<CSquare>();
		if (ChessBoard.size<3 ||
				(ChessBoard.size==3 && this.location.equals(2, 2)))
			throw new NoMoreFeasibleMovesException("No more moves feasible for Knight");
		else{
			int x = this.location.x_cord;
			int y = this.location.y_cord;
			
			int [] x_array = {x+2, x+2, x-2, x-2, x+1, x-1, x+1, x-1};
			int [] y_array = {y+1, y-1, y+1, y-1, y+2, y+2, y-2, y-2};
			
			for (int a=0; a<=7; a++){
				CSquare squ = new CSquare(x_array[a], y_array[a]);
				if (board.hasSquare(squ)){
					moves.add(squ);
				}
			}
		}
		return moves;
	}		
}
