from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from .forms import *
from .filters import *


# Create your views here.


def home(request):
    farmers = Farmer.objects.all()
    total_farmers = farmers.count()

    centre_managers = CentreManager.objects.all()
    total_centre_managers = centre_managers.count()

    context = {'total_farmers': total_farmers,
               'total_centre_managers': total_centre_managers}
    return render(request, 'index.html', context)


# Customers
def FarmersList(request):
    farmers = Farmer.objects.all()

    myFilter = FarmersFilter(request.GET, queryset=farmers)
    farmers = myFilter.qs

    paginator = Paginator(farmers, 10)
    page_number = request.GET.get('page', 1)
    farmer_obj = paginator.get_page(page_number)
    context = {'farmers': farmers,
               'farmer_obj': farmer_obj, 'myFilter': myFilter}
    return render(request, 'farmers/farmers_list.html', context)


def addFarmer(request):
    form = FarmersForm()
    if request.method == 'POST':
        form = FarmersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farmers')

    context = {"form": form}
    return render(request, 'farmers\farmers_add.html', context)


