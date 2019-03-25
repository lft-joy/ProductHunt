from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


# Create your views here.


def products_list(requests):
    return render(requests, 'products_list.html')


def product(request):
    if request.method == 'GET':
        return render(request, 'product.html')
    elif request.method == 'POST':
        title = request.POST['APP名称']
        intro = request.POST['介绍']
        try:
            icon = request.POST['图片']
            product = Product()
            product.title = title
            product.icon = icon
            product.intro = intro
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('主页')
        except Exception as e:
            return render(request, 'products_list.html', {'错误': '请上传图片'})
