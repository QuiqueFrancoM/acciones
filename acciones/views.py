from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import acciones, persona
from .forms import AccionesForm
def home(request):
    return http.HttpResponse("Página Raiz del proyecto")
def index(request):
    if request.method == 'POST':
        form = AccionesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return HttpResponse("<h1>Acción guardada!</h1>")
        return HttpResponse("<h1>Acción no guardada!</h1>")
    else:
        form = AccionesForm()
        return render(request, 'acciones/formato_dummie.html', {"form":form})

def lista_acciones(request):
    #return HttpResponse("<h1>Lista de acciones</h1>")
    Lacciones = acciones.objects.all().order_by('prioridad')
    return render(request, 'acciones/ListaAcciones2.html', {'Lacciones': Lacciones})

def accion_numero(request, id):
    accionN = acciones.objects.get(pk = id)
    return render(request, 'acciones/accionNo.html', context={
        'id':id,
        'accionN':accionN})

def accion_nombre(request, nombre):
    return HttpResponse("<h1>Acción con slug "+ nombre+ "</h1>")
