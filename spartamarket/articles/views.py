from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST, require_http_methods
from .forms import ArticleForm, CommentForm

from .models import Article, Comment


def index(request):
    return render(request, 'articles/index.html')

# Create your views here.


def articles(request):
    articles = Article.objects.all().order_by("-created_at")
    context = {
        "articles": articles,
    }
    return render(request, "articles/articles.html", context)


def view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = Comment.objects.all().order_by("-created_at")
    context = {
        "article": article,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "articles/view.html", context)

@require_http_methods(["GET", "POST"])
def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                article = form.save(commit=False)
                article.author = request.user
                article.save()
                return redirect("articles:view", article.pk)
        else:
            form = ArticleForm()
            image_url = "{% static 'articles/image-gallery.png' %}"
        context = {
            "form": form,
            "image_url": image_url,
        }
        return render(request, "articles/create.html", context)
    return redirect("accounts:login")


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.author:
        article.delete()
        return redirect("articles:articles")
    

@require_POST
def update(request, pk):
    article = get_object_or_404(Article, pk)
    if request.user == article.author:
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
            return redirect("articles:view", article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            "form": form,
        }
        return render(request, "articles/create.html", context)
    else:
        return redirect("articels:articles")
    
    
@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect("articles:articles")
    return redirect("accounts:login")


@require_POST
def comment_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(comment.article)
            comment.author = request.user
            comment.save()
            return redirect("articles:view", pk=pk)
    return redirect("accounts:login")


@require_POST
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.author:
        comment.delete()
        return redirect("articles:view", pk)
    else:
        return redirect("articles:view", pk)