var app = angular.module('gifs', ["restangular"]);

app.config(function($interpolateProvider, $httpProvider, RestangularProvider){
  
    $interpolateProvider.startSymbol("[[");
    $interpolateProvider.endSymbol("]]");

    RestangularProvider.setBaseUrl('');

    });

app.controller('GifCtrl', function($scope, Restangular) {

  $scope.loadData = function(query){
    var url = 'api/?query='+$scope.query;
    var resource = Restangular.all(url);
        
    resource.getList().then(function(data){
        $scope.results = data[2];
    });
  }
});