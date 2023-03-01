from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Store, Part, Inventory

@login_required
def index(request):  
  return render(request, 'pages/index.html')


def userLogout(request):
  logout(request)
  return redirect('/')


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


def parts(request):
  parts = Part.objects.all()
  return render(request, 'pages/parts.html', {"parts":parts})


def addPart(request):
  sap_code=request.POST['txtCodeSap']
  sup_code=request.POST['txtCodeSup']
  description=request.POST['txtNamePart']

  part=Part.objects.create(sap_code=sap_code, sup_code=sup_code, description=description)
  return redirect('/parts')


def partEdition(request, sap_code):
  part = Part.objects.get(sap_code=sap_code)
  return render(request, "partEdition.html", {"part":part})


def editPart(request):
  sap_code=request.POST['txtSapCode']
  sup_code=request.POST['txtSupCode']
  description=request.POST['txtNamePart']

  part = Part.objects.get(sap_code=sap_code)
  part.sup_code = sup_code
  part.description = description
  part.save()
  return redirect('/parts')


def erasePart(request, sap_code):
  part = Part.objects.get(sap_code=sap_code)
  part.delete()
  return redirect('/parts')


def inventories(request):
  inventories = Inventory.objects.all()
  return render(request, 'pages/inventories.html', {"inventories":inventories})


def addInventory(request):
  qty = request.POST['nmbQty']
  part_id = request.POST['txtCodeSap']
  store_id = request.POST['txtCode']
  min = request.POST['nmbMin']
  order = request.POST['nmbOrder']
  max = request.POST['nmbMax']

  inventory = Inventory.objects.create(qty=qty, part_id=part_id, store_id=store_id, min=min, order=order, max=max)
  return redirect('/inventories')


def inventoryEdition(request, id):
  inventory = Inventory.objects.get(id=id)
  return render(request, "inventoryEdition.html", {"inventory":inventory})


def editInventory(request):
  id=request.POST['nmbId']
  qty = request.POST['nmbQty']
  part_id = request.POST['txtCodeSap']
  store_id = request.POST['txtCode']
  min = request.POST['nmbMin']
  order = request.POST['nmbOrder']
  max = request.POST['nmbMax']

  inventory = Inventory.objects.get(id=id)
  inventory.qty = qty
  inventory.part_id = part_id
  inventory.store_id = store_id
  inventory.min = min
  inventory.order = order
  inventory.max = max
  inventory.save()
  return redirect('/inventories')


def eraseInventory(request, id):
  inventory = Inventory.objects.get(id=id)
  inventory.delete()
  return redirect('/inventories')