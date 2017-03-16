var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

var Favorites = require('../models/favorites');
var Verify = require('./verify');

var favRouter = express.Router();
favRouter.use(bodyParser.json());
favRouter.route('/')
    .get(Verify.verifyOrdinaryUser, function(req,res,next) {
        Favorites.find({postedBy: req.decoded._doc._id})
            .populate('postedBy')
            .populate('dishes')
            .exec(function (err, fav) {
                if (err) throw err;
                res.json(fav);
            });
    })
    .post(Verify.verifyOrdinaryUser, function(req,res,next){
        if (req.body._id) 
            Favorites.findOneAndUpdate({postedBy: req.decoded._doc._id}, {$addToSet:{dishes:req.body._id}},{upsert:true, new:true})
                .exec(function(err,resp) {
                    if (err) throw err;
                    res.json(resp); 
                });
    })
    .delete(Verify.verifyOrdinaryUser, function(req,res,next) {
        Favorites.findOneAndUpdate({postedBy: req.decoded._doc._id},{$set:{dishes:[]}},{new:true})
            .exec(function (err, resp) {
                if (err) throw err;
                res.json(resp);
            });
    });
favRouter.route('/:dishId')
    .delete(Verify.verifyOrdinaryUser, function(req,res,next) {
        Favorites.findOneAndUpdate({postedBy: req.decoded._doc._id},{$pull:{dishes:req.params.dishId}},{new:true})
            .exec(function(err,resp) {
                if (err) throw err;
                res.json(resp);
            });
    });

module.exports = favRouter;