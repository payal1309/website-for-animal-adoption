from django.shortcuts import render,redirect
from .models import Accounts 
from .forms import AccountsForm
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request , 'home.html',{})

    
def listings(request):
    all_members = Accounts.objects.all()
    print('Img List: ', all_members)

    return render(request , 'listings.html', {'all':all_members})


def add(request):
    if request.method == 'POST':
        # form = AccountsForm(request.POST or None)
        form = AccountsForm(request.POST, request.FILES)
        print('iSvAl', form.is_valid())
        if form.is_valid():
            form.save()
            print('Saving')
        else:
            messages.success(request ,('There was an error in your form please try again'))
            return redirect('add')

        messages.success(request,('Your form has been Submitted Succesfully'))
        return redirect('listings')
    else:
        return render(request , 'add.html',{})