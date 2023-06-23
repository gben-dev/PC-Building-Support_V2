from django.shortcuts import render, redirect
from .models import Ensamble
from .forms import EnsambleForm, RegistroForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def hardware(request):
    return render(request, 'app/hardware.html')

def armar_tu_pc(request):
    return render(request, 'app/armar_tu_pc.html')

def ensambles(request):
    if request.method == 'POST':
        form = EnsambleForm(request.POST)
        if form.is_valid():
            ensamble = form.save()  # Guardar el objeto ensamble
            return redirect('resultado')
    else:
        form = EnsambleForm()
    return render(request, 'app/ensambles.html', {'form': form})

def resultado(request):
    ensambles = Ensamble.objects.all()

    if request.method == 'POST':
        ensamble_id = request.POST.get('ensamble_id')
        ensamble = Ensamble.objects.get(id=ensamble_id)
        ensamble.delete()
        return redirect('resultado')

    return render(request, 'app/resultado.html', {'ensambles': ensambles})



def editar_ensamble(request, ensamble_id):
    ensamble = Ensamble.objects.get(id=ensamble_id)  # Obtener el ensamble por ID

    if request.method == 'POST':
        form = EnsambleForm(request.POST, instance=ensamble)
        if form.is_valid():
            form.save()
            return redirect('resultado')
    else:
        form = EnsambleForm(instance=ensamble)

    return render(request, 'app/editar_ensamble.html', {'form': form})

def eliminar_ensamble(request, ensamble_id):
    try:
        ensamble = Ensamble.objects.get(id=ensamble_id)
        ensamble.delete()
        messages.success(request, 'El registro se eliminó correctamente.')
    except Ensamble.DoesNotExist:
        messages.error(request, 'El registro no existe.')
    return redirect('resultado')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página principal después del inicio de sesión exitoso
        else:
            # Mostrar mensaje de error si las credenciales son inválidas
            error_message = 'Nombre de usuario o contraseña incorrectos.'
            return render(request, 'app/login.html', {'error_message': error_message})
    else:
        return render(request, 'app/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'app/registro.html', {'form': form})