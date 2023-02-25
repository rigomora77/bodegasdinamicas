from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stores/', views.stores, name='stores'),
    path('addStore/', views.addStore),
    path('storeEdition/<code>', views.storeEdition),
    path('editStore/', views.editStore),
    path('eraseStore/<code>', views.eraseStore)
]