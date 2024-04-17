from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from articles.models import Article
from accounts.models import User, Card
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

def gatcha(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = get_object_or_404(User, pk=request.user.pk)
            user.point = 100
            user.save()
            card = Card.objects.create(cardnum=1)
            user.cards.add(card)
            return redirect("users:gatcha")
        return render(request, "users/gatcha.html")
    return redirect("accounts:login")

def cards(request, pk):
    if request.user.is_authenticated:
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
                
        context = {
            "user": user,
            "cards": unique_cards,
            "count": len(unique_cards),
        }
        return render(request, "users/cards.html", context)
    return redirect("accounts:login")

