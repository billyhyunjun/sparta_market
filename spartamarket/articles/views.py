from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST, require_http_methods
from .forms import ArticleForm, CommentForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Article, Comment, Hashtag
from accounts.models import User
from stores.models import Store


def index(request):
    articles = Article.objects.all().order_by("-created_at")[:3]
    stores = Store.objects.all().order_by("-created_at")[:3]
    context = {
        "articles": articles,
        "stores": stores,
    }
    return render(request, 'articles/index.html', context)

# Create your views here.


@require_http_methods(["GET", "POST"])
def articles(request):
    select = request.GET.get("select")
    search = request.GET.get("search")
    sort = request.GET.get("sort", "-created_at")
    if select == "title":
        articles = Article.objects.filter(
            title__icontains=search).order_by(sort)
    elif select == "content":
        articles = Article.objects.filter(
            content__icontains=search).order_by(sort)
    elif select == "author":
        articles = Article.objects.filter(
            author__username__icontains=search).order_by(sort)
    else:
        articles = Article.objects.all().order_by(sort)
    context = {
        "articles": articles,
        "select": select,
        "search": search,
    }
    return render(request, "articles/articles.html", context)


def like_articles(request, pk):
    sort = request.GET.get("sort", "-created_at")
    member = get_object_or_404(get_user_model(), pk=pk)
    articles = member.like_articles.all().order_by(sort)
    context = {
        "articles": articles,
        "member": member,
    }
    return render(request, "articles/like_articles.html", context)


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect("articles:articles_view", pk)
    return redirect("accounts:login")


def articles_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comments.all().order_by("-pk")
    hashtags = article.hashtags.all().order_by("content")
    context = {
        "article": article,
        "comment_form": comment_form,
        "comments": comments,
        "hashtags": hashtags,
    }
    return render(request, "articles/articles_view.html", context)


@require_http_methods(["GET", "POST"])
def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                article = form.save(commit=False)
                article.author = request.user
                article.save()
                user = get_object_or_404(User, pk=request.user.pk)
                user.point += 100
                user.save() 
                for word in request.POST.get("hashtag").split():  # content를 공백기준 리스트로 변경
                    if word.startswith('#'):  # '#' 로 시작하는 요소 선택
                        hashtag, created = Hashtag.objects.get_or_create(content=word)
                        article.hashtags.add(hashtag)
                messages.add_message(request, messages.INFO, '게시글이 생성 되었습니다. **100포인트** ')
                return redirect("articles:articles_view", article.pk)
        else:
            form = ArticleForm()
        context = {
            "form": form,
        }
        return render(request, "articles/create.html", context)
    return redirect("accounts:login")


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.author:
        article.delete()
        messages.add_message(request, messages.INFO, '게시글이 삭제 되었습니다.')
        return redirect("articles:articles")


@require_http_methods(["GET", "POST"])
def update(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        hashtags = article.hashtags.all().order_by("content")
        if request.user == article.author:
            if request.method == "POST":
                form = ArticleForm(
                    request.POST, request.FILES, instance=article)
                if form.is_valid():
                    article = form.save()
                    article.hashtags.clear()  # 기존에 있던 hashtag 삭제
                    for word in article.content.split():
                        if word.startswith('#'):
                            hashtag, created = Hashtag.objects.get_or_create(content=word)
                            article.hashtags.add(hashtag)
                messages.add_message(request, messages.INFO, '게시글이 수정 되었습니다.')
                return redirect("articles:articles_view", article.pk)
            context = {
                "article": article,
                "hashtags": hashtags,
            }
            return render(request, "articles/update.html", context)
        else:
            return redirect("articels:articles")
    return redirect("accounts:login")


@require_POST
def comment_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            user = get_object_or_404(User, pk=request.user.pk)
            user.point += 10
            user.save()
            messages.add_message(request, messages.INFO, ' **10포인트** ')
            return redirect("articles:articles_view", pk=pk)
    return redirect("accounts:login")


@require_POST
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.author:
        comment.delete()
        return redirect("articles:articles_view", pk)
    else:
        return redirect("articles:articles_view", pk)


def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles = hashtag.hashtag_articles.order_by('-pk')
    
    context = {
        'hashtag': hashtag, 
        'articles': articles,
    }
    return render(request, 'articles/hashtag.html', context)