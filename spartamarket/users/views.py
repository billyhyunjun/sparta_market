from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from articles.models import Article
from accounts.models import User 
# Create your views here.


@require_http_methods(["GET", "POST"])
def profile(request, username):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=username)
        member = get_object_or_404(get_user_model(), username=username)
        articles = Article.objects.filter(author=user).order_by("-created_at")
        context = {
            "user": user,
            "articles": articles,
            "member": member,
        }
        return render(request, "users/profile.html", context)
    return redirect("accounts:login")


@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_id)
        if request.user != member:
            if member.followers.filter(pk=request.user.pk).exists():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", member.username)
    return redirect("accounts:login")
