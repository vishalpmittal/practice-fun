knightGame
==========
knight game repository

Project Description:
====================
This program moves a chess piece "Knight" from a provided location on a "3 x 3" Chess Board to the far right hand bottom corner.
KNIGHT moves in specific way such as 2 steps in one direction and 1 step left/right.

Exceptions: 
-  If the KNIGHT starts position (2,2) then it cannot move further and throws a NoMoreFeasibleMovesException.
-  If the KNIGHT start position is not on board it throws IllegalArgumentException.

Checkout:
====================
cd your_work_dir

git clone -b master https://github.com/vishalpmittal/knightGame

cd knightGame

Execute:
====================
cd your_work_dir/knightGame

mvn install

Run program individually:
====================
mvn exec:java -Dexec.mainClass=“org.vpm.game.ChessGame" -Dexec.args="1 2"

mvn exec:java -Dexec.mainClass=“org.vpm.game.ChessGame" -Dexec.args="1 1"

Run tests:
====================
mvn test

Clean Environment:
====================
mvn clean

Note:
====================
Maven is using Junit 4.11 in as mentioned in the pom.xml file. Change the Junit version number in pom.xml, if you are using another version. That might also requre to change the imports in junit test programs.
