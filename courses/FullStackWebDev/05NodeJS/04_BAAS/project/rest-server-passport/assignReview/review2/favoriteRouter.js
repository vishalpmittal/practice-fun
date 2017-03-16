var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

var Favorites = require('../models/favorites');
var Verify = require('./verify');

var favoriteRouter = express.Router();
favoriteRouter.use(bodyParser.json());

favoriteRouter.route('/')

// Populate before returning the favorites to the user
.get(Verify.verifyOrdinaryUser, function (req, res, next) {
    Favorites.find({
            "postedBy": req.decoded._doc._id
        })
        .populate('postedBy')
        .populate('dishes')
        .exec(function (err, favorite) {
            if (err) throw err;

            res.json(favorite);
        });
})

// Create documents and add dishes
.post(Verify.verifyOrdinaryUser, function (req, res, next) {
    Favorites.findOne({
        "postedBy": req.decoded._doc._id
    }, function (err, favorite) {
        if (favorite) {
            Favorites.create(req.body, function (err, favorite) {
                if (err) throw err;
                favorite.postedBy = req.decoded._doc._id;
                favorite.dishes.push(req.body._id);
                favorite.save(function (err, favorite) {
                    if (err) throw err;
                    res.json(favorite);
                });
            });

        } else {
            var index = favorite.dishes.indexOf(req.body._id);
            if (index > -1) { // already added
                var err = new Error();
                err.status = 401;
                return next(err);
            } else {
                favorite.dishes.push(req.body._id);
                favorite.save(function (err, favorite) {
                    if (err) throw err;
                    res.json(favorite);
                });
            }
        }
    });
})

// Delete the list of favorites corresponding to the user
.delete(Verify.verifyOrdinaryUser, function (req, res, next) {
    Favorites.remove({
        "postedBy": req.decoded._doc._id
    }, function (err, response) {
        if (err) throw err;
        res.json(response);
    });
});

// Delete the specified dish
favoriteRouter.route('/:favoriteId')
    .delete(Verify.verifyOrdinaryUser, function (req, res, next) {
        Favorites.findOne({
            postedBy: req.decoded._doc._id
        }, function (err, favorite) {
            if (err) throw err;
            if (favorite) {
                var index = favorite.dishes.indexOf(req.params.favoriteId);
                if (index > -1) {
                    favorite.dishes.splice(index, 1);
                }
                favorite.save(function (err, favorite) {
                    if (err) throw err;
                    res.json(favorite);
                });
            } else { // favorite doesn't exist
                var err = new Error();
                err.status = 401;
                return next(err);
            }
        });
    });


module.exports = favoriteRouter;