/*
* Author: Vishal Mittal
* Date: 06/14/2014, Saturday
*
* Chess Square class to encapsulate x and y co-ordinates of each square
*/

package org.vpm.game;

public class CSquare {
	int x_cord;
	int y_cord;

	public CSquare(int x, int y) {
		this.x_cord = x;
		this.y_cord = y;
	}
	
	/*
	 * Utility comparison method with co-ordinates
	 */
	public boolean equals(int x, int y){
		if(this.x_cord == x && this.y_cord == y)
			return true;
		return false;
	}
	
	/*
	 * 	(non-Javadoc)
	 * @see java.lang.Object#equals(java.lang.Object)
	 */
	@Override
	public boolean equals(Object o){
		boolean is_equal= false;
		if (o != null && o instanceof CSquare)
        {
			if (this.x_cord == ((CSquare)o).x_cord && this.y_cord == ((CSquare)o).y_cord) 
				is_equal = true;
        }
		return is_equal;		
	}
	
	/*
	 * (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString(){
		return "(" + this.x_cord +"," +this.y_cord+")";
	}
}