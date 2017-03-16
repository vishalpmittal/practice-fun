// grab the things we need
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var favoriteSchema = new Schema({
    postedBy: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User'
    },
    dishes: [{       
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Dish'
    }]
}, {
    timestamps: true
});

// make this available to our Node applications
module.exports = mongoose.model('Favorite', favoriteSchema);