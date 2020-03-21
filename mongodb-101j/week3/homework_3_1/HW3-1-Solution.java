import com.mongodb.BasicDBList;
import com.mongodb.BasicDBObject;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.DBObject;
import com.mongodb.MongoClient;
import com.mongodb.MongoClientURI;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;

import java.io.IOException;
import java.util.List;

import static com.mongodb.client.model.Filters.eq;


/**
 * Drop the lowest score for students in a data set.
 */
public class HW3-1-Solution{
  public static void main(final String[] args) {
    MongoClient client = new MongoClient();
    MongoDatabase schoolDB = client.getDatabase("school");
    MongoCollection<Document> students = schoolDB.getCollection("students");

    // Iterate through the students and repair them.
    MongoCursor<Document> cursor = students.find().iterator();
    try {
      while (cursor.hasNext()) {
        Document student = cursor.next();
        List<Document> scores = (List<Document>) student.get("scores");
        // Now find the lowest homework score.
        Document minScoreObj = null;
        double minScore = Double.MAX_VALUE;  // Minimum score value.

        for (Document scoreDocument : scores) {
          // The array contains documents with "type" and "score".
          double score = scoreDocument.getDouble("score");
          String type = scoreDocument.getString("type");

          if (type.equals("homework") && score < minScore) {
            minScore = score;
            minScoreObj = scoreDocument; // this is the lowest score obj
          }
        }

        // Remove the lowest score.
        if (minScoreObj != null) {
          scores.remove(minScoreObj);   // remove the lowest
        }

        // replace the scores array for the student
        students.updateOne(eq("_id", student.get("_id")),
                   new Document("$set", new Document("scores", scores)));
      }
    } finally {
      cursor.close();
    }

    client.close();
  }
}