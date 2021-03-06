from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('notes/', views.getNotes),
    path('notes/create/', views.createNotes),
    path('notes/<str:pk>/update/', views.updateNotes),
    path('notes/<str:pk>/delete/', views.deleterNote),
    path('notes/<str:pk>/', views.getNote),
]
