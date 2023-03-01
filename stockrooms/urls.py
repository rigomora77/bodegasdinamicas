from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stores/', views.stores, name='stores'),
    path('addStore/', views.addStore),
    path('storeEdition/<code>', views.storeEdition),
    path('editStore/', views.editStore),
    path('eraseStore/<code>', views.eraseStore),
    path('parts/', views.parts, name='parts'),
    path('addPart/', views.addPart),
    path('partEdition/<sap_code>', views.partEdition),
    path('editPart/', views.editPart),
    path('erasePart/<sap_code>', views.erasePart),
    path('userLogout/', views.userLogout, name="userLogout"),
    path('inventories/', views.inventories, name='inventories'),
    path('addInventory/', views.addInventory),
    path('inventoryEdition/<id>', views.inventoryEdition),
    path('editInventory/', views.editInventory),
    path('eraseInventory/<id>', views.eraseInventory),
]
