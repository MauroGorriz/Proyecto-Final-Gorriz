from django.shortcuts import render
from Appentrega.models import *
from django.http import *
from Appentrega.forms import form_bcen , form_btor , form_beng , form_registro, form_editar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import *

##Base es para tener siempre a mano el template por si necesito agregar algo nuevo.##
def base(request):
    return render(request, "Appentrega/Views 1.0/base.html")

def inicio(request):
    return render(request, "Appentrega/padre.html")

def sobremi(request):
    return render(request, "Appentrega/sobremi.html")

## Funciones login, registro, editar y logout

def inicio_sesion(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 

            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasena)

            if user is not None:
                login(request, user)

                return render(request, "Appentrega/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
           
        else:

            return render(request, "Appentrega/inicio.html", {"mensaje":"Los datos ingresados son incorrectos"})

    form = AuthenticationForm()

    return render(request, "Appentrega/Registro/login.html", {"form": form})

def registro_usuario(request):
    
    if request.method == 'POST':
        form = form_registro(request.POST)

        if form.is_valid():
            info=form.cleaned_data
            usuario = info['first_name'] 
            form.save()

            return render(request, "Appentrega/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
        
    else:
        form = form_registro()

    return render(request, "Appentrega/Registro/registro.html", {"form": form})

def editar_usuario(request):

    usuario_actual = request.user
    
    if request.method == 'POST':
        form = form_editar(request.POST)

        if form.is_valid():
            info=form.cleaned_data
            usuario_actual.first_name = info['first_name'] 
            usuario_actual.last_name = info['last_name'] 
            usuario_actual.email = info['email'] 
            usuario_actual.save()

            return render(request, "Appentrega/inicio.html", {"mensaje":f"Has actualizado tu perfil"})
        
    else:
        form = form_editar(initial={'first name':usuario_actual.first_name,
                                    'last name':usuario_actual.last_name,
                                    'email':usuario_actual.email,})

    return render(request, "Appentrega/Registro/editarusuario.html", {"form_e": form})

def cerrar_sesion(request):
    logout(request)
    return render(request, "Appentrega/Registro/cerrarsesion.html")


##Funciones de agregar bombas (Create)##
@login_required
def agregar_bcen(request):

    if request.method == "POST":

        nformu = form_bcen(request.POST)

        if nformu.is_valid():

            info_ok = nformu.cleaned_data

            Bomba_Cen = BCentri(
                modelo=info_ok["modelo"],
                materiales_carcaza=info_ok["materiales_carcaza"],
                materiales_voluta=info_ok["materiales_voluta"],
                presion=info_ok["presion"],
                caudal=info_ok["caudal"],
                altura=info_ok["altura"],
                temp=info_ok["temp"],
            )

            Bomba_Cen.save()

            return render(request, "Appentrega/padre.html")
    else:

        nformu = form_bcen()

    return render(request, "Appentrega/NuevaBCent.html", {"MiFormulario":nformu})

def agregar_btor(request):
    
    if request.method == "POST":

        nformu = form_btor(request.POST)

        if nformu.is_valid():

            info_ok = nformu.cleaned_data

            Bomba_tor = BTornillo(
                modelo=info_ok["modelo"],
                materiales_carcaza=info_ok["materiales_carcaza"],
                materiales_tornillo=info_ok["materiales_tornillo"],
                presion=info_ok["presion"],
                caudal=info_ok["caudal"],
                altura=info_ok["altura"],
                temp=info_ok["temp"],
            )

            Bomba_tor.save()

            return render(request, "Appentrega/padre.html")
    else:

        nformu = form_btor()
        
    return render(request, "Appentrega/NuevaBTor.html", {"MiFormulario2":nformu})

def agregar_beng(request):
    
    if request.method == "POST":

        nformu = form_beng(request.POST)

        if nformu.is_valid():

            info_ok = nformu.cleaned_data

            Bomba_eng = BEngranajes(
                modelo=info_ok["modelo"],
                materiales_carcaza=info_ok["materiales_carcaza"],
                materiales_engranajes=info_ok["materiales_engranajes"],
                presion=info_ok["presion"],
                caudal=info_ok["caudal"],
                altura=info_ok["altura"],
                temp=info_ok["temp"],
            )

            Bomba_eng.save()

            return render(request, "Appentrega/padre.html")
    else:

        nformu = form_beng()

    return render(request, "Appentrega/NuevaBEng.html",{"MiFormulario3":nformu})


##Funciones de buscar bombas (Read)##

@login_required
def busqueda(request):
    return render(request, "Appentrega/busqueda.html")

def buscar_modelo_bcen(request):

    if request.method=="GET":

        presion_dada = request.GET["presion"]
        resultados_modelos = BCentri.objects.filter(presion__icontains=presion_dada)
        return render(request, "Appentrega/resultadobusquedacen.html", {'DBusqueda1':resultados_modelos})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def buscar_modelo_btor(request):

    if request.method=="GET":

        presion_dada = request.GET["presion"]
        resultados_modelos = BTornillo.objects.filter(presion__icontains=presion_dada)
        return render(request, "Appentrega/resultadobusquedator.html", {'DBusqueda2':resultados_modelos})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def buscar_modelo_beng(request):

    if request.method=="GET":

        presion_dada = request.GET["presion"]
        resultados_modelos = BEngranajes.objects.filter(presion__icontains=presion_dada)
        return render(request, "Appentrega/resultadobusquedaeng.html", {'DBusqueda3':resultados_modelos})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

##Funciones de actualizar bombas (Update)##

def actualizar_bcen(request, bcen_id):

    bcen_elegida = BCentri.objects.get(id=bcen_id)

    if request.method == "POST":

        nformu = form_bcen(request.POST)

        if nformu.is_valid():

            info_ok = nformu.cleaned_data

            bcen_elegida.modelo = info_ok["modelo"]
            bcen_elegida.materiales_carcaza = info_ok["materiales_carcaza"]
            bcen_elegida.materiales_voluta = info_ok["materiales_voluta"]
            bcen_elegida.presion = info_ok["presion"]
            bcen_elegida.caudal = info_ok["caudal"]
            bcen_elegida.altura = info_ok["altura"]
            bcen_elegida.temp = info_ok["temp"]

            bcen_elegida.save()

            return render(request, "Appentrega/padre.html")
    else:

        nformu = form_bcen(initial = {"modelo":bcen_elegida.modelo,
                                      "materiales_carcaza":bcen_elegida.materiales_carcaza,
                                      "materiales_voluta":bcen_elegida.materiales_voluta,
                                      "presion":bcen_elegida.presion,
                                      "caudal":bcen_elegida.caudal,
                                      "altura":bcen_elegida.altura,
                                      "temp":bcen_elegida.temp})
        
    return render(request, "Appentrega/update_bcen.html", {"MiFormulario":nformu})

def actualizar_btor(request, btor_id):

    btor_elegida = BTornillo.objects.get(id=btor_id)

    if request.method == "POST":

        nformu = form_btor(request.POST)

        if nformu.is_valid():

            info_ok = nformu.cleaned_data

            btor_elegida.modelo = info_ok["modelo"]
            btor_elegida.materiales_carcaza = info_ok["materiales_carcaza"]
            btor_elegida.materiales_tornillo = info_ok["materiales_tornillo"]
            btor_elegida.presion = info_ok["presion"]
            btor_elegida.caudal = info_ok["caudal"]
            btor_elegida.altura = info_ok["altura"]
            btor_elegida.temp = info_ok["temp"]

            btor_elegida.save()

            return render(request, "Appentrega/padre.html")
    else:

        nformu = form_bcen(initial = {"modelo":btor_elegida.modelo,
                                      "materiales_carcaza":btor_elegida.materiales_carcaza,
                                      "materiales_voluta":btor_elegida.materiales_tornillo,
                                      "presion":btor_elegida.presion,
                                      "caudal":btor_elegida.caudal,
                                      "altura":btor_elegida.altura,
                                      "temp":btor_elegida.temp})
        
    return render(request, "Appentrega/update_btor.html", {"MiFormulario2":nformu})

def actualizar_beng(request, beng_id):

    beng_elegida = BEngranajes.objects.get(id=beng_id)

    if request.method == "POST":

        nformu = form_beng(request.POST)

        if nformu.is_valid():

            info_ok = nformu.cleaned_data

            beng_elegida.modelo = info_ok["modelo"]
            beng_elegida.materiales_carcaza = info_ok["materiales_carcaza"]
            beng_elegida.materiales_engranajes = info_ok["materiales_engranajes"]
            beng_elegida.presion = info_ok["presion"]
            beng_elegida.caudal = info_ok["caudal"]
            beng_elegida.altura = info_ok["altura"]
            beng_elegida.temp = info_ok["temp"]

            beng_elegida.save()

            return render(request, "Appentrega/padre.html")
    else:

        nformu = form_bcen(initial = {"modelo":beng_elegida.modelo,
                                      "materiales_carcaza":beng_elegida.materiales_carcaza,
                                      "materiales_voluta":beng_elegida.materiales_engranajes,
                                      "presion":beng_elegida.presion,
                                      "caudal":beng_elegida.caudal,
                                      "altura":beng_elegida.altura,
                                      "temp":beng_elegida.temp})
        
    return render(request, "Appentrega/update_beng.html", {"MiFormulario3":nformu})

##Funciones para eliminar bombas##

def eliminar_bcen(request, bcen_id):
    
    bcen_elegida = BCentri.objects.get(id=bcen_id)
    bcen_elegida.delete()

    return render(request, "Appentrega/padre.html")

def eliminar_btor(request, btor_id):
    
    btor_elegida = BTornillo.objects.get(id=btor_id)
    btor_elegida.delete()

    return render(request, "Appentrega/padre.html")

def eliminar_beng(request, beng_id):
    
    beng_elegida = BEngranajes.objects.get(id=beng_id)
    beng_elegida.delete()

    return render(request, "Appentrega/padre.html")