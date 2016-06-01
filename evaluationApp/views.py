from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
    )
from django.shortcuts import (
    render,
    redirect,
    )
from django.contrib import messages
from .models import evaluation201606
from .forms import evaluation201606Form

# Create your views here.

def _get_page(list_, page_no, count=5):
    paginator = Paginator(list_, count)
    try:
        page = paginator.page(page_no)
    except (EmptyPage, PageNotAnInteger):
        page = paginator.page(1)
    return page

def index(request):
    form = evaluation201606Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'投稿を受け付けました。')
            return redirect('evaluationApp:index')
        else:
            messages.error(request,'入力内容に誤りがあります。')
    page = _get_page(
        evaluation201606.objects.order_by('-id'),
        request.GET.get('page')
        )
    contexts = {
        'form': form,
        'page': page,
        }
    return render(request, 'evaluationApp/index.html', contexts)
