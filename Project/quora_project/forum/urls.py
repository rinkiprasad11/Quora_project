from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post_question/', views.post_question, name='post_question'),
    path('question/<int:question_id>/answer/', views.answer_question, name='answer_question'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
