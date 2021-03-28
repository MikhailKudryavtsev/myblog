from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


def login(request):
    """Производит Вход в систему"""
    args = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Пользователь не найден!'})
    else:
        return render(request, 'login.html', args)


def logout(request):
    """Совершает Выход из системы"""
    auth.logout(request)
    return redirect('/')


def register(request):
    """Выполняет регистрацию пользователя"""
    args = {'form': UserCreationForm()}
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'],
                                         password=new_user_form.cleaned_data['password1'])
            auth.login(request, new_user)
            return redirect('/')
        else:
            args['form'] = new_user_form
    return render(request, 'register.html', args)
