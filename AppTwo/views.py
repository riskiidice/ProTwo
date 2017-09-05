from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    context= { 'insert_me': 'Help Page'}
    return render(request,'AppTwo/help.html', context)

def users(request):
    users_list = User.objects.all()
    context = { 'users': users_list }
    return render(request, 'AppTwo/users.html', context)
