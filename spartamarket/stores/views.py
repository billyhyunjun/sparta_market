from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST, require_http_methods
from .forms import StoreForm
from django.contrib.auth import get_user_model
from accounts.models import User
from .models import Store
from django.contrib import messages

# Create your views here.


@require_http_methods(["GET", "POST"])
def stores(request):
    select = request.GET.get("select")
    search = request.GET.get("search")
    sort = request.GET.get("sort", "-created_at")
    if select == "title":
        stores = Store.objects.filter(
            title__icontains=search).order_by(sort)
    elif select == "content":
        stores = Store.objects.filter(
            content__icontains=search).order_by(sort)
    elif select == "author":
        stores = Store.objects.filter(
            author__username__icontains=search).order_by(sort)
    else:
        stores = Store.objects.all().order_by(sort)
        
    context = {
        "stores": stores,
        "select": select,
        "search": search,
    }
    return render(request, "stores/stores.html", context)


def like_stores(request, pk):
    sort = request.GET.get("sort", "-created_at")
    member = get_object_or_404(get_user_model(), pk=pk)
    stores = member.like_stores.all().order_by(sort)
    context = {
        "stores": stores,
        "member": member,
    }
    return render(request, "stores/like_stores.html", context)


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        store = get_object_or_404(Store, pk=pk)
        if store.like_users.filter(pk=request.user.pk).exists():
            store.like_users.remove(request.user)
        else:
            store.like_users.add(request.user)
        return redirect("stores:stores_view", pk)
    return redirect("accounts:login")


def stores_view(request, pk):
    store = get_object_or_404(Store, pk=pk)
    context = {
        "store": store,
    }
    return render(request, "stores/stores_view.html", context)


@require_http_methods(["GET", "POST"])
def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = StoreForm(request.POST)
            if form.is_valid():
                store = form.save(commit=False)
                store.author = request.user
                store.save()
                seller = get_object_or_404(User, pk=store.author.pk)
                card = store.card
                seller.cards.remove(card)
                messages.add_message(request, messages.INFO, '상점이 등록되었습니다.')
                return redirect("stores:stores_view", store.pk)
        else:
            form = StoreForm()
        context = {
            "form": form,
        }
        return render(request, "stores/create.html", context)
    return redirect("accounts:login")


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        store = get_object_or_404(Store, pk=pk)
        if request.user == store.author or request.user.is_superuser:
            seller = get_object_or_404(User, pk=store.author.pk)
            card = store.card
            seller.cards.add(card)
            store.delete()
            messages.add_message(request, messages.INFO, '상점이 삭제 되었습니다.')
            return redirect("stores:stores")
    return redirect("accounts:login")

@require_POST
def buy(request, pk):
    if request.user.is_authenticated:
        store = get_object_or_404(Store, pk=pk)
        if request.user != store.author:
            seller = get_object_or_404(User, pk=store.author.pk)
            buyer = get_object_or_404(User, pk=request.user.pk)
            if buyer.point >= store.price:
                buyer.point -= store.price
                seller.point += store.price
                buyer.save()
                seller.save()
                card = store.card
                buyer.cards.add(card)
                store.delete()
                return redirect("stores:stores")
            else:
                messages.add_message(request, messages.INFO, '포인드가 부족합니다.')
                return redirect("stores:stores_view", pk)
    return redirect("accounts:login")


@require_http_methods(["GET", "POST"])
def update(request, pk):
    if request.user.is_authenticated:
        store = get_object_or_404(Store, pk=pk)
        if request.user == store.author or request.user.is_superuser:
            if request.method == "POST":
                form = StoreForm(request.POST, instance=store)
                if form.is_valid():
                    store = form.save()
                    messages.add_message(request, messages.INFO, '상점이 수정 되었습니다.')
                return redirect("stores:stores_view", store.pk)
            context = {
                "store": store,
            }
            return render(request, "stores/update.html", context)
        else:
            return redirect("stores:stores")
    return redirect("accounts:login")
