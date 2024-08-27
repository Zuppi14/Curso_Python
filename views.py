from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .forms import ProductoForm
from .models import Producto



# Create your views here.

#Productos/

def index(request):
    productos = Producto.objects.all().values()
    return render (
        request,
        "index.html",
        context={"productos": productos}
    )

def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto = Producto.objects.get(id=producto_id)

    return render(
        request, 
        "detalle.html", 
        context={"producto": producto})


def formulario(request):
    form = ProductoForm()

    return render(
        request,
        "producto_form.html",
        {"form": form}
    )
    