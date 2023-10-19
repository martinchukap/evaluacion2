
from django.contrib import admin
from django.urls import path

from primerapp.views import *
from segundapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("juguetes/", juguetes),
    path("electronica/", electronica),
    path("ropa/", ropa),


    path("chile/", chile),
    path("argentina/", argentina),
    path("brasil/", brasil),
]
