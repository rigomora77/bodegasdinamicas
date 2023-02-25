from django.shortcuts import render, redirect
from .models import Store

def index(request):
  return render(request, 'pages/index.html')

def stores(request):
  stockrooms = Store.objects.all()
  return render(request, 'pages/stores.html', {"stockrooms":stockrooms})

def addStore(request):
  code=request.POST['txtCode']
  name=request.POST['txtName']

  store=Store.objects.create(code=code, name=name)
  return redirect('/stores')


def storeEdition(request, code):
  store = Store.objects.get(code=code)
  return render(request, "storeEdition.html", {"store":store})


def editStore(request):
  code=request.POST['txtCode']
  name=request.POST['txtName']

  store = Store.objects.get(code=code)
  store.name = name
  store.save()
  return redirect('/stores')


def eraseStore(request, code):
  store = Store.objects.get(code=code)
  store.delete()
  return redirect('/stores')


