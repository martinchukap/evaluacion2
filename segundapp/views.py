from django.shortcuts import render

# Create your views here.


def paises(request):
    return render (request, 'templatesProductos/paises.html')

def chile(request):
    data = {
        "pais": "Chile",
        "dato1": "Empanada",
        "dato2": "Cueca",
        "dato3": "Gabriel Boric",
        'imagen' : 'imagenes/xchi.png'
    }

    return render (request, 'templatesProductos/paises.html', data)
    
def argentina (request):
    data = {
        "pais": "Argentina",
        "dato1": "Asado",
        "dato2": "Tango",
        "dato3": "Alberto Ferndaez",
        'imagen' : 'imagenes/ag.png'
    }
    return render (request, 'templatesProductos/paises.html', data)

def brasil (request):
    data = {
        "pais": "Brasil",
        "dato1": "Sarapatel",
        "dato2": "Zamba",
        "dato3": "Luiz Inácio lula",
        'imagen' : 'imagenes/bra.jpg'
    }
    return render (request, 'templatesProductos/paises.html', data)