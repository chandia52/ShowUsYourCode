from django import forms
from django.contrib.auth.models import User
from .models import Proyecto
from django.core.files.images import ImageFile

"""Constants"""

ERROR_MESSAGES_USER = {
   "unique": "El nombre de usuario no está disponible, intenta con otro...",
   "invalid": "Ingresa un nombre de usuario válido...",
   "required": "El nombre de usuario es requerido..."
}
ERROR_MESSAGES_EMAIL = {
   "invalid": "Ingresa un correo electrónico válido...",
   "unique": "El correo electrónico no está disponible, intenta con otro..."
}

"""Functions"""

def must_be_gt(value_password):
    if len(value_password) < 3:
        raise forms.ValidationError("El password debe contener al menos 3 caracteres...")


class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'input_login',"id":"username_login"}))
    password = forms.CharField(max_length=20,widget= forms.PasswordInput(attrs={'class':'input_login',"id":"password_login"}))

class CreateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20,label="Nombre:",error_messages={"required":"El Nombre es requerido..."})
    last_name = forms.CharField(max_length=20,label="Apellido:",error_messages={"required":"El Apellido es requerido..."})
    username = forms.CharField(max_length=20,label="Nombre de Usuario:", error_messages=ERROR_MESSAGES_USER)
    password = forms.CharField(max_length=20,label="Contraseña:",widget= forms.PasswordInput())
    email = forms.CharField(label="Correo Electronico:",error_messages=ERROR_MESSAGES_EMAIL)

    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","password")

class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20,label="Nombre",error_messages={"required":"El Nombre es requerido..."})
    last_name = forms.CharField(max_length=20,label="Apellido",error_messages={"required":"El Apellido es requerido..."})
    username = forms.CharField(max_length=20,label="Nombre de Usuario", error_messages=ERROR_MESSAGES_USER)

    
    class Meta:
        model = User
        fields = ("first_name","last_name","username")

class EditPasswordForm(forms.Form):
    password = forms.CharField(max_length=20,label='Contraseña Actual', widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=20,label='Nueva Contraseña', widget=forms.PasswordInput(),validators=[must_be_gt])
    repeat_password = forms.CharField(max_length=20,label='Repetir Nueva Contraseña',  widget=forms.PasswordInput(),validators=[must_be_gt])

    def clean(self):
        clean_data = super(EditPasswordForm,self).clean()
        password1 = clean_data["new_password"]
        password2 = clean_data["repeat_password"]

        if password1 != password2:
            raise forms.ValidationError("Ambas contraseñas no son iguales")

class ProyectoForm(forms.ModelForm):
   
   class Meta:
        model = Proyecto
        fields = ("nombre","descripcion","imagen")
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 50})
        }