from django.urls import path,include
from .import views

urlpatterns = [
    path('add/',views.add_author,name='add_author'),
    path('edit/<int:id>',views.edit_author,name='edit_author'),
]
