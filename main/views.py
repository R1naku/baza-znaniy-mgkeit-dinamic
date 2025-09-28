from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from .forms import RegistForm, LoginForm

def regist(request):#регистрация
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = RegistForm()
    return render(request, 'main/register/regist.html', {'form': form})

def login_view(request): #вход в профиль
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Попытка входа по логину
            user = authenticate(request, username=username_or_email, password=password)
            
            # Если не получилось, попробуем по email
            if user is None:
                try:
                    user_obj = User.objects.get(email=username_or_email)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    user = None
            
            if user is not None:
                login(request, user)
                welcome_name = user.first_name if user.first_name else user.username
                messages.success(request, f'Добро пожаловать, {welcome_name}!')
                return redirect('home')
            else:
                messages.error(request, 'Неверный логин/email или пароль')
    else:
        form = LoginForm()
    
    return render(request, 'main/login/login.html', {'form': form})

#функция выхода
def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('home')

def index(request):
    return render(request, 'main/index.html')

# Универсальная функция для площадок
def place_view(request, place_num):
    template_name = f'main/place{place_num}.html'
    return render(request, template_name)

def place1(request):
    return place_view(request, 1)

def place2(request):
    return place_view(request, 2)

def place3(request):
    return place_view(request, 3)

def place4(request):
    return place_view(request, 4)

# Универсальная функция для курсов
def course_view(request, place_num, course_num):
    template_name = f'main/p{place_num}/k{course_num}p{place_num}.html'
    return render(request, template_name)

def k1p1(request):
    return course_view(request, 1, 1)

def k2p1(request):
    return course_view(request, 1, 2)

def k3p1(request):
    return course_view(request, 1, 3)

def k4p1(request):
    return course_view(request, 1, 4)

def k1p2(request):
    return course_view(request, 2, 1)

def k2p2(request):
    return course_view(request, 2, 2)

def k3p2(request):
    return course_view(request, 2, 3)

def k4p2(request):
    return course_view(request, 2, 4)

def k1p3(request):
    return course_view(request, 3, 1)

def k2p3(request):
    return course_view(request, 3, 2)

def k3p3(request):
    return course_view(request, 3, 3)

def k4p3(request):
    return course_view(request, 3, 4)

def k1p4(request):
    return course_view(request, 4, 1)

def k2p4(request):
    return course_view(request, 4, 2)

def k3p4(request):
    return course_view(request, 4, 3)

def k4p4(request):
    return course_view(request, 4, 4)

# Универсальная функция для уроков
def lesson_view(request, place_num, course_num, lesson_num):
    template_name = f'main/p{place_num}/lessonk{course_num}p{place_num}/l{lesson_num}k{course_num}p{place_num}.html'
    return render(request, template_name)

# Универсальная функция для тестов
def test_view(request, place_num, course_num, lesson_num, test_num):
    template_name = f'main/p{place_num}/lessonk{course_num}p{place_num}/tl{lesson_num}k{course_num}p{place_num}/t{test_num}l{lesson_num}k{course_num}p{place_num}.html'
    return render(request, template_name)

def l1k1p1(request):
    return lesson_view(request, 1, 1, 1)

def l2k1p1(request):
    return render(request, 'main/p1/lessonk1p1/l2k1p1.html')

def l3k1p1(request):
    return render(request, 'main/p1/lessonk1p1/l3k1p1.html')

def l4k1p1(request):
    return render(request, 'main/p1/lessonk1p1/l4k1p1.html')

def l1k2p1(request):
    return render(request, 'main/p1/lessonk2p1/l1k2p1.html')

def l2k2p1(request):
    return render(request, 'main/p1/lessonk2p1/l2k2p1.html')
    
def l3k2p1(request):
    return render(request, 'main/p1/lessonk2p1/l3k2p1.html')

def l4k2p1(request):
    return render(request, 'main/p1/lessonk2p1/l4k2p1.html')

def l1k3p1(request):
    return render(request, 'main/p1/lessonk3p1/l1k3p1.html')

def l2k3p1(request):
    return render(request, 'main/p1/lessonk3p1/l2k3p1.html')
    
def l3k3p1(request):
    return render(request, 'main/p1/lessonk3p1/l3k3p1.html')

def l4k3p1(request):
    return render(request, 'main/p1/lessonk3p1/l4k3p1.html')

def l1k4p1(request):
    return render(request, 'main/p1/lessonk4p1/l1k4p1.html')

def l2k4p1(request):
    return render(request, 'main/p1/lessonk4p1/l2k4p1.html')
    
def l3k4p1(request):
    return render(request, 'main/p1/lessonk4p1/l3k4p1.html')

def l4k4p1(request):
    return render(request, 'main/p1/lessonk4p1/l4k4p1.html')

def l1k1p2(request):
    return render(request, 'main/p2/lessonk1p2/l1k1p2.html')

def l2k1p2(request):
    return render(request, 'main/p2/lessonk1p2/l2k1p2.html')

def l3k1p2(request):
    return render(request, 'main/p2/lessonk1p2/l3k1p2.html')

def l4k1p2(request):
    return render(request, 'main/p2/lessonk1p2/l4k1p2.html')

def l1k2p2(request):
    return render(request, 'main/p2/lessonk2p2/l1k2p2.html')

def l2k2p2(request):
    return render(request, 'main/p2/lessonk2p2/l2k2p2.html')
    
def l3k2p2(request):
    return render(request, 'main/p2/lessonk2p2/l3k2p2.html')

def l4k2p2(request):
    return render(request, 'main/p2/lessonk2p2/l4k2p2.html')

def l1k3p2(request):
    return render(request, 'main/p2/lessonk3p2/l1k3p2.html')

def l2k3p2(request):
    return render(request, 'main/p2/lessonk3p2/l2k3p2.html')
    
def l3k3p2(request):
    return render(request, 'main/p2/lessonk3p2/l3k3p2.html')

def l4k3p2(request):
    return render(request, 'main/p2/lessonk3p2/l4k3p2.html')

def l1k4p2(request):
    return render(request, 'main/p2/lessonk4p2/l1k4p2.html')

def l2k4p2(request):
    return render(request, 'main/p2/lessonk4p2/l2k4p2.html')
    
def l3k4p2(request):
    return render(request, 'main/p2/lessonk4p2/l3k4p2.html')

def l4k4p2(request):
    return render(request, 'main/p2/lessonk4p2/l4k4p2.html')

def l1k1p3(request):
    return render(request, 'main/p3/lessonk1p3/l1k1p3.html')

def l2k1p3(request):
    return render(request, 'main/p3/lessonk1p3/l2k1p3.html')

def l3k1p3(request):
    return render(request, 'main/p3/lessonk1p3/l3k1p3.html')

def l4k1p3(request):
    return render(request, 'main/p3/lessonk1p3/l4k1p3.html')

def l1k2p3(request):
    return render(request, 'main/p3/lessonk2p3/l1k2p3.html')

def l2k2p3(request):
    return render(request, 'main/p3/lessonk2p3/l2k2p3.html')
    
def l3k2p3(request):
    return render(request, 'main/p3/lessonk2p3/l3k2p3.html')

def l4k2p3(request):
    return render(request, 'main/p3/lessonk2p3/l4k2p3.html')

def l1k3p3(request):
    return render(request, 'main/p3/lessonk3p3/l1k3p3.html')

def l2k3p3(request):
    return render(request, 'main/p3/lessonk3p3/l2k3p3.html')
    
def l3k3p3(request):
    return render(request, 'main/p3/lessonk3p3/l3k3p3.html')

def l4k3p3(request):
    return render(request, 'main/p3/lessonk3p3/l4k3p3.html')

def l1k4p3(request):
    return render(request, 'main/p3/lessonk4p3/l1k4p3.html')

def l2k4p3(request):
    return render(request, 'main/p3/lessonk4p3/l2k4p3.html')
    
def l3k4p3(request):
    return render(request, 'main/p3/lessonk4p3/l3k4p3.html')

def l4k4p3(request):
    return render(request, 'main/p3/lessonk4p3/l4k4p3.html')

def l1k1p4(request):
    return render(request, 'main/p4/lessonk1p4/l1k1p4.html')

def l2k1p4(request):
    return render(request, 'main/p4/lessonk1p4/l2k1p4.html')

def l3k1p4(request):
    return render(request, 'main/p4/lessonk1p4/l3k1p4.html')

def l4k1p4(request):
    return render(request, 'main/p4/lessonk1p4/l4k1p4.html')

def l1k2p4(request):
    return render(request, 'main/p4/lessonk2p4/l1k2p4.html')

def l2k2p4(request):
    return render(request, 'main/p4/lessonk2p4/l2k2p4.html')
    
def l3k2p4(request):
    return render(request, 'main/p4/lessonk2p4/l3k2p4.html')

def l4k2p4(request):
    return render(request, 'main/p4/lessonk2p4/l4k2p4.html')

def l1k3p4(request):
    return render(request, 'main/p4/lessonk3p4/l1k3p4.html')

def l2k3p4(request):
    return render(request, 'main/p4/lessonk3p4/l2k3p4.html')
    
def l3k3p4(request):
    return render(request, 'main/p4/lessonk3p4/l3k3p4.html')

def l4k3p4(request):
    return render(request, 'main/p4/lessonk3p4/l4k3p4.html')

def l1k4p4(request):
    return render(request, 'main/p4/lessonk4p4/l1k4p4.html')

def l2k4p4(request):
    return render(request, 'main/p4/lessonk4p4/l2k4p4.html')
    
def l3k4p4(request):
    return render(request, 'main/p4/lessonk4p4/l3k4p4.html')

def l4k4p4(request):
    return render(request, 'main/p4/lessonk4p4/l4k4p4.html')

def t1l1k1p1(request):
    return render(request, 'main/p1/lessonk1p1/tl1k1p1/t1l1k1p1.html')

def t2l1k1p1(request):
    return render(request, 'main/p1/lessonk1p1/tl1k1p1/t2l1k1p1.html')

def t3l1k1p1(request):
    return render(request, 'main/p1/lessonk1p1/tl1k1p1/t3l1k1p1.html')

def t4l1k1p1(request):
    return render(request, 'main/p1/lessonk1p1/tl1k1p1/t4l1k1p1.html')

def t1l1k2p1(request):
    return render(request, 'main/p1/lessonk2p1/tl1k2p1/t1l1k2p1.html')

def t2l1k2p1(request):
    return render(request, 'main/p1/lessonk2p1/tl1k2p1/t2l1k2p1.html')

def t3l1k2p1(request):
    return render(request, 'main/p1/lessonk2p1/tl1k2p1/t3l1k2p1.html')

def t4l1k2p1(request):
    return render(request, 'main/p1/lessonk2p1/tl1k2p1/t4l1k2p1.html')

def t1l1k3p1(request):
    return render(request, 'main/p1/lessonk3p1/tl1k3p1/t1l1k3p1.html')

def t2l1k3p1(request):
    return render(request, 'main/p1/lessonk3p1/tl1k3p1/t2l1k3p1.html')

def t3l1k3p1(request):
    return render(request, 'main/p1/lessonk3p1/tl1k3p1/t3l1k3p1.html')

def t4l1k3p1(request):
    return render(request, 'main/p1/lessonk3p1/tl1k3p1/t4l1k3p1.html')

def t1l1k4p1(request):
    return render(request, 'main/p1/lessonk4p1/tl1k4p1/t1l1k4p1.html')

def t2l1k4p1(request):
    return render(request, 'main/p1/lessonk4p1/tl1k4p1/t2l1k4p1.html')

def t3l1k4p1(request):
    return render(request, 'main/p1/lessonk4p1/tl1k4p1/t3l1k4p1.html')

def t4l1k4p1(request):
    return render(request, 'main/p1/lessonk4p1/tl1k4p1/t4l1k4p1.html')

def t1l1k1p2(request):
    return render(request, 'main/p2/lessonk1p2/tl1k1p2/t1l1k1p2.html')

def t2l1k1p2(request):
    return render(request, 'main/p2/lessonk1p2/tl1k1p2/t2l1k1p2.html')

def t3l1k1p2(request):
    return render(request, 'main/p2/lessonk1p2/tl1k1p2/t3l1k1p2.html')

def t4l1k1p2(request):
    return render(request, 'main/p2/lessonk1p2/tl1k1p2/t4l1k1p2.html')

def t1l1k2p2(request):
    return render(request, 'main/p2/lessonk2p2/tl1k2p2/t1l1k2p2.html')

def t2l1k2p2(request):
    return render(request, 'main/p2/lessonk2p2/tl1k2p2/t2l1k2p2.html')

def t3l1k2p2(request):
    return render(request, 'main/p2/lessonk2p2/tl1k2p2/t3l1k2p2.html')

def t4l1k2p2(request):
    return render(request, 'main/p2/lessonk2p2/tl1k2p2/t4l1k2p2.html')

def t1l1k3p2(request):
    return render(request, 'main/p2/lessonk3p2/tl1k3p2/t1l1k3p2.html')

def t2l1k3p2(request):
    return render(request, 'main/p2/lessonk3p2/tl1k3p2/t2l1k3p2.html')

def t3l1k3p2(request):
    return render(request, 'main/p2/lessonk3p2/tl1k3p2/t3l1k3p2.html')

def t4l1k3p2(request):
    return render(request, 'main/p2/lessonk3p2/tl1k3p2/t4l1k3p2.html')

def t1l1k4p2(request):
    return render(request, 'main/p2/lessonk4p2/tl1k4p2/t1l1k4p2.html')

def t2l1k4p2(request):
    return render(request, 'main/p2/lessonk4p2/tl1k4p2/t2l1k4p2.html')

