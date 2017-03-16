var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var Verify    = require('./verify');

var Favorites = require('../models/favorites');

var favoriteRouter = express.Router();

favoriteRouter.route('/')
.get(Verify.verifyOrdinaryUser, function (req, res, next) 
{
    Favorites.find({})
        .populate('dishes.postedBy')
        .exec(function (err, favorite) 
        {
            if (err) throw err;
            res.json(favorite);
        });
})

.post(Verify.verifyOrdinaryUser, function (req, res, next) 
{
    Favorites.findOne ({postedBy:req.decoded._doc._id})
        .exec (function (err,favorite) 
        {
            if (err) throw err;
            if (favorite == null) 
            {
                var fav = new Favorites;
                fav.postedBy = req.decoded._doc._id;
                fav.dishes.push(req.body._id);
                fav.save(function (err,result)
                {
                    res.json(result);
                }); 
            } 
            else 
            {
                favorite.dishes.addToSet(req.body._id);
                favorite.save(function(err, result) 
                {
                    res.json(result);
                });
            }
        });
})

.delete(Verify.verifyOrdinaryUser, function (req, res, next) 
{
    Favorites.remove({}, function (err, resp) 
    {
        if (err) throw err;
        res.json(resp);
    });
});

favoriteRouter.route('/:dishObjectId')
.delete(Verify.verifyOrdinaryUser,function(req, res, next)
{
	var dishId = req.params.dishObjectId;	
	Favorites.findOneAndUpdate(
		{postedBy : req.decoded._doc._id}, 
		{$pull: {dishes: dishId} }, 
        { "new": true },
         function(err, favDish) 
         {
            if (err) throw err;
            console.log ( favDish);
            res.json(favDish);
	    }) ;
});
    
module.exports = favoriteRouter;