from django.urls import path
from clients.views import LoginClass,logout,CreateClass,EditClass,edit_password,crear_proyecto

app_name="client"
urlpatterns = [
    path('login/',LoginClass.as_view(),name="login"),
    path('logout/',logout,name="logout"),
    path('create/',CreateClass.as_view(),name="create"),
    path('edit/',EditClass.as_view(),name="edit"),
    path('edit_password/',edit_password,name="edit_password"),
    path('create_project/',crear_proyecto,name="create_project")

    
]