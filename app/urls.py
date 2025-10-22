from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('novo/', views.novo_aluno, name='novo_aluno'),
    path('aluno/<int:pk>/', views.detalhes_aluno, name='detalhes_aluno'),
    path('aluno/<int:pk>/editar/', views.editar_aluno, name='editar_aluno'),
    path('aluno/<int:pk>/excluir/', views.excluir_aluno, name='excluir_aluno'),
]