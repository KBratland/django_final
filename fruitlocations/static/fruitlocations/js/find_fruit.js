/**
 * Created by student on 11/19/14.
 */

$(document).ready(function(){
    /* Define base layers */
    var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib='Map data © openstreetmap contributors';
    var osm = new L.TileLayer(osmUrl, {attribution: osmAttrib});

/* create new layer group */
    var layer_fruit = new L.LayerGroup();
    var array_fruitmarkers = new Array();

/* create custom marker which will represent fruits in layer 'layer_fruit' */
    CustomMarker = L.Marker.extend({
        options: {
        title: 'Click to see fruit attributes'
        }
    });

/* define function which adds markers from array to layer group */
    function AddPointsToLayer() {
        for (var i=0; i<array_fruitmarkers.length; i++) {
            array_fruitmarkers[i].addTo(layer_fruit);
        }
    }

/* Get all fruits from DB and add them to layer:_fruit */
    $.ajax({
        url: '/fruitlocations/add_fruit/',
        type: 'GET',
        success: function(response) {
            $.each(eval(response), function(key, val) {
                //fields in JSON that were returned
                var fields = val.fields;

                // parse point field to get values of lat & lon
                var regExp = /\(([^)]+)\)/;
                var matches = regExp.exec(fields.geom);
                var point = matches[1];
                var lon=point.split(' ')[0];
                var lat=point.split(' ')[1];

                //function which creates and adds new markers based on filtered values
                marker = new CustomMarker([lat, lon], {
                    title: fields.name,
                    opacity: 1.0
                });
                marker.bindPopup("<strong>Variety: </strong>" + fields.fruit_variety);
                marker.addTo(map);
                array_fruitmarkers.push(marker);
            });

            // add markers to layer and add it to map
            AddPointsToLayer();
        }
    });

    /* create map object */
    var map = L.map('map', {
        center: [45.52, -122.68],
        zoom: 7,
        fullscreenControl: true,
        fullscreenControlOptions: {
            position: 'topleft'
        },
        layers: [osm, layer_fruit]
    });

    var baseLayers = {
        "OpenStreetMap": osm
    };

    var overlays = {
        "FoundFruits": layer_fruit
    };

    L.control.layers(baseLayers, overlays).addTo(map);

});