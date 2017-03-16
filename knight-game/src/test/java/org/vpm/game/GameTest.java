package org.vpm.game;

import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import static org.junit.Assert.*;

public class GameTest {
    private static Throwable setupError = null;
	private static ChessBoard cboard = null;
	private static CSquare knight_base_loc = null;
	private static KnightPiece knight = null;
	private static ChessGame cg = null;
    
    @BeforeClass
    public static void setUp() {
        try {    		
    		cboard = new ChessBoard(3);    		
        } catch (Throwable t) {
            setupError = t;
        }
    }

    @AfterClass
    public static void cleanUp() throws Exception {
    }

    @Before
    public void setUpTest() throws Throwable {    	
        if (setupError != null) {
            throw setupError;
        }
    }
   
    public int run_game(int x, int y) throws Exception{
    	knight_base_loc = new CSquare(x, y);
		knight = new KnightPiece(knight_base_loc, cboard);
		cg = new ChessGame(cboard, knight);
		ChessGame.target = new CSquare(3, 3);
		return cg.play();
    }
    
    @Test
    public void positiveTests() throws Exception {
        assertTrue("Knight start at (1,1) test ", run_game(1,1)==4);
        assertTrue("Knight start at (1,2) test ", run_game(1,2)==1);
        assertTrue("Knight start at (1,3) test ", run_game(1,3)==6);
        assertTrue("Knight start at (2,1) test ", run_game(2,1)==1);
        assertTrue("Knight start at (2,3) test ", run_game(2,3)==3);
        assertTrue("Knight start at (3,1) test ", run_game(3,1)==2);
        assertTrue("Knight start at (3,2) test ", run_game(3,2)==3);
        assertTrue("Knight start at (3,3) test ", run_game(3,3)==0);
    }   
    
    @Test
    public void specialCaseTests() {
    	Throwable e = null;
    	try {
    		run_game(2,2);
    	}catch (Throwable ex) {
    		e = ex;
    	}
    	assertTrue(e instanceof NoMoreFeasibleMovesException);
    }   
        
    @Test
    public void negativeTests() {
    	Throwable e = null;
		try { run_game(-1,-1); }catch (Throwable ex) { e = ex; }
    	assertTrue(e instanceof IllegalArgumentException);    	
   
		try { run_game(0,0); }catch (Throwable ex) { e = ex; }
		assertTrue(e instanceof IllegalArgumentException);
		
		try { run_game(1,4); }catch (Throwable ex) { e = ex; }
		assertTrue(e instanceof IllegalArgumentException);
		
		try { run_game(5,4); }catch (Throwable ex) { e = ex; }
		assertTrue(e instanceof IllegalArgumentException);    	
    }
}
