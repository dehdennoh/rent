from django.shortcuts import render, redirect
from Hosyapp.models import Member, Contact, Users


# Create your views here.
def index(request):
    if request.method == 'POST':
        messages = Contact(name=request.POST['name'],
                           email=request.POST['email'],
                          subject=request.POST['subject'],
                           message=request.POST['message'])

        messages.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':
        members = Member(username=request.POST['username'],
                         email=request.POST['email'],
                         password=request.POST['password'])
        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def upload(request):
    return render(request, 'upload.html')


def details(request):
   messages = Contact.objects.all()
   return render(request, 'details.html', {'messages': messages})

def users(request):
    myusers = Users.objects.all()
    return render(request, 'users.html', {'myusers': myusers})

def adminhome(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():

            member = Member.objects.get(username=request.POST['username'],
                                        password=request.POST['password'])

            return render(request, 'adminhome.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
