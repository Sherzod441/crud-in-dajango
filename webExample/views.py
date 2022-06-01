from django.shortcuts import redirect, render
from .models import Users
from .forms import UsersForm

# Create your views here.


def index(request):
    return render(request, 'App/home.html')

def about(request):
    return render(request, 'App/about.html')

def users(request):
    obj = Users.objects.all()
    return render(request, 'App/users.html', {'obj': obj})

def addUser(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Xatolik mavjud...'

                    
    
    form = UsersForm()

    data = {
        'form':form,
        'error':error,
    }
    return render(request, 'App/addUser.html', data)
    