
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('topics/<slug:slug>/', views.topics, name="topics"),
    path('articles/new/', views.article_new, name="article_new"),
    path('articles/<int:pk>/', views.articles, name="articles"),
    path('articles/<slug:slug>/', views.article, name="article"),
    path('drafts/<int:pk>/', views.drafts, name="drafts"),
    path('drafts/<int:pk>/update/<int:article_pk>/', views.draft_publish, name="draft_publish"),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name="logout"),
    path('accounts/profile/', views.profile, name="profile"),
    path('subscribe/', views.subscribe, name="subscribe"),
    path('comment/<int:article_pk>/', views.comment, name="comment"),
    path('terms-and-conditions/', views.terms, name="terms")
]
