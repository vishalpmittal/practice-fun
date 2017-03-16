/*
* Author: Vishal Mittal
* Date: 06/14/2014, Saturday
*/

package org.vpm.game;

import java.util.List;

public interface Piece {
	void move (CSquare new_loc) throws InvalidMoveException;
	
	List<CSquare> getPossibleMoves() throws NoMoreFeasibleMovesException;
}
