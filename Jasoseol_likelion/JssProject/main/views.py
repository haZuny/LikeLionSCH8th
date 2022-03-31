from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm, CommentForm
from .models import Jasoseol, Comment
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

#페이지네이터(페이지를 나눌수 있게 해준다) 임포트
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    all_jss = Jasoseol.objects.all()    #자소설 전체 목록 불러오기
    paginator = Paginator(all_jss, 5)   #전체목록에서 5개를 한 페이지로 자르기(객체리스트, 개수)
    page = request.GET.get('page')      #요청 받은 페이지가 뭔지 알아냄
    jss_page = paginator.get_page(page) #아까 자른 페이지 중에서 요청받은 페이지에 들어가는 자소서 목록들
    return render(request, 'index.html', {'all_jss':jss_page})

def my_index(request):
    my_jss = Jasoseol.objects.filter(author=request.user)
    return render(request, 'index.html', {'all_jss':my_jss})

def create(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            temp_form = filled_form.save(commit=False)
            temp_form.author = request.user
            temp_form.save()
            return redirect('index')
    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form':jss_form})

@login_required(login_url='/login')
def detail(request, jss_id):
    try:
        my_jss = Jasoseol.objects.get(pk=jss_id)
        comment_form = CommentForm()
    except:
        raise Http404


    return render(request, 'detail.html', {'my_jss':my_jss, 'comment_form':comment_form})

def delete(request, jss_id):
    my_jss = get_object_or_404(Jasoseol, pk=jss_id)
    if request.user == my_jss.author:
        my_jss.delete()
        return redirect('index')

    raise PermissionDenied

def update(request, jss_id):
    my_jss = get_object_or_404(Jasoseol, pk=jss_id)
    if request.user == my_jss.author:
        jss_form = JssForm(instance=my_jss)

        if request.method=="POST":
            updated_form = JssForm(request.POST, instance=my_jss)
            if updated_form.is_valid():
                updated_form.save()
                return redirect('index')

        return render(request, 'create.html', {'jss_form':jss_form})
    raise PermissionDenied

def create_comment(request, jss_id):
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        temp_form = comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.jasoseol = Jasoseol.objects.get(pk = jss_id)
        temp_form.save()
        return redirect('detail', jss_id)

def delete_comment(request, jss_id, comment_id):
    my_comment = Comment.objects.get(pk = comment_id)
    if request.user == my_comment.author:
        my_comment.delete()
        return redirect('detail', jss_id)
    else:
        raise PermissionDenied