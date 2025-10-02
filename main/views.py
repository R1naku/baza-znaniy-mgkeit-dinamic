from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import JsonResponse
from django.utils import timezone
from .forms import RegistForm, LoginForm
from .models import Place, Course, Subject, Topic, Question, Answer, UserProgress


#авторизация
def regist(request):
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


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username_or_email, password=password)
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


def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('home')


#главная страница
def index(request):
    places = Place.objects.filter(is_active=True)
    return render(request, 'main/index.html', {'places': places})


#динамические представления
class PlaceDetailView(DetailView):
    model = Place
    template_name = 'main/place_detail.html'
    context_object_name = 'place'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = self.object.courses.filter(is_active=True)
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = 'main/course_detail.html'
    context_object_name = 'course'
    
    def get_object(self):
        place = get_object_or_404(Place, slug=self.kwargs['place_slug'])
        return get_object_or_404(Course, place=place, number=self.kwargs['course_number'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = self.object.subjects.filter(is_active=True)
        return context


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'main/subject_detail.html'
    context_object_name = 'subject'
    
    def get_object(self):
        place = get_object_or_404(Place, slug=self.kwargs['place_slug'])
        course = get_object_or_404(Course, place=place, number=self.kwargs['course_number'])
        return get_object_or_404(Subject, course=course, slug=self.kwargs['subject_slug'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topics'] = self.object.topics.filter(is_active=True)
        
        #добавляем список завершенных тем для текущего пользователя
        if self.request.user.is_authenticated:
            completed_topics = UserProgress.objects.filter(
                user=self.request.user,
                topic__subject=self.object,
                is_completed=True
            ).values_list('topic_id', flat=True)
            context['completed_topics'] = list(completed_topics)
        else:
            context['completed_topics'] = []
        
        return context


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'main/topic_detail.html'
    context_object_name = 'topic'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = self.object.questions.filter(is_active=True).prefetch_related('answers')
        
        #subject для навигации
        context['subject'] = self.object.subject
        
        #предыдущую и следующую темы
        all_topics = self.object.subject.topics.filter(is_active=True).order_by('order', 'id')
        topic_list = list(all_topics)
        
        try:
            current_index = topic_list.index(self.object)
            context['prev_topic'] = topic_list[current_index - 1] if current_index > 0 else None
            context['next_topic'] = topic_list[current_index + 1] if current_index < len(topic_list) - 1 else None
        except (ValueError, IndexError):
            context['prev_topic'] = None
            context['next_topic'] = None
        
        return context


class SubmitTestView(LoginRequiredMixin, View):
    def post(self, request, topic_id):
        topic = get_object_or_404(Topic, pk=topic_id)
        
        #подсчет баллов
        score = 0
        max_score = 0
        
        for question in topic.questions.filter(is_active=True):
            max_score += question.points
            
            if question.question_type == 'single':
                #один правильный ответ
                answer_id = request.POST.get(f'question_{question.id}')
                if answer_id and Answer.objects.filter(id=answer_id, is_correct=True).exists():
                    score += question.points
                    
            elif question.question_type == 'multiple':
                #несколько правильных ответов
                answer_ids = request.POST.getlist(f'question_{question.id}')
                correct_answers = set(question.answers.filter(is_correct=True).values_list('id', flat=True))
                selected_answers = set(int(aid) for aid in answer_ids if aid.isdigit())
                
                #начисляем баллы только если выбраны ВСЕ правильные ответы и НЕТ неправильных
                if selected_answers == correct_answers:
                    score += question.points
                    
            elif question.question_type == 'text':
                #текстовый ответ (пока пропускаем, требует ручной проверки)
                pass
        
        #сохранение прогресса
        progress, _ = UserProgress.objects.get_or_create(user=request.user, topic=topic)
        progress.score = score
        progress.max_score = max_score
        progress.attempts += 1
        progress.is_completed = score >= max_score * 0.7
        if progress.is_completed:
            progress.completed_at = timezone.now()
        progress.save()
        
        return JsonResponse({
            'score': score,
            'max_score': max_score,
            'percentage': round((score / max_score * 100) if max_score > 0 else 0, 1),
            'is_completed': progress.is_completed
        })
