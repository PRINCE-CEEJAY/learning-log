from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Lesson
from .forms import LessonForm
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'home.html')

@login_required(login_url='/admin/')
def lesson_list_create_view(request):    
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.user = request.user
            lesson.save()
            context = {'lesson': lesson }
            return render(request, 'lessons/partials/lesson-item.html', context) 
    return render(request, 'lessons/partials/add-lesson.html', {'form': LessonForm()})
        


@login_required
def get_lessons(request):
    lessons = Lesson.objects.filter(user=request.user).order_by('-created_at') 
    if request.htmx:
        query = request.GET.get('search', '')
        import time
        time.sleep(2)
        lessons = request.user.lesson.filter(Q(topic__icontains=query) | 
                            Q(summary__icontains=query))
        return render(request, 'lessons/partials/lesson-list.html', {'lessons': lessons})   
    
    context = {'lessons': lessons, 'form': LessonForm()}
    return render(request, 'lessons/lesson-list.html', context)


@login_required(login_url='/admin/')
def lesson_update(request, id):
    lesson = get_object_or_404(Lesson, id=id, user=request.user)
    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            updated = form.save()
            context = {'lesson': updated}
            return render(request, 'lessons/partials/lesson-item.html', context)        

    context = {'form': LessonForm(instance=lesson), 'lesson': lesson}
    return render(request, 'lessons/partials/update-lesson.html', context)

def get_details(request, id):
    lesson = get_object_or_404(Lesson, id=id, user=request.user)
    return render(request, 'lessons/partials/lesson-detail.html', {'lesson': lesson})

def lesson_delete(request, id):
    lesson = get_object_or_404(Lesson, id=id, user=request.user)
    lesson.delete()
    return HttpResponse("")