from django.shortcuts import render

# Create your views here.
def index(request):
    productos = [
        {"codigo":1,"nombre":"Alpiste pal Mauri","Precio":"$1.250","Stock":"Muchos"},
        {"codigo":2,"nombre":"Tung sahur figura","Precio":"$12.550","Stock":"Entre 1 y 10.000"},
        {"codigo":3,"nombre":"peo","Precio":"$10.250","Stock":"Más de uno"},
        {"codigo":4,"nombre":"chaya","Precio":"$11.250","Stock":"Suficientes"},
        ]
    return render(request, 'inicio/default.html', {"articulos":productos})