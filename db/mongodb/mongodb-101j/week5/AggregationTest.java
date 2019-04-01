import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;
import java.util.ArrayList;
import java.util.List;

import static java.util.Arrays.asList;

public class AggregationTest {

    /*Get all states with total population > 10 million */
    public static void getStates(MongoCollection<Document> collection){
        List<Document> pipeline;

        pipeline = asList(new Document("$group", new Document("_id", "$state").append("totalPop", new Document("$sum", "$pop"))),
                new Document("$match", new Document("totalPop", new Document("$gte", 10000000))));

        List<Document> results = collection.aggregate(pipeline)
                .into(new ArrayList<Document>());

        for (Document cur : results) {
            System.out.println(cur.toString());
        }
    }

    /*Get all states with total population > 10 million */
    public static void getStatesUsingParser(MongoCollection<Document> collection){
        List<Document> pipeline;

        pipeline = asList(Document.parse("{$group:{_id:\"$state\",totalPop:{$sum:\"$pop\"}}}"),
                Document.parse("{$match:{totalPop:{$gte:10000000 }}}"));

        List<Document> results = collection.aggregate(pipeline)
                .into(new ArrayList<Document>());

        for (Document cur : results) {
            System.out.println(cur.toString());
        }
    }

    public static void main(String[] args) {
        MongoClient client = new MongoClient();
        MongoDatabase database = client.getDatabase("uszips");
        MongoCollection<Document> collection = database.getCollection("zips");
        getStates(collection);
        getStatesUsingParser(collection);
    }
}