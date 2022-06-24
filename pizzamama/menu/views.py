from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza


def index(request):
   ''' pizzas = Pizza.objects.all()
    pizza_names_prices = [pizza.nom + " : " + str(pizza.prix) + "€"for pizza in pizzas]
    pizza_names_prices_str = ", ".join(pizza_names_prices)
    return HttpResponse("Les pizzas :" + pizza_names_prices_str)'''
   pizzas = Pizza.objects.all().order_by("prix")
   return render(request, 'menu/index.html', {'pizzas': pizzas})