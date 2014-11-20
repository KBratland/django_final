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


def find_fruit(request):
    item_list = FruitLocations.Objects.all()
    output_list = []
    for item in item_list:
        output_item = {}
        output_item["geom"] = item.geom
        output_item["fruit_variety"] = item.fruit_variety
        output_list.append(output_item)

    return HttpResponse(json.dumps(response_data), content_type="application/json")

    # return render_to_response('fruitlocations/find_fruit.html')


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