from django.urls import path
from . import views

urlpatterns = [
    #аутентификация
    path('login/', views.login_view, name='login'),
    path('regist/', views.regist, name='regist'),
    path('logout/', views.logout_view, name='logout'),
    
    #главная страница
    path('', views.index, name='home'),
    
    #динамические маршруты
    path('place/<slug:slug>/', views.PlaceDetailView.as_view(), name='place_detail'),
    path('place/<slug:place_slug>/course/<int:course_number>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('place/<slug:place_slug>/course/<int:course_number>/subject/<slug:subject_slug>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('topic/<int:pk>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('topic/<int:topic_id>/submit/', views.SubmitTestView.as_view(), name='submit_test'),
]