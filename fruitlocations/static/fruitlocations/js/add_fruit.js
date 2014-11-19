/**
 * Created by student on 11/18/14.
 */


$(document).ready(function(){
    var map = L.map('map').setView([45.52, -122.68], 13);
    var treeIcon = L.icon({
        iconUrl: 'http://localhost:8000/static/fruitlocations/images/tree.png',
        iconSize:     [46, 70],
        iconAnchor:   [17, 70],
        popupAnchor:  [8, -60]
    });

    var marker = L.marker([45.52, -122.6], {icon: treeIcon}, {draggable: true});

    marker.addTo(map);

    marker.bindPopup("<b>Add point</b><br>Drag the marker to your lcoation").openPopup();

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(map);

    function onMapClick(e) {
      var lat = e.latlng.lat;
      var lng = e.latlng.lng;

      // Every time when user click on map we want to delete previous marker and create new marker on the new position where the user clicked
      if (typeof marker != 'undefined') {
          map.removeLayer(marker);  // delete previous marker
          marker = L.marker([lat, lng], {icon: treeIcon}).addTo(map);  // add new marker
          marker.bindPopup("<b>Is your location right?</b><br>Click again to get a different location. Or double click the map to zoom in").openPopup();
      }
      else {
          marker = L.marker([lat, lng], {icon: treeIcon}).addTo(map);  // add new marker
      }

      // we want to pass value of lat long to input field with id 'coordinates'
      // note that we set that field as hidden because we don't want user to type the coordinates there. We want him to set marker on map
      $('#coordinates').val(lng + ',' + lat)
      // add the coordinates back to the map via ajax

    }

    // call the onMapClick function when user click on map, also call ajax request
    map.on('dragend', onMapClick);
});