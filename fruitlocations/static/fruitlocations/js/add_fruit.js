/**
 * Created by student on 11/18/14.
 */


$(document).ready(function(){
    //instantiate the map and add the initial marker which will eventually grab lat/long for locating point

    var map = L.map('map').setView([45.52, -122.68], 13);

    var marker = L.marker([45.52, -122.6]);

    marker.addTo(map);

    marker.bindPopup("<b>Add fruit tree</b><br>Click the location of the fruit tree on the map to add it to the database").openPopup();

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(map);

    // grab lat and long using a marker,
    function onMapClick(e) {

      var lat = e.latlng.lat;
      var lng = e.latlng.lng;

      // Every time when user click on map we want to delete previous marker and create new marker on the new position where the user clicked
      if (typeof marker != 'undefined') {
          map.removeLayer(marker);  // delete previous marker
          marker = L.marker([lat, lng]).addTo(map);  // add new marker
          marker.bindPopup("<b>Is your location right?</b><br>Click again to get a different location. Or double click the map to zoom in").openPopup(); // add instructional popup
      }
      else {
          marker = L.marker([lat, lng]).addTo(map);  // add new marker
      }

      // we want to pass value of lat long to input field with id 'coordinates'
      $('#coordinates').val(lng + ',' + lat)

    }

    // call the onMapClick function when user click on map, also call ajax request
    map.on('click', onMapClick);
});