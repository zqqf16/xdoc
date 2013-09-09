var editor = angular.module('xdoc.editor', ['ui.ace']);

editor.controller('AceCtrler', ['$scope', '$http', function($scope, $http) {
	$scope.aceStyle = {'height': '1000px','weight':'800px'};
	$scope.aceHeight = '1000px';
	$http.get('/raw/example.md').success(function(data){
		$scope.aceModel = data.content;
		$scope.title = data.title;
	});

}]);

editor.directive('markdown', function () {
	var converter = new Showdown.converter();
	return {
		restrict: 'AE',
		link: function (scope, element, attrs) {
			scope.$watch(attrs.ngModel, function (newVal) {
				var html = converter.makeHtml(newVal);
				element.html(html);
			});
		}
	};
});
