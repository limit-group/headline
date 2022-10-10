from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

from writy.models import Article


class SignUpForm(UserCreationForm):  
        class Meta:  
            model = User  
            fields = ('email','username')

class LoginForm():
    class Meta:
        model = User
        fields = ('username', 'password')

class ArticleForm():
    class Meta:
        model = Article
        fields = ('title', 'image', 'topic', 'content')

