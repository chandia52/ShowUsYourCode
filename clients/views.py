from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse

from clients.forms import LoginUserForm,CreateUserForm,EditUserForm,EditPasswordForm,ProyectoForm
from django.shortcuts import get_object_or_404
from .models import Proyecto

from django.urls import reverse_lazy,reverse

from django.contrib.auth import logout as logout_django,update_session_auth_hash,authenticate,login as login_django

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from django.views.generic import View,CreateView,UpdateView



""""Class"""
    
class LoginClass(View):
    form = LoginUserForm()
    message = None
    template = "clients/login.html"
    

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return render(request,self.template,self.get_context())
    
    def post(self,request,*args,**kwargs):
        username_post = request.POST['username']
        password_post = request.POST['password']
        user = authenticate( username = username_post , password = password_post)
        if user is not None:
            login_django(request,user)
            return redirect("home")  
        else:
            message = "User o Password incorrecto" 
        return render(request,self.template,self.get_context())
    
    def get_context(self):
        return {"form":self.form,"message":self.message}
    

class CreateClass(CreateView):
    success_url = reverse_lazy("client:login")
    template_name = "clients/create.html"
    model = User
    form_class = CreateUserForm

    def form_valid(self,form):
        self.object = form.save(commit = False)
        self.object.set_password(self.object.password)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url()) 
    
class EditClass(UpdateView,LoginRequiredMixin,SuccessMessageMixin):
    model = User
    template_name = "clients/edit.html"
    success_url = reverse_lazy ("client:edit")
    form_class = EditUserForm
    success_messages = "Tus datos han sido actualizados con exito"
    def form_valid(self,request,*args,**kwargs):
        messages.success(self.request,self.success_messages)
        return super(EditClass,self).form_valid(request,*args,**kwargs)
    def get_object(self,queryset = None):
        return self.request.user
    
"""Functions"""
def edit_password(request):
    
    form = EditPasswordForm(request.POST or None)    
    if request.method == "POST":
        if form.is_valid():
            current_password = form.cleaned_data["password"]
            new_password = form.cleaned_data["new_password"]
            if authenticate(username = request.user.username,password = current_password):
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request,"Contraseña actualizada con exito!")
                update_session_auth_hash(request,request.user)
                return redirect("home")
                
            else:
                messages.error(request,"Su contraseña actual no es valida")
    context = {"form":form}
    return render(request,'clients/edit_password.html',context)

@login_required(login_url="client:login")
def logout(request):
    logout_django(request)
    return redirect('client:login')


@login_required
def crear_proyecto(request):
    if request.method == "POST":
        formulario = ProyectoForm(request.POST,request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            descripcion = data["descripcion"]
            imagen = data["imagen"]
            proyecto = Proyecto(nombre=nombre,descripcion=descripcion,imagen=imagen)  # lo crean solo en RAM
            proyecto.save()# Lo guardan en la Base de datos          
           # Redirecciono al home
            url_exitosa = reverse('home')  # instrumentos/guitarras/
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProyectoForm()
    return render(request,'clients/crear_proyecto.html',{'formulario': formulario})
