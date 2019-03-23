from django.shortcuts import render


# Create your views here.


def products_list(requests):
    return render(requests, 'products_list.html')
