angular.module('app.controllers', [])
  
.controller('page1Ctrl', function($scope) {

})
   
.controller('page2Ctrl', function($scope) {



})
   
.controller('page3Ctrl', function($scope, $cordovaGeolocation) {

 





    var watchOptions = {
    frequency: 15 * 60 * 1000,
    timeout : 1 * 60 * 1000,
    enableHighAccuracy: false
    };
   $cordovaGeolocation
   .getCurrentPosition(watchOptions)
	
   .then(function (position) {
      var lat  = position.coords.latitude
      var long = position.coords.longitude
      alert(lat + '   ' + long)
      var myLatlng = new google.maps.LatLng(lat, long);

   var map = new google.maps.Map(document.getElementById('map'), {
          center: myLatlng,
          scrollwheel: false,
          zoom: 12
        });

      var marker = new google.maps.Marker({
        position: myLatlng,
        map: map,
        title: 'I am'
      });


   }, function(err) {
       alert(JSON.stringify(err));
      
   }); 

     

})
      
.controller('page4Ctrl', function($scope) {

})
   
.controller('page5Ctrl', function($scope) {

})
   
.controller('page6Ctrl', function($scope) {

})
   
.controller('page7Ctrl', function($scope) {

})
 
