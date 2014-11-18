/**
 * Created by student on 11/14/14.
 */

$(document).ready(function (){

    var map = L.map('map').setView([45.52, -122.68], 13);
//    var treeIcon = L.icon({
//        iconUrl: 'images/Tree_icon.png',
//        iconSize:     [38, 95],
//        iconAnchor:   [22, 94]
//    });

    var marker = L.marker([45.52, -122.6], {draggable: true});

    marker.addTo(map);

    marker.bindPopup("<b>Welcome to Urban Fruit Finder!</b><br>Please register to access the Fruit Finder.", id="popup").openPopup();

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 18
        }).addTo(map);

});