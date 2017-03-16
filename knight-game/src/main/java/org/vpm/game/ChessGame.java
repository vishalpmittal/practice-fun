/*
* Author: Vishal Mittal
* Date: 06/14/2014, Saturday
*
*/

package org.vpm.game;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ChessGame {
	ChessBoard cboard = null;
	KnightPiece knight = null;
	static CSquare target = null;
	List<CSquare> prev_loc = new ArrayList<CSquare>();
	static int turns = 0;

	public ChessGame(ChessBoard cboard, KnightPiece knight) {
		this.cboard = cboard;
		this.knight = knight;
		prev_loc.add(this.knight.location);
	}
    
    /*
    * Recursive method to keep moving Knight until it reaches target location 
    */
	public void knight_game(List<CSquare> curr_moves) throws Exception {
		System.out.println("Knight at: " + this.knight.location);
		if (knight.location.equals(target)) {
			return;
		} else {
			System.out.println("Knight can move to : " + curr_moves);
			if (curr_moves.contains(ChessGame.target)) {
				this.knight.move(target);
				ChessGame.turns += 1;

			} else {
				Iterator<CSquare> it = curr_moves.iterator();
				while (it.hasNext()) {
					CSquare x = it.next();
					if (!prev_loc.contains(x)) {
						this.knight.move(x);
						//System.out.println("Moved knight to :" + x);
						ChessGame.turns += 1;
						prev_loc.add(x);
						//System.out.println("Knight loc history : " + this.prev_loc);
						knight_game(this.knight.getPossibleMoves());
						break;
					}
				}
			}
		}
	}

	public int play() throws Exception {
		System.out.println("--------------------------------");
		System.out.println("Starting Game with base location :"
				+ this.knight.location);

		ChessGame.turns = 0;
		List<CSquare> poss_moves = null;

		poss_moves = this.knight.getPossibleMoves();
		knight_game(poss_moves);
		
		System.out.println("Knight at end: " + knight.location);
		System.out.println("Turns :" + ChessGame.turns);
		System.out.println("--------------------------------");
		return ChessGame.turns;
	}

	public static void main(String args[]) throws Exception {
		CSquare knight_base_loc = null;
		try {
			knight_base_loc = new CSquare(Integer.parseInt(args[0]),
					Integer.parseInt(args[1]));
		} catch (Exception e) {
			System.err.println("Usage: java ChessGame x y \n"
							+ "where x and y are the integer co-ordinates of Knights base location");
			System.exit(-1);
		}

		ChessBoard cboard = new ChessBoard(3);
		KnightPiece knight = new KnightPiece(knight_base_loc, cboard);

		ChessGame cg = new ChessGame(cboard, knight);
		ChessGame.target = new CSquare(3, 3);
		cg.play();
	}
}
