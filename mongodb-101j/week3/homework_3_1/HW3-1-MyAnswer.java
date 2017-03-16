package com.mdb;

import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Vishal on 8/18/2015.
 */
public class HW3-1-MyAnswer{

    public static void main(String[] args) {
        MongoClient client = new MongoClient();
        MongoDatabase database = client.getDatabase("school");
        MongoCollection<Document> collection = database.getCollection("students");

        List< Document > all = collection
                .find()
                .into(new ArrayList<Document>());

        int id_pivot = -1;

        for (Document cur : all){

            int curr_id = cur.getInteger("_id");
            List<Document> all_cur_scores  = (List<Document>)cur.get("scores");

            double minScore = Double.MAX_VALUE;
            int removeScorePivot = -99;

            for (int i = 0; i < all_cur_scores.size(); i++){
                Document curr_score = all_cur_scores.get(i);
                if (curr_score.getString("type").equalsIgnoreCase("homework")){
                    double curr_hw_score = curr_score.getDouble("score");
                    if(curr_hw_score < minScore){
                        minScore = curr_hw_score;
                        removeScorePivot = i;
                    }
                }
            }

            all_cur_scores.remove(removeScorePivot);

            if (curr_id == 137){
                for (Document doc : all_cur_scores){
                    Helper.printJson(doc);
                }
            }
            collection.updateOne(new Document("_id", curr_id), new Document("$set", new Document("scores", all_cur_scores)));
        }
    }
}
