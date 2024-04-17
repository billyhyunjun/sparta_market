from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .forms import CustomUserChangeForm, CustumUserCreationForm
from django.contrib import messages
from .models import User
from articles.models import Article


# Create your views here.

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        if request.POST.get("way") == "signin":
            form_login = AuthenticationForm(request, request.POST)
            form_singup = CustumUserCreationForm()
            if form_login.is_valid():
                auth_login(request, form_login.get_user())
                next_url = request.GET.get("next") or "index"
                return redirect(next_url)
        elif request.POST.get("way") == "signup":
            form_singup = CustumUserCreationForm(request.POST)
            form_login = AuthenticationForm()
            if form_singup.is_valid():
                user = form_singup.save()
                auth_login(request, user)
                return redirect("index")
        messages.add_message(request, messages.INFO, '입력이 잘못 되었습니다.')
    else:
        form_login = AuthenticationForm()
        form_singup = CustumUserCreationForm()
    context = {
        "form_login": form_login,
        "form_singup": form_singup,
    }
    return render(request, "accounts/login.html", context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("index")


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
        return redirect("index")
    else:
        return redirect("index")



@require_http_methods(["GET", "POST"])
def update(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserChangeForm(
                request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect("index")
            else:
                messages.add_message(request, messages.INFO, '입력이 잘못 되었습니다.')
        user = get_object_or_404(User, pk=request.user.pk)
        context = {
            "user": user,
        }
        return render(request, "accounts/update.html", context)
    return redirect("accounts:login")
