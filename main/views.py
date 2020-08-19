from django.shortcuts import render, redirect
from . import models

#모델폼을 사용하기 위해 만들어둔 forms.py import
from .forms import CardForm

# Create your views here.

#홈화면 렌더링, 모든 모델 객체 반환
def home(request):
    cards = models.Card.objects.all()
    return render(request, 'home.html', {'cards':cards})


def create(request):

    if request.method == "POST":
        # 모델폼은 save기능까지 지원, request에서 채워진 폼을 입력받아 저장
        card = models.Card()
        card.title = request.POST['title']
        card.describe = request.POST['describe']
        card.img = request.POST['img']
        card.save()
        return redirect('home')
    else:
        return render(request, 'create.html', {'cardForm':CardForm})

    
def detail(request, card_id):
    card = models.Card.objects.get(pk=card_id)
    return render(request, 'detail.html', {'card':card})
