from django.shortcuts import render, get_object_or_404
from .models import Lesson
from .forms import LessonForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'home.html')

@login_required(login_url='/admin/')
def create_lesson(request):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.user = request.user
            lesson.save()
            context = {'lesson': lesson }
            return(request, 'partials/lesson-detail.html', context) 
        
    context = {'form': LessonForm()}
    return render(request, 'partials/add-lesson.html', context)

    
def get_lessons(request):
        lessons = Lesson.objects.filter(user=request.user).order_by('-created_at')    
        context = {'lessons': lessons, 'form': LessonForm()}
        return render(request, 'lesson-list.html', context)

def get_lesson(request, id):
    lesson = get_object_or_404(Lesson, id=id, user=request.user)
    context = {'lesson': lesson}
    return render(request, 'partials/lesson-detail.html', context)
            

@login_required(login_url='/admin/')
def lesson_update(request, id):
    if request.method == "POST":
        lesson = get_object_or_404(Lesson, id=id, user=request.user)
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.save()
            context = {'lesson': updated}
            return render(request, 'partials/-lesson-detail.html', context)        
        
    context = {'form': LessonForm()}
    return render(request, 'partials/update-lesson.html', context)


def lesson_delete(request, id):
    if request.method == "DELETE":
        lesson = get_object_or_404(Lesson, id=id, user=request.user)
        lesson.delete()
        return ""