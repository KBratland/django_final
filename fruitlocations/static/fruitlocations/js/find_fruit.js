/**
 * Created by student on 11/19/14.
 */

$(document).ready(function(){

/* make a function that recognizes an action in or on the DOM that starts the request for AJAX function to run, what data do I need to make AJAX function work
/* make the AJAX request: URL - trigger the python code to get hte JASON data (/fruitlocations/find_fruit), data that I want to 'GET'
/*make a function to 'POST' data in the success portion of the ajax*/
/* create custom marker which will represent fruits in layer 'layer_fruit' */
//    CustomMarker = L.Marker.extend({
//        options: {
//        iconURL: 'http://localhost:8000/fruitlocations/images/tree.png',
//        title: 'Click to see fruit attributes'
//        }
//    });



/* Get all fruits from DB and add them to layer:_fruit */
//    $.ajax({
//        url: "/fruitlocations/find_fruit/",
//        type: 'POST',
//        data: {'fruit_variety' = fruit_variety, 'coordinates' = coordinates},
//        success: function(response) {
//
//        var fruitLayer = L.geoJson().addTo(map);
//myLayer.addData(geojsonFeature);
//
//            var array_fruitmarkers =  [];
//            var fruit_layer =  makeLayer
//
//            function AddPointsToLayer() {
//                for (var i=0; i<fruit_markers.length; i++) {
//                    array_fruitmarkers[i].addTo(layer_fruit);
//                }
//            };
//
//
//
//            $.each(eval(response), function(key, val) {
//                //fields in JSON that were returned
//                var fields = val.fields;
//
//                // parse point field to get values of lat & lon
//                var regExp = /\(([^)]+)\)/;
//                var matches = regExp.exec(fields.geom);
//                var point = matches[1];
//                var lon=point.split(' ')[0];
//                var lat=point.split(' ')[1];
//
//                //function which creates and adds new markers
//                marker = new CustomMarker([lat, lon], {
//                    title: fields.name,
//                    opacity: 1.0
//                });
//                marker.bindPopup("<strong>Variety: </strong>" + fields.fruit_variety);
//                marker.addTo(map);
//                array_fruitmarkers.push(marker);
//            });
//
//            // add markers to layer and add it to map
//            AddPointsToLayer();
//        }
//    });

    /* create map object */
    var map = L.map('map').setView([45.52, -122.68], 13);

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(map);

    function getFruits () {
        $.ajax({
            "url": "/fruitlocations/ajax_get_fruit/",
            "method": "GET",
            "success": function () {
                console.log(data)
            }
        })
    }
    //event handler to send AJAX GET when the map loads in the DOM
    $(window).on("load", function () {
        getFruits()
    });
});