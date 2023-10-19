from django.shortcuts import render


# Create your views here.


def index(request):
    return render (request, 'templatesProductos/index.html')

def electronica(request):
    data = {
        "titulo": "Electónica",
        "producto1": "Mac",
        "producto2": "Celular",
        "producto3": "Chuto movil",
        'imagen' : 'imagenes/don_rene.jpg'
    }

    return render (request, 'templatesProductos/index.html', data)
    
def juguetes (request):
    data = {
        "titulo": "Jugetes",
        "producto1": "Pelota",
        "producto2": "Chuto",
        "producto3": "Arma",
        'imagen' : 'imagenes/don_rene.jpg'
    }
    return render (request, 'templatesProductos/index.html', data)

def ropa (request):
    data = {
        "titulo": "Ropa",
        "producto1": "Pantalon",
        "producto2": "Laba",
        "producto3": "Poleron",
        'imagen' : 'imagenes/don_rene.jpg'
    }
    return render (request, 'templatesProductos/index.html', data)