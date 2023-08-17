from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurante, Critico
from .forms import RestauranteForm, CriticoForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required



def lista_restaurantes(request):
    restaurantes = Restaurante.objects.select_related('creado_por').all()
    return render(request, 'criticos/lista_restaurantes.html', {'restaurantes': restaurantes})

def lista_criticos(request):
    criticos = Critico.objects.all()
    return render(request, 'criticos/lista_criticos.html', {'criticos': criticos})



@login_required
def agregar_restaurante(request):
    if request.method == 'POST':
        form = RestauranteForm(request.POST)
        if form.is_valid():
            restaurante = form.save(commit=False)  
            restaurante.creado_por = request.user  
            restaurante.save() 
            return redirect('lista_restaurantes')
    else:
        form = RestauranteForm()
    return render(request, 'criticos/agregar_restaurante.html', {'form': form})



def agregar_critico(request):
    if request.method == 'POST':
        form = CriticoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_criticos')
    else:
        form = CriticoForm()
    return render(request, 'criticos/agregar_critico.html', {'form': form})


@login_required
def eliminar_restaurante(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, pk=restaurante_id)
    if request.method == 'POST':
        restaurante.delete()
        return redirect('lista_restaurantes')
    return render(request, 'criticos/eliminar_restaurante.html', {'restaurante': restaurante})



def detalle_restaurante(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, pk=restaurante_id)
    return render(request, 'criticos/detalle_restaurante.html', {'restaurante': restaurante})



@login_required
def editar_restaurante(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, pk=restaurante_id)
    if request.method == "POST":
        formulario = RestauranteForm(request.POST, instance=restaurante)

        if formulario.is_valid():
            formulario.save()

            url_exitosa = reverse('lista_restaurantes')
            return redirect(url_exitosa)
    else:  
        formulario = RestauranteForm(instance=restaurante)
    return render(
        request=request,
        template_name='criticos/formulario_restaurante.html',  
        context={'formulario': formulario},
    )



def mi_informacion(request):
    informacion = {
        'nombre': 'Santiago Nuñez Muñoz',
        'email': 'santiagonunez077@gmail.com',
        'descripcion': '¡Hola! Soy yo, y aquí tienes información sobre mí.',
    }
    return render(
        request,
        'criticos/mi_informacion.html',  
        {'informacion': informacion}
    )