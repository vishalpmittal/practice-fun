'use strict';

angular.module('confusionApp')

        .controller('MenuController', ['$scope', 'menuFactory', function($scope, menuFactory) {
            
            $scope.tab = 1;
            $scope.showMenu = false;
            $scope.filtText = '';
            $scope.showDetails = false;
            $scope.message = "Loading...";
            $scope.dishes=menuFactory.getDishes().query(
                function(response){
                    $scope.dishes = response;
                    $scope.showMenu = true;
                },
                function(response){
                    $scope.message = "Error: " + response.status + " " + response.statusText;
                }
            );
            

                        
            $scope.select = function(setTab) {
                $scope.tab = setTab;
                
                if (setTab === 2) {
                    $scope.filtText = "appetizer";
                }
                else if (setTab === 3) {
                    $scope.filtText = "mains";
                }
                else if (setTab === 4) {
                    $scope.filtText = "dessert";
                }
                else {
                    $scope.filtText = "";
                }
            };

            $scope.isSelected = function (checkTab) {
                return ($scope.tab === checkTab);
            };
    
            $scope.toggleDetails = function() {
                $scope.showDetails = !$scope.showDetails;
            };
        }])

        .controller('ContactController', ['$scope', function($scope) {

            $scope.myfeedback = {mychannel:"", firstName:"", lastName:"", agree:false, email:"" };
            
            var channels = [{value:"tel", label:"Tel."}, {value:"Email",label:"Email"}];
            
            $scope.channels = channels;
            $scope.invalidChannelSelection = false;
                        
        }])

        .controller('FeedbackController', ['$scope', 'feedbackFactory', function($scope,feedbackFactory) {
           // $scope.feedback=feedbackFactory.getFeedback().get();
            $scope.sendFeedback = function() {
                
                console.log($scope.myfeedback);
                
                if ($scope.myfeedback.agree && ($scope.myfeedback.mychannel == "")) {
                    $scope.invalidChannelSelection = true;
                    console.log('incorrect');
                }
                else {
                    $scope.invalidChannelSelection = false;
                    feedbackFactory.getFeedback().save($scope.myfeedback);
                    $scope.myfeedback = {mychannel:"", firstName:"", lastName:"", agree:false, email:"" };
                    $scope.myfeedback.mychannel="";
                    
                    $scope.feedbackForm.$setPristine();
                    console.log($scope.myfeedback);
                }
            };
        }])

        .controller('DishDetailController', ['$scope', '$stateParams', 'menuFactory', function($scope, $stateParams, menuFactory) {
            
            
            $scope.showDish = false;
            $scope.message = "Loading...";
            $scope.dish=menuFactory.getDishes().get({id:parseInt($stateParams.id,10)})
            .$promise.then(
                 function(response){
                                $scope.dish = response;
                                $scope.showDish = true;
                            },
                            function(response) {
                                $scope.message = "Error: "+response.status + " " + response.statusText;
                            }
            );
            
            
            
        }])

        .controller('DishCommentController', ['$scope', 'menuFactory', function($scope, menuFactory) {
            
            $scope.mycomment = {rating:5, comment:"", author:"", date:""};
            
            $scope.submitComment = function () {
                
                $scope.mycomment.date = new Date().toISOString();
                console.log($scope.mycomment);
                
                $scope.dish.comments.push($scope.mycomment);
                menuFactory.getDishes().update({id:$scope.dish.id},$scope.dish);
                $scope.commentForm.$setPristine();
                
                $scope.mycomment = {rating:5, comment:"", author:"", date:""};
            };
        }])

        // implement the IndexController and About Controller here
        .controller('AboutController',['$scope','corporateFactory',function($scope, corporateFactory){
                $scope.message = "Loading...";
                $scope.showInfo = false;
                $scope.leadership= corporateFactory.getLeaders().query(
                function(response){
                    $scope.dishes = response;
                    $scope.showInfo = true;
                },
                function(response){
                    $scope.message = "Error: " + response.status + " " + response.statusText;
                });
                
        }])
        
        .controller('IndexController',['$scope','menuFactory','corporateFactory', function($scope,menuFactory,corporateFactory){
            
                $scope.showDish = false;
                $scope.message = "Loading...";
                $scope.promotion = menuFactory.getPromotion().get({id:0});
                
            
                $scope.dishHome = menuFactory.getDishes().get({id:0})
                .$promise.then(
                            function(response){
                                $scope.dishHome = response;
                                $scope.showDish = true;
                            },
                            function(response) {
                                $scope.message = "Error: "+response.status + " " + response.statusText;
                            }
                        );
                $scope.leaderHome= corporateFactory.getLeaders().get({id:0});
                
                
        }])

;
