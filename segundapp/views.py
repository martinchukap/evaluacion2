from django.shortcuts import render

# Create your views here.


def paises(request):
    return render (request, 'templatesProductos/paises.html')

def chile(request):
    data = {
        "pais": "Pais: Chile",
        "dato1": "Comida tipica: Empanada",
        "dato2": "Baile tipico: Cueca",
        "dato3": "Presidente: Gabriel Boric",
        'imagen' : 'imagenes/xchi.png'
    }

    return render (request, 'templatesProductos/paises.html', data)
    
def argentina (request):
    data = {
        "pais": "Pais: Argentina",
        "dato1": "Comida tipica: Asado",
        "dato2": "Baile tipico: Tango",
        "dato3": "Presidente: Alberto Ferndaez",
        'imagen' : 'imagenes/ag.png'
    }
    return render (request, 'templatesProductos/paises.html', data)

def brasil (request):
    data = {
        "pais": "Pais: Brasil",
        "dato1": "Comida tipica: Sarapatel",
        "dato2": "Baile tipico: Zamba",
        "dato3": "Presidente: Luiz Inácio lula",
        'imagen' : 'imagenes/bra.jpg'
    }
    return render (request, 'templatesProductos/paises.html', data)