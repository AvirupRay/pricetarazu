from django.shortcuts import render
from django.http import *
from django.template import loader

# Create your views here.

home_template = loader.get_template('index.html')
main_template = loader.get_template('main.html')
login_template = loader.get_template('login.html')
signup_template = loader.get_template('signup.html')
about_template = loader.get_template('about.html')

def index(request):
    return HttpResponse(home_template.render({}, request))

def signup(request):
    pass

def login(request):
    pass

def logout(request):
    pass
