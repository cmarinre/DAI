# recetas/views.py

from django.shortcuts import  get_object_or_404, render, redirect
from recetas.models import Receta, Ingrediente
from .forms import RecetaForm
from django.contrib import messages
 

# Create your views here.

def index(request):
    return render(request, "inicio.html", {})

def detalle(request, pk):
    unareceta = Receta.objects.get(pk=pk)
    ingredientes = Ingrediente.objects.filter(receta = unareceta)
    return render(request, "detalle.html", {'unareceta' : unareceta, 'ingredientes': ingredientes})


 
def busqueda(request):

    if request.GET.get("searchInput") != "":
        filtrados = Receta.objects.filter(nombre = request.GET.get('searchInput'))
        if(filtrados!=None):
            return render(request, "listaRecetas.html", {'filtrados': filtrados})
    else:
        todos = Receta.objects.all()
        return render(request, "listaRecetas.html", {'filtrados': todos})
    


   
def post_new(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.add_message(request,  messages.SUCCESS, 'La receta ha sido guardada con éxito')
            return redirect('detalle', pk = post.pk)
    else:
        form = RecetaForm()
    return render(request, 'post_new.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Receta, pk=pk)
    if request.method=="POST":
        form = RecetaForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(request,  messages.SUCCESS, 'La receta ha sido editada con éxito')
            return redirect('detalle', pk = post.pk)
    else:
        form = RecetaForm(instance=post)
    return render(request, 'post_new.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Receta, pk=pk)
    Receta.objects.filter(pk=pk).delete()
    todos = Receta.objects.all()
    messages.add_message(request,  messages.SUCCESS, 'La receta ha sido eliminada con éxito')
    return render(request, 'listaRecetas.html', {'filtrados': todos})
