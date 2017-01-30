// Define the `phonecatApp` module
var phonecatApp = angular.module('phonecatApp', ['gantt',
    'gantt.table',
    'gantt.movable',
    'gantt.tooltips',
    'gantt.drawtask'
]);

// Define the `PhoneListController` controller on the `phonecatApp` module
phonecatApp.controller('PhoneListController', function PhoneListController($scope) {
    $scope.data = [
        {
          "name": "Milestones",
          "tasks": [
            {
              "name": "Kickoff",
              "from": "2016-10-07T03:30:00.000Z",
              "to": "2016-10-08T04:30:00.000Z"
            },
            {
              "name": "Concept approval",
              "from": "2016-10-18T12:30:00.000Z",
              "to": "2016-10-19T12:30:00.000Z"
            }
          ]
        }
    ]
    $scope.drawTaskFactory = function() {
        var newTask = {
            id: 5,
            name: 'New Task'
            // Other properties
        }

        return newTask;
    }

});