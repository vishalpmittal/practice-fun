package com.mdb;

import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Projections;
import com.mongodb.client.model.Sorts;
import org.bson.Document;
import org.bson.conversions.Bson;
import org.bson.types.ObjectId;

import java.util.ArrayList;
import java.util.List;

import static com.mongodb.client.model.Filters.gt;

/**
 * Created by Vishal on 8/18/2015.
 */
public class Homework2 {

    public static void main(String[] args) {
        MongoClient client = new MongoClient();
        MongoDatabase database = client.getDatabase("students");
        MongoCollection<Document> collection = database.getCollection("grades");

        Bson filter = new Document("type", "homework");
        Bson projection = new Document("_id",0);
        Bson sort_stu = new Document("student_id", 1).append("score", 1);

        List< Document > all = collection
                .find()
                .filter(filter)
                .sort(sort_stu)
                .into(new ArrayList<Document>());

        int id_pivot = -1;

        for (Document cur : all){
            Helper.printJson(cur);

            ObjectId obj_id = cur.getObjectId("_id");
            int curr_stud_id = cur.getInteger("student_id");

            if (id_pivot != curr_stud_id){
                System.out.println("going to remove the record with id" + curr_stud_id +"; "+ obj_id);
                collection.deleteOne(new Document("_id", obj_id));
                id_pivot = curr_stud_id;
            }
        }
    }
}
