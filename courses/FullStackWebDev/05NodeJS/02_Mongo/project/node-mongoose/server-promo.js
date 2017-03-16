var mongoose = require('mongoose'),
    assert = require('assert');

require('mongoose-currency').loadType(mongoose);
var Currency = mongoose.Types.Currency;

var Promotions = require('./models/promotions');

// Connection URL
var url = 'mongodb://localhost:27017/conFusion';
mongoose.connect(url);
var db = mongoose.connection;

db.on('error', console.error.bind(console, 'connection error:'));

db.once('open', function () {
    // we're connected!
    console.log("Connected correctly to server");

    // create a new promotion
    Promotions.create({
        name: 'Weekend Grand Buffet',
        image: 'images/buffet.png',
        price: '$19.99',
        description: 'Featuring . . .'
    }, function (err, promo) {
        if (err) throw err;
        console.log('Promotion created!');
        console.log(promo);

        var id = promo._id;

        // get all the Promotions
        setTimeout(function () {
            Promotions.findByIdAndUpdate(id, {
                    $set: {
                        description: 'Updated Test'
                    }
                }, {
                    new: true
                })
                .exec(function (err, promo) {
                    if (err) throw err;
                    console.log('Updated Promotion!');
                    console.log(promo);

                    db.collection('promotions').drop(function () {
                        db.close();
                    });
                });
        }, 3000);
    });
});