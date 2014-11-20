/**
 * Created by student on 11/19/14.
 */
$(document).ready(function(){
    var map = L.map('map').setView([45.52, -122.68], 13);

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(map);

    $getJSON(response_data)

});