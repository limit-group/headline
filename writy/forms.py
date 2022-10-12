from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from writy.models import Article, Comment, Subscriber, Contact


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username")


class LoginForm:
    class Meta:
        model = User
        fields = ("username", "password")


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "image", "topic", "content")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ("email",)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("email", "subject", "message")

# class FeedbackForm(forms.ModelForm):

#     class Meta:
#         model = FeedbackForm
#         fields= {}