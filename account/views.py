from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        user_name = request.POST['user']
        pass_word1 = request.POST['word1']
        pass_word2 = request.POST['word2']
        try:
            User.objects.get(username=user_name)
            return render(request, 'signup.html', {'用户名错误': '该用户已存在'})
        except User.DoesNotExist:
            if pass_word1 == pass_word2:
                User.objects.create(username=user_name, password=pass_word1)
                return redirect('主页')
            else:
                return render(request, 'signup.html', {'密码错误': '两次密码不一致'})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_name = request.POST['user']
        pass_word = request.POST['word']
        user = auth.authenticate(username=user_name, password=pass_word)
        if user is None:
            return render(request, 'login.html', {'错误': '账号或密码错误'})
        else:
            auth.login(request, user)
            return redirect('主页')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('主页')
