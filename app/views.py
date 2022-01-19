from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from app.models import Question, User

from .forms import LoginForm, QuestionForm, RegisterForm

# Create your views here.
@login_required
def home(request):
    context = {}

    questions = [
        {"id": 1, "text": "What is 2+2?"},
        {"id": 2, "text": "What is 2+2?"},
        {"id": 3, "text": "What is 2+2?"},
    ]

    context["questions"] = questions
    context['user'] = request.user
    context['form'] = QuestionForm

    return render(request, 'home.html', context)


def register(request):
    context = {}

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = None
            try:
                user = User.objects.get(college_email=form.cleaned_data.get('college_email'))
            except (User.DoesNotExist):
                pass
            
            if user: 
                context["msg"] = "Account already exists!"
            else:
                user = User.objects.create_user(**form.cleaned_data)
                auth_login(request, user)
                return redirect('home')
                
    if request.user.is_authenticated:
        return redirect('home')

    context['form'] = RegisterForm()
    return render(request, 'register.html', context)


def login(request):
    context = {}

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            college_email = form.cleaned_data.get('college_email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, college_email=college_email, password=password)
            
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                context["msg"] = "Account already exists!"
                
    if request.user.is_authenticated:
        return redirect('home')

    context['form'] = LoginForm()
    return render(request, 'login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')


def profile(request):
    context = {}
    context['user'] = request.user
    return render(request, 'profile.html', context)


def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # question = Question(**form.cleaned_data)
            # print(question)
            pass
        
        return redirect('home')

    return HttpResponseNotFound()



def view_question(request, id):
    context = {}
    context['question'] = "hellooo"
    return render(request, 'question.html', context)