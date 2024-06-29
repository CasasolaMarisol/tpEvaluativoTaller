from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Persona  # Importar el modelo Persona
from myapp.forms import PersonaForm  # Importar el formulario PersonaForm

def ver_personas(request):
    personas = Persona.objects.all()
    return render(request, 'ver_personas.html', {'personas': personas})

def agregar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_personas')  # Redirige a la vista de ver personas después de agregar
    else:
        form = PersonaForm()
    
    return render(request, 'agregar_persona.html', {'form': form})

def editar_persona(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)

    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('ver_personas')  # Redirige a la vista de ver personas después de editar
    else:
        form = PersonaForm(instance=persona)
    
    return render(request, 'editar_persona.html', {'form': form})

def eliminar_persona(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    
    if request.method == 'POST':
        persona.delete()
        return redirect('ver_personas')  # Redirige a la vista de ver personas después de eliminar
    
    return render(request, 'confirmar_eliminar_persona.html', {'persona': persona})