def t3l1k4p2(request):
    return render(request, 'main/p2/lessonk4p2/tl1k4p2/t3l1k4p2.html')

def t4l1k4p2(request):
    return render(request, 'main/p2/lessonk4p2/tl1k4p2/t4l1k4p2.html')

def t1l1k1p3(request):
    return render(request, 'main/p3/lessonk1p3/tl1k1p3/t1l1k1p3.html')

def t2l1k1p3(request):
    return render(request, 'main/p3/lessonk1p3/tl1k1p3/t2l1k1p3.html')

def t3l1k1p3(request):
    return render(request, 'main/p3/lessonk1p3/tl1k1p3/t3l1k1p3.html')

def t4l1k1p3(request):
    return render(request, 'main/p3/lessonk1p3/tl1k1p3/t4l1k1p3.html')

def t1l1k2p3(request):
    return render(request, 'main/p3/lessonk2p3/tl1k2p3/t1l1k2p3.html')

def t2l1k2p3(request):
    return render(request, 'main/p3/lessonk2p3/tl1k2p3/t2l1k2p3.html')

def t3l1k2p3(request):
    return render(request, 'main/p3/lessonk2p3/tl1k2p3/t3l1k2p3.html')

def t4l1k2p3(request):
    return render(request, 'main/p3/lessonk2p3/tl1k2p3/t4l1k2p3.html')

def t1l1k3p3(request):
    return render(request, 'main/p3/lessonk3p3/tl1k3p3/t1l1k3p3.html')

def t2l1k3p3(request):
    return render(request, 'main/p3/lessonk3p3/tl1k3p3/t2l1k3p3.html')

def t3l1k3p3(request):
    return render(request, 'main/p3/lessonk3p3/tl1k3p3/t3l1k3p3.html')

def t4l1k3p3(request):
    return render(request, 'main/p3/lessonk3p3/tl1k3p3/t4l1k3p3.html')

def t1l1k4p3(request):
    return render(request, 'main/p3/lessonk4p3/tl1k4p3/t1l1k4p3.html')

def t2l1k4p3(request):
    return render(request, 'main/p3/lessonk4p3/tl1k4p3/t2l1k4p3.html')

def t3l1k4p3(request):
    return render(request, 'main/p3/lessonk4p3/tl1k4p3/t3l1k4p3.html')

def t4l1k4p3(request):
    return render(request, 'main/p3/lessonk4p3/tl1k4p3/t4l1k4p3.html')

def t1l1k1p4(request):
    return render(request, 'main/p4/lessonk1p4/tl1k1p4/t1l1k1p4.html')

def t2l1k1p4(request):
    return render(request, 'main/p4/lessonk1p4/tl1k1p4/t2l1k1p4.html')

def t3l1k1p4(request):
    return render(request, 'main/p4/lessonk1p4/tl1k1p4/t3l1k1p4.html')

def t4l1k1p4(request):
    return render(request, 'main/p4/lessonk1p4/tl1k1p4/t4l1k1p4.html')

def t1l1k2p4(request):
    return render(request, 'main/p4/lessonk2p4/tl1k2p4/t1l1k2p4.html')

def t2l1k2p4(request):
    return render(request, 'main/p4/lessonk2p4/tl1k2p4/t2l1k2p4.html')

def t3l1k2p4(request):
    return render(request, 'main/p4/lessonk2p4/tl1k2p4/t3l1k2p4.html')

def t4l1k2p4(request):
    return render(request, 'main/p4/lessonk2p4/tl1k2p4/t4l1k2p4.html')

def t1l1k3p4(request):
    return render(request, 'main/p4/lessonk3p4/tl1k3p4/t1l1k3p4.html')

def t2l1k3p4(request):
    return render(request, 'main/p4/lessonk3p4/tl1k3p4/t2l1k3p4.html')

def t3l1k3p4(request):
    return render(request, 'main/p4/lessonk3p4/tl1k3p4/t3l1k3p4.html')

def t4l1k3p4(request):
    return render(request, 'main/p4/lessonk3p4/tl1k3p4/t4l1k3p4.html')

def t1l1k4p4(request):
    return render(request, 'main/p4/lessonk4p4/tl1k4p4/t1l1k4p4.html')

def t2l1k4p4(request):
    return render(request, 'main/p4/lessonk4p4/tl1k4p4/t2l1k4p4.html')

def t3l1k4p4(request):
    return render(request, 'main/p4/lessonk4p4/tl1k4p4/t3l1k4p4.html')

def t4l1k4p4(request):
    return render(request, 'main/p4/lessonk4p4/tl1k4p4/t4l1k4p4.html')