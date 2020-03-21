use photoshare

var rem_sunrises = db.images.find({'tags':'sunrises'}).count();
print ("total initial sunrises: " + rem_sunrises );

print("Adding index on images");
db.albums.ensureIndex({'images':1});

print("Iterating over images");
var cur = db.images.find();
var j=0;
while(cur.hasNext()){
    doc = cur.next();
    image_id = doc._id

    b = db.albums.find({images:image_id}).count()
    if(b==0){
        //delete it from images
        db.images.remove({_id:image_id})
        j++;
    }
}

var rem_sunrises = db.images.find({'tags':'sunrises'}).count();

print ("total removed was", j);
print ("total remaining sunrises: " + rem_sunrises );
