var express = require('express');
var morgan = require('morgan');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

var Favorites = require('../models/favorites');
var Verify = require('./verify');

var favRouter = express.Router();
favRouter.use(bodyParser.json());

favRouter.route('/')
    .get(Verify.verifyOrdinaryUser, function (req, res, next) {
        Favorites.findOne({
                postedBy: req.decoded._doc._id
            })
            .populate('postedBy')
            .populate('dishes')

        .exec(function (err, favorites) {
            if (err) throw err;
            res.json(favorites);
        });
    })

.post(Verify.verifyOrdinaryUser, function (req, res, next) {
    Favorites.findOne({
        postedBy: req.decoded._doc._id
    }, function (err, userFav) {
        if (err) throw err;

        // Check if the req body does contain a dish id
        if (req.body._id != null) {
            // If the user already exists in favorites collection
            if (userFav != null) {
                if (userFav.dishes.indexOf(req.body._id) > -1) {
                    // if the favorite dish already in user list
                    console.log("Item " + req.body._id + " already exists in fav's list of user: " + userFav.postedBy);
                    res.json(userFav);
                } else {
                    // new dish item for user push and save
                    userFav.dishes.push(req.body._id);

                    userFav.save(function (err, userFav) {
                        if (err) throw err;
                        console.log("added dish item " + req.body._id + " in favorites for user " + userFav.postedBy);
                        res.json(userFav);
                    });
                }

                // New user for favorites
            } else {
                newUserFavObj = {
                    postedBy: req.decoded._doc._id,
                    dishes: [req.body._id]
                };

                Favorites.create(newUserFavObj, function (err, userFav) {
                    if (err) throw err;
                    console.log("Created new favorites for user: " + userFav.postedBy + " and added favorite item " + req.body._id);
                    res.json(userFav);
                });
            }
            // if req body does not contain id just return current json
        } else {
            console.log("No dish id provided in the request")
            res.json(userFav);
        }
    });
})

.delete(Verify.verifyOrdinaryUser, function (req, res, next) {
    Favorites.findOneAndRemove({
        postedBy: req.decoded._doc._id
    }, function (err, resp) {
        if (err) throw err;
        console.log("removed favorite list for user "+ req.decoded._doc._id);
        res.json(resp);
    });
});

favRouter.route('/:dishObjId')
    .delete(Verify.verifyOrdinaryUser, function (req, res, next) {
        Favorites.findOne({
            postedBy: req.decoded._doc._id
        }, function (err, userFav) {
            if (err) throw err;

            // If the user already exists in favorites collection
            if (userFav != null) {

                // find the index of item 
                var index = userFav.dishes.indexOf(req.params.dishObjId);

                if (index > -1) {
                    userFav.dishes.splice(index, 1);

                    userFav.save(function (err, userFav) {
                        if (err) throw err;
                        console.log("removed dish item " + req.params.dishObjId + " from favorites for user " + userFav.postedBy);
                        res.json(userFav);
                    });
                } else {
                    console.log("dish item " + req.params.dishObjId + " does not exists in favorites for user " + userFav.postedBy);
                    res.json(userFav);
                }

                // user does not exists
            } else {
                console.log("User favorite list does not exists")
                res.json(userFav);
            }
        });
    });

module.exports = favRouter;