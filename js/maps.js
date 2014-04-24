var geocoder;
var map;
var marker;

// Initializes the map.
function initialize () {
  geocoder = new google.maps.Geocoder();
  var latlng = new google.maps.LatLng(28.59899156770566, 77.2283935546875);
  var mapOptions = {
    zoom: 14,
    center: latlng
  }
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  google.maps.event.addListener(map, 'click', function(event) {
    addMarker(event.latLng);
  });

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      map.setCenter(new google.maps.LatLng(position.coords.latitude,
                                           position.coords.longitude));
    });
  }
}

// Locates an address and centers the map.
function codeAddress() {
  var address = document.getElementById('address').value;
  geocoder.geocode({'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      map.setCenter(results[0].geometry.location);
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
}

// Add a marker to the map and push to the array.
function addMarker(location) {
  if (!marker) {
    marker = new google.maps.Marker({
      animation: google.maps.Animation.DROP,
      draggable: true,
      position: location,
      map: map
    });
  } else {
    marker.setPosition(location);
  }
}

google.maps.event.addDomListener(window, 'load', initialize);
