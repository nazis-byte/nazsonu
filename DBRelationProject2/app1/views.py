from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PassportForm, PersonForm
from .models import PersonModel, PassportModel
# Create your views here.
def addPE(request):
    fr =PersonForm()
    return render(request, "addpe.html", {"form":fr})


def savePE(request):
    ano = request.POST.get("aadhar")
    name = request.POST.get("pname")
    cn = request.POST.get("contact")
    address = request.POST.get("address")
    PersonModel(aadhar=ano, pname=name, contact=cn, address=address).save()
    messages.success(request, "Person Details Saved")
    return redirect("main")


def viewPE(request):
    pf = PersonModel.objects.all()
    return render(request, "viewpe.html", {"data":pf})


def addPA(request):
    pa=PassportForm()
    return render(request, "addpa.html", {"form":pa})


def savePA(request):
    no=request.POST.get("pno")
    details=request.POST.get("p_details")
    pe=PassportModel(pno=no, p_details_id=details)
    pe.save()
    return redirect("main")


def viewPA(request):
    ef = PassportModel.objects.all()
    return render(request, "viewpa.html", {"data":ef})