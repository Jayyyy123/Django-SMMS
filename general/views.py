from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MaintenanceEquipment, MaintenanceRequest, RecordEquipment
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CreateMaintenanceRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# general -> index

def userBooking(request):
    equipment = MaintenanceEquipment.objects.all()[0]
    equipment2 = MaintenanceEquipment.objects.all()[1]
    equipment3 = MaintenanceEquipment.objects.all()[2]
    equipment4 = MaintenanceEquipment.objects.all()[3]
    equipment5 = MaintenanceEquipment.objects.all()[4]
    equipment6 = MaintenanceEquipment.objects.all()[5]

    form = CreateMaintenanceRequest(request.POST or None)
    if form.is_valid():
        form.save()
        form = CreateMaintenanceRequest()
        print("Success")
        # messages.success(request, 'You have done submitted')
        return redirect('userBooking')

    context = {'equipment': equipment,
               'equipment2': equipment2, 'equipment3': equipment3,
               'equipment4': equipment4, 'equipment5': equipment5,
               'equipment6': equipment6, 'form': form}

    return render(request, 'userBooking.html', context)


def userCancel(request):
    cancels = MaintenanceRequest.objects.filter(progress=("Uncomplete"))

    if request.method == 'POST':
        cancels.delete()
        return redirect('userCancel')

    return render(request, 'userCancel.html', {'cancels': cancels})


def userHistory(request):
    history = MaintenanceRequest.objects.filter(progress=("Completed"))
    return render(request, 'userHistory.html', {'history': history})


def userProfile(request):
    return render(request, 'userProfile.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def logInPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('userBooking')

        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def createOrder(request):

    context = {}
    return render(request, 'order.html', context)
