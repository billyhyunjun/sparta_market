import random
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from articles.models import Article
from accounts.models import User, Card
from django.contrib import messages
# Create your views here.


@require_http_methods(["GET", "POST"])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    member = get_object_or_404(get_user_model(), username=username)
    articles = Article.objects.filter(author=user).order_by("-created_at")
    context = {
        "user": user,
        "articles": articles,
        "member": member,
    }
    return render(request, "users/profile.html", context)


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


def gatcha(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            if user.point >= 100:
                user.point -= 100
                user.save()
                gatcha = random.randint(1, 50)
                card = Card.objects.create(cardnum=gatcha)
                user.cards.add(card)
                context = {
                    "gatcha": str(gatcha),
                }
                return render(request, "users/gatcha.html", context)
            messages.add_message(request, messages.INFO, '포인트가 부족합니다.')
            return render(request, "users/gatcha.html")
        return render(request, "users/gatcha.html")
    return redirect("accounts:login")


def cards(request, pk):
    user = get_object_or_404(User, pk=pk)
    all_cards = user.cards.all().order_by("cardnum")
    # 중복을 제거할 빈 리스트를 생성
    unique_cards = []
    # 이미 추가한 카드의 번호를 추적하기 위한 집합을 생성
    added_card_nums = set()
    # 중복을 제거하고 유니크한 카드만 추가
    for card in all_cards:
        if card.cardnum not in added_card_nums:
            unique_cards.append(card)
            added_card_nums.add(card.cardnum)
    card_list = []
    card_nums = sorted(list(added_card_nums))
    for i in range(1, 51):
        if str(i) in card_nums:
            card_list.append(unique_cards[card_nums.index(str(i))])
        else:
            card_list.append("blank")
    count = len(unique_cards)
    context = {
        "user": user,
        "cards": unique_cards,
        "count": count,
        "card_list": card_list,
    }
    return render(request, "users/cards.html", context)


def card_storage(request, pk):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=pk)
        if request.method == "POST":
            cardnum = request.POST.get("cardnum")
            card_choices = Card.objects.filter(cardnum=cardnum, card_users=request.user)
            if card_choices.exists():
                context = {
                    "card_choice": card_choices.first(),  
                }
            return render(request, "stores/create.html", context)
        all_cards = user.cards.all().order_by("cardnum")
        count = len(all_cards)
        context = {
            "user": user,
            "all_cards": all_cards,
            "count": count,
        }
        return render(request, "users/card_storage.html", context)
    return redirect("accounts:login")


def document(request):
    cards = [str(i) for i in range(1, 51)]
    context = {
        "cards": cards,
    }
    return render(request, "users/document.html", context)
