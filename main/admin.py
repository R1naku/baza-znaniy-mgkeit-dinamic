from django.contrib import admin
from .models import Place, Course, Subject, Topic, Question, Answer, UserProgress


class AnswerInline(admin.TabularInline):
    """Inline для вариантов ответов внутри вопроса"""
    model = Answer
    extra = 4
    fields = ['text', 'is_correct', 'order']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text_short', 'topic', 'question_type', 'points', 'order', 'is_active']
    list_filter = ['question_type', 'is_active', 'topic__subject__course__place']
    search_fields = ['text', 'topic__title']
    list_editable = ['order', 'is_active']
    inlines = [AnswerInline]
    
    def text_short(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_short.short_description = 'Текст вопроса'


class QuestionInline(admin.StackedInline):
    """Inline для вопросов внутри темы"""
    model = Question
    extra = 0
    fields = ['text', 'question_type', 'points', 'order', 'is_active']
    show_change_link = True


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'order', 'is_active', 'created_at', 'questions_count']
    list_filter = ['is_active', 'subject__course__place', 'subject__course', 'subject']
    search_fields = ['title', 'content']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [QuestionInline]
    fieldsets = (
        ('Основная информация', {
            'fields': ('subject', 'title', 'slug', 'order', 'is_active')
        }),
        ('Содержание', {
            'fields': ('content',),
            'classes': ('wide',)
        }),
    )
    
    def questions_count(self, obj):
        return obj.questions.count()
    questions_count.short_description = 'Вопросов'


class TopicInline(admin.TabularInline):
    """Inline для тем внутри предмета"""
    model = Topic
    extra = 0
    fields = ['title', 'order', 'is_active']
    show_change_link = True


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'icon', 'order', 'is_active', 'topics_count']
    list_filter = ['is_active', 'course__place', 'course']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [TopicInline]
    
    def topics_count(self, obj):
        return obj.topics.count()
    topics_count.short_description = 'Тем'


class SubjectInline(admin.TabularInline):
    """Inline для предметов внутри курса"""
    model = Subject
    extra = 0
    fields = ['name', 'slug', 'icon', 'order', 'is_active']
    show_change_link = True


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'place', 'number', 'is_active', 'subjects_count']
    list_filter = ['place', 'number', 'is_active']
    search_fields = ['description']
    list_editable = ['is_active']
    inlines = [SubjectInline]
    
    def subjects_count(self, obj):
        return obj.subjects.count()
    subjects_count.short_description = 'Предметов'


class CourseInline(admin.TabularInline):
    """Inline для курсов внутри площадки"""
    model = Course
    extra = 0
    fields = ['number', 'is_active']
    show_change_link = True


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'color', 'order', 'is_active', 'courses_count']
    list_filter = ['is_active']
    search_fields = ['name', 'address']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CourseInline]
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'address', 'slug', 'order', 'is_active')
        }),
        ('Оформление', {
            'fields': ('color',),
            'description': 'Цвет темы для площадки (hex код, например #008cff)'
        }),
    )
    
    def courses_count(self, obj):
        return obj.courses.count()
    courses_count.short_description = 'Курсов'


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'topic', 'is_completed', 'score', 'max_score', 'percentage', 'attempts', 'last_attempt_at']
    list_filter = ['is_completed', 'topic__subject__course__place', 'last_attempt_at']
    search_fields = ['user__username', 'user__email', 'topic__title']
    readonly_fields = ['last_attempt_at', 'percentage']
    date_hierarchy = 'last_attempt_at'
    
    def percentage(self, obj):
        return f"{obj.percentage}%"
    percentage.short_description = 'Процент'
