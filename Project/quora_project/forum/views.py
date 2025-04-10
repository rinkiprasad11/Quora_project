from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, QuestionForm, AnswerForm
from .models import Question, Answer, Like
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages





def home(request):
   
    questions = Question.objects.all()  
    
    
    for question in questions:
        for answer in question.answer_set.all():
            print(f"Answer content: {answer.content}")  

    return render(request, 'forum/home.html', {'questions': questions})

@login_required
def profile(request):
    return render(request, 'forum/profile.html', {'user': request.user})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():  
            user = form.save()  
            login(request, user)  
            return redirect('home')  
    else:
        form = UserRegistrationForm()
    return render(request, 'forum/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  
            user = form.get_user()  
            print(f"Username entered: {form.cleaned_data['username']}")  
           
            login(request, user) 
            return redirect('home')  
    else:
        form = AuthenticationForm()  
    
    return render(request, 'forum/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('home')


def home(request):
    questions = Question.objects.all()
    return render(request, 'forum/home.html', {'questions': questions})

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
           
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('home')  
    else:
        form = QuestionForm()
    return render(request, 'forum/post_question.html', {'form': form})


@login_required
def answer_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)  
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)  
            answer.question = question  
            answer.author = request.user  
            answer.save()  
            return redirect('home')  
    else:
        form = AnswerForm()  
    return render(request, 'forum/answer_question.html', {'form': form, 'question': question})


@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    existing_like = Like.objects.filter(user=request.user, answer=answer).first()

    if existing_like:
        
        existing_like.delete()
    else:
       
        Like.objects.create(user=request.user, answer=answer)

    return redirect('question_detail', question_id=answer.question.id)


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
   
    return render(request, 'forum/question_detail.html', {'question': question})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  
        else:
            messages.error(request, 'Error occurred during sign up. Please try again.')
    else:
        form = UserCreationForm()

    return render(request, 'forum/signup.html', {'form': form})