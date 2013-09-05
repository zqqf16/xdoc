angular.module('doc.ui-ace', ['ui.ace'])
  .controller('AceCtrl', ['$scope', '$http', function ($scope, $http) {
	  $http.get('/raw/example.md').success(function(data) {
		  $scope.aceModel = data.content;
		  $scope.title = data.title;
	  });
  }])
;
