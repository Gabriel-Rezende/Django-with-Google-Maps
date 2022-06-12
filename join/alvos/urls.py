from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.AdicionarAlvoView.as_view(), name='adicionar_alvo'),
    path('editar/<int:pk>/', views.EditarAlvoView.as_view(), name='editar_alvo'),
    path('excluir/<int:pk>/', views.ExcluirAlvoView.as_view(), name='excluir_alvo'),
]
