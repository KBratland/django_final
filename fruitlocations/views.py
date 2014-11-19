from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.gis.geos import Point
from .models import FruitLocations
from .forms import AddFruit

#do a landing page with a form and a csrf token
#then have another url for handling the post
#then make the add fruit def be the fruit/add_fruit

# @login_required

# def load_current_fruit(request):


def add_fruit(request):

    if request.method == 'POST':
        form = AddFruit(request.POST)
        if form.is_valid():
            new_point = FruitLocations()
            cd = form.cleaned_data
            coordinates = cd['coordinates'].split(',')
            new_point.geom = Point(float(coordinates[0]), float(coordinates[1]))
            new_point.fruit_variety = cd['Fruit Variety']

            new_point.save()

            return render_to_response('AddFruit_success.html')

        else:
            return render_to_response('AddFruit_fail.html')

    else:
        form = AddFruit()

    token = {}
    token.update(csrf(request))
    token['form'] = AddFruit()

    return render_to_response('fruitlocations/add_fruit.html')