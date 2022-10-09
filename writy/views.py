from django.shortcuts import get_object_or_404,  render
from django.contrib.auth import logout
from writy.models import Article, Topic, Subscriber, Comment
from django.contrib.auth.models import User


# 404 Page

def error_404(request, exception):
    return render(request, 'writy/404.html')



# Home Page

def home(request):
    categories = Topic.objects.all()
    return render(request, 'writy/home.html', {'categories': categories})


def topics(request, slug):
    categories = Topic.objects.all()
    topic = get_object_or_404(Topic, slug=slug)
    articles = Article.objects.filter(topic=topic, status=1).order_by('-created_on')

    return render(request, 'writy/articles.html', {'articles': articles, 'categories': categories})


# All articles for a given author

def articles(request, pk):
    categories = Topic.objects.all()
    author = get_object_or_404(User, pk=pk)
    articles = Article.objects.filter(author=author, status=1).order_by('-created_on')

    return render(request, 'article/articles.html', {'articles': articles, 'categories': categories})



# View a single article.

def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    categories = Topic.objects.all()
    comments = Comment.objects.filter(article=article).order_by('-created_on').all()
    print(comments)
    return render(request, 'writy/article.html', {'article': article, 'comments': comments, 'categories': categories})


# Create a new article.

def article_new(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.user
        slug = title.replace(" ", "-")
        content = request.POST['editor']
        image = request.FILES['image']
        topic = request.POST['topic']

        topic1 = get_object_or_404(Topic, pk=topic)
        article = Article(title=title, author=author, slug=slug, content=content, image=image, topic=topic1)
        article.save()

        context = {}
        context['success'] = "Succcessfuly Posted an article, Head over to publish!"

        return render(request, 'article/new.html')
    else:

        categories = Topic.objects.all()
        return render(request, 'article/new.html', {'categories': categories})


# List of draft Articles.

def drafts(request, pk):
    author = get_object_or_404(User, pk=pk)
    articles = Article.objects.filter(author=author, status=0).order_by('-created_on')
    categories = Topic.objects.all()

    return render(request, 'article/drafts.html', {'articles': articles, 'categories': categories})


# Publish a draft article.

def draft_publish(request, pk, article_pk):
    author = get_object_or_404(User, pk=pk)
    articles = Article.objects.filter(author=author, status=0).order_by('-created_on')
    Article.objects.filter(author=author, pk=article_pk).update(status=1)
    categories = Topic.objects.all()

    return render(request, 'article/drafts.html', {'articles': articles, 'categories': categories})



#  Comment on an article. 

def comment(request, article_pk):
    # if request.method == 'POST':
    comment = request.POST['comment']
    article = get_object_or_404(Article, pk=article_pk)
    author = request.user
    comment = Comment(comment=comment, article=article, author=author)
    comment.save()

    categories = Topic.objects.all()

    return render(request, 'writy/article.html', {'article': article, 'categories': categories})



# Subscribe to newsletter

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']

        subscriber = Subscriber(email=email)
        subscriber.save()
        categories = Topic.objects.all()
        context = {}
        context['message'] = "You have now part of the Scratch family, Thank you!"
        context['categories'] = categories

        

        return render(request, 'writy/home.html', context)
    else:
        return render(request, 'writy/subscribe.html')


# Terms of Service.

def terms(request):
    categories = Topic.objects.all()
    return render(request, 'writy/terms.html', {'categories': categories})

# User Registration.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']

        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username, email, password)

        return render(request, 'registration/login.html')
        
    else:
        return render(request, 'registration/signup.html')


def profile(request):
    categories = Topic.objects.all()
    return render(request, 'registration/profile.html', {'categories': categories})

# Logout.

def logout_view(request):
    categories = Topic.objects.all()
    logout(request)
    # Redirect to a success page.
   
    return render(request, 'registration/logged_out.html', {'categories': categories})

