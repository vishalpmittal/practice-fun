var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

var Favorites = require('../models/favorites');
var Verify    = require('./verify');

var favoritesRouter = express.Router();
favoritesRouter.use(bodyParser.json());

favoritesRouter.route('/')
.get(Verify.verifyOrdinaryUser, function (req, res, next) {
  var userid = req.decoded._doc._id;
  console.log("userid = "+userid)
  // Return all favorites posted by this user
	Favorites.find({})
			.where("postedBy", userid)
			//- @NOTE video describing assignment does not show populating the
			// postedBy and dishes but the assignment instructions require it so
			// the 2 following lines are added to match instructions instead of 
			// video
	  	.populate("dishes")
	  	.populate("postedBy")
	  	//-
      .exec(function (err, favorite) {
	      if (err) throw err;
	      res.json(favorite);
  });
})

.post(Verify.verifyOrdinaryUser, function (req, res, next) {
  var userid = req.decoded._doc._id;
  var dishid = req.body._id;
  var existing_fav = null;
  console.log("userid = "+userid)
  console.log("dish id = "+dishid);
  console.log("Checking for existing favorite before creating new one");
	// Look for existing favorite first
  Favorites.findOne({"postedBy":userid})
  	.exec(function (err, fav) {
	    if (err) throw err;
	    if (fav) {
		    console.log(fav.dishes);
		    if (fav.dishes.indexOf(dishid) != -1) {
			    res.writeHead(200, {
			        'Content-Type': 'text/plain'
			    });   	
			  	res.end('This dish is already a favorite');
		    }
		    else {
		    	fav.dishes.push(dishid);	   
          fav.save(function (err, favorite) {
            if (err) throw err;
  			  	res.end('Added dish to existing favorite');
          });
		    }
	    }
	    else {
	      console.log('no match found, creating one');
	    	// This dish is not yet in the list of favorites, add it now
	    	Favorites.create({}, function (err, favorite) {
	            if (err) throw err;
	            favorite.dishes = [];
	            favorite.dishes.push(dishid);
	            favorite.postedBy = userid;
	            favorite.save(function (err, favorite) {
	              if (err) throw err;
	              console.log('Favorite added!');
	              res.end('Added the favorite with id: ' + dishid);
	          });
	        });	    	
	    }
	  });
})

.delete(Verify.verifyOrdinaryUser, function (req, res, next) {
  var userid = req.decoded._doc._id;
  Favorites.remove({"postedBy":userid}, function (err, resp) {
      if (err) throw err;
      res.json(resp);
  });
});

favoritesRouter.route('/:dishid')
.delete(Verify.verifyOrdinaryUser, function (req, res, next) {
  var userid = req.decoded._doc._id;
  Favorites.find({})
  	.where("postedBy",userid)
  	.$where("this.dishes.include(dishid)")
  	.exec(function (err, resp) {
        if (err) throw err;
        res.json(resp);
    });
});

module.exports = favoritesRouter;
