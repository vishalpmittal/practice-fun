var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// create a schema
var favoritesSchema = new Schema({
	  postedBy: {
	      type: mongoose.Schema.Types.ObjectId,
	      ref: 'User'
	  },
	  dishes:[{
          type: mongoose.Schema.Types.ObjectId,
          ref: 'Dish'
	  }]
	}, 
	{
    timestamps: true
	}
);

var Favorites = mongoose.model('Favorites', favoritesSchema);

module.exports = Favorites;
