from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST, require_http_methods
from .forms import StoreForm
from django.contrib.auth import get_user_model

from .models import Store


def index(request):
    stores = Store.objects.all().order_by("-created_at")[:3]
    context = {
        "stores": stores,
    }
    return render(request, 'stores/index.html', context)

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
        store = get_object_or_404(store, pk=pk)
        if store.like_users.filter(pk=request.user.pk).exists():
            store.like_users.remove(request.user)
        else:
            store.like_users.add(request.user)
        return redirect("stores:stores_view", pk)
    return redirect("accounts:login")


def stores_view(request, pk):
    store = get_object_or_404(store, pk=pk)
    context = {
        "store": store,
    }
    return render(request, "stores/stores_view.html", context)


@require_http_methods(["GET", "POST"])
def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = StoreForm(request.POST, request.FILES)
            if form.is_valid():
                store = form.save(commit=False)
                store.author = request.user
                store.price = 0
                store.save()
                return redirect("stores:stores_view", store.pk)
            print(form.errors)
        else:
            form = StoreForm()
        context = {
            "form": form,
        }
        return render(request, "stores/create.html", context)
    return redirect("accounts:login")


@require_POST
def delete(request, pk):
    store = get_object_or_404(store, pk=pk)
    if request.user == store.author:
        store.delete()
        return redirect("stores:stores")


@require_http_methods(["GET", "POST"])
def update(request, pk):
    if request.user.is_authenticated:
        store = get_object_or_404(store, pk=pk)
        if request.user == store.author:
            if request.method == "POST":
                form = StoreForm(
                    request.POST, request.FILES, instance=store)
                if form.is_valid():
                    store = form.save()
                return redirect("stores:stores_view", store.pk)
            context = {
                "store": store,
            }
            return render(request, "stores/update.html", context)
        else:
            return redirect("articels:stores")
    return redirect("accounts:login")
