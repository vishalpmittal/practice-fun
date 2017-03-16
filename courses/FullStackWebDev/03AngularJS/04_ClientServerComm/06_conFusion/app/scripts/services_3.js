'use strict';

angular.module('confusionApp')
        .constant("baseURL","http://localhost:3000/")
        .service('menuFactory', ['$resource','baseURL',function($resource,baseURL) {
    
            
            
    
                this.getDishes = function(){
                    
                    return $resource(baseURL+"dishes/:id",null,{'update':{method:'PUT'}});
                    
                };
    
                
    
                // implement a function named getPromotion
                this.getPromotion =  function(){
                    return $resource(baseURL+"promotions/:id");
                };
                // that returns a selected promotion.
    
                        
        }])

        .factory('corporateFactory', ['$resource','baseURL',function($resource,baseURL) {
    
            var corpfac = {};
    
            
     
            // Implement two functions, one named getLeaders,
            corpfac.getLeaders = function(){
                return $resource(baseURL+"leadership/:id");
            };
            // the other named getLeader(index)
            
            // Remember this is a factory not a service
    
            return corpfac;
        }])

        .factory('feedbackFactory',['$resource','baseURL',function($resource,baseURL){
            var feedback = {};
            feedback.getFeedback = function(){
                return $resource(baseURL+"feedback/:id");
            };
            
            return feedback;
        }])

;
