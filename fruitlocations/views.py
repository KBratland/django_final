from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import json

from django.contrib.gis.geos import Point
from fruitlocations.models import FruitLocations
from fruitlocations.forms import AddFruit

# @login_required

def find_fruit(request):
    return render_to_response("fruitlocations/find_fruit.html")

# Take all data from FruitLocations model table and turn it into a json object to send to map via JS/AJAX (see find_fruit.js)
def ajax_get_fruit(request):
    if request.is_ajax() and request.method == "GET":
        fruits = FruitLocations.objects.all()
        fruit_markers = {}
        for object in fruits:
            fruit_markers[object.id] = {"fruit_variety": object.fruit_variety, "geom": object.geom}
        print(fruit_markers)
        return HttpResponse(json.dumps(fruit_markers), content_type="application/json")
    else:
        return 'Http404'


# Create add fruit form that takes spatial data from a marker on a map garnered through JS/AJAX (see add_fruit.js) and save to DB

def add_fruit(request):

    if request.method == 'POST':
        form = AddFruit(request.POST)
        if form.is_valid():
            new_point = FruitLocations()
            cd = form.cleaned_data
            coordinates = cd['coordinates'].split(',')
            new_point.geom = Point(float(coordinates[0]), float(coordinates[1]))
            new_point.fruit_variety = cd['fruit_variety']

            new_point.save()

            return render_to_response('fruitlocations/AddFruit_success.html')

        else:
            return render_to_response('fruitlocations/AddFruit_fail.html')

    else:
        form = AddFruit()

    token = {}
    token.update(csrf(request))
    token['form'] = AddFruit()

    return render_to_response('fruitlocations/add_fruit.html', token)