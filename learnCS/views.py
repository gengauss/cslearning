from django.shortcuts import render, redirect
from learnCS.models import Course, Lesson, Exercise, Reference
from django.http import HttpResponse
import operator
from django.db.models import Q

# Admin Page (Select db)
def admindb(request):
    choice = ''
    if request.method == 'POST' and request.POST['dbname']:
        if request.POST['dbname']=='course':
            choice = 'course'
            data = Course.objects.all()
        elif request.POST['dbname']=='lesson':
            choice = 'lesson'
            data = Lesson.objects.all()
        elif request.POST['dbname']=='exercise':
            choice = 'exercise'
            data = Exercise.objects.all()
        elif request.POST['dbname']=='reference':
            choice = 'reference'
            data = Reference.objects.all()
            
        data_dictionary = {'choice':choice, 'data':data}
        return render(request, 'learncs/admin/dbpage.html',data_dictionary)

    return render(request, 'learncs/admin/dbpage.html',{'choice':choice})

# Admin Page (Add db)
def dbAdd(request):
    if request.method == 'POST':
        if request.POST.get('dbAdd_c'):
            new_data = Course(id=request.POST['dbAdd_cId'], title=request.POST['dbAdd_cTitle'])
            new_data.save()
        
        elif request.POST.get('dbAdd_l'):
            new_data = Lesson(id=request.POST['dbAdd_lId'], title=request.POST['dbAdd_lTitle'], content=request.POST['dbAdd_lContent'], course_id=request.POST['dbAdd_lCId'])
            new_data.save()
        
        elif request.POST.get('dbAdd_e'):
            new_data = Exercise(id=request.POST['dbAdd_eId'], title=request.POST['dbAdd_eTitle'], problem=request.POST['dbAdd_eProb'], solution=request.POST['dbAdd_eSol'], course_id=request.POST['dbAdd_eCId'], lesson_id=request.POST['dbAdd_eLId'])
            new_data.save()
        
        elif request.POST.get('dbAdd_r'):
            new_data = Reference(id=request.POST['dbAdd_rId'], title=request.POST['dbAdd_rTitle'], link=request.POST['dbAdd_rLink'], course_id=request.POST['dbAdd_rCId'], lesson_id=request.POST['dbAdd_rLId'])
            new_data.save()
        
        return redirect('/admindb/fulldb')

# Admin Page (Delete db)
def dbDel_C(request, course_id):
    del_data = Course.objects.get(id=course_id)
    del_data.delete()
    return redirect('/admindb/fulldb')

def dbDel_L(request, lesson_id):
    del_data = Lesson.objects.get(id=lesson_id)
    del_data.delete()
    return redirect('/admindb/fulldb')
    
def dbDel_E(request, exercise_id):
    del_data = Exercise.objects.get(id=exercise_id)
    del_data.delete()
    return redirect('/admindb/fulldb')

def dbDel_R(request, reference_id):
    del_data = Reference.objects.get(id=reference_id)
    del_data.delete()
    return redirect('/admindb/fulldb')

# Admin Page (Full dblist)
def fulldb(request):
    courses = Course.objects.all()
    lessons = Lesson.objects.all()
    exercises = Exercise.objects.all()
    references = Reference.objects.all()
    data_dictionary = {'courses':courses, 'lessons':lessons, 'exercises':exercises, 'references':references}
    return render(request, 'learncs/admin/fulldb.html', data_dictionary)

# Create your views here.
def homepage(request):
    courses = Course.objects.all()
    data_dictionary = {'courses':courses}
    return render(request,'learncs/user/homepage.html',data_dictionary)

#tutorial
def index(request,course_id):
    courses = Course.objects.all()
    course = Course.objects.get(pk=course_id)
    lessons = Lesson.objects.filter(course_id=course_id)
    data_dictionary = {'lessons':lessons,'courses':courses}
    return render(request,'learncs/user/index.html',data_dictionary)

def detail(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    #data_dictionary = {'lesson':lesson, 'file':'files/tutorials/'+str(lesson.course_id)+'-'+str(lesson.id)+'.pdf'}
    data_dictionary = {'lesson':lesson}
    return render(request,'learncs/user/detail.html',data_dictionary)

#exercise
def exercise(request, course_id):
    courses = Course.objects.all()
    course = Course.objects.get(pk=course_id)
    lessons = Lesson.objects.filter(course_id=course_id)
    data_dictionary = {'lessons':lessons,'courses':courses}
    return render(request,'learncs/user/exercise.html',data_dictionary)

def problem(request, lesson_id):
    lessons = Lesson.objects.get(pk=lesson_id)
    exercises = Exercise.objects.filter(lesson_id=lesson_id)
    data_dictionary = {'exercises':exercises,'lessons':lessons}
    return render(request,'learncs/user/problem.html',data_dictionary)

def content(request, exercise_id):
    exercises = Exercise.objects.get(pk=exercise_id)
    data_dictionary = {'exercises':exercises}
    return render(request,'learncs/user/content.html',data_dictionary)

def general(request, course_id):
    courses = Course.objects.all()
    Courses = Course.objects.get(pk=course_id)
    data_dictionary = {'Courses':Courses,'courses':courses}
    return render(request, 'learncs/user/general.html', data_dictionary)

#reference
def reference(request,course_id):
    course = Course.objects.get(pk=course_id)
    references = Reference.objects.filter(course_id=course_id)
    data_dictionary = {'references':references}
    return render(request,'learncs/user/reference.html',data_dictionary)


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        lessons = Lesson.objects.filter(title__icontains=q)
        return render(request, 'learncs/user/search.html',
                      {'lessons': lessons, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def showAnswer(request):
    if request.method == 'POST':
        exercises = Exercise.objects.get(pk=exercise_id)
        data_dictionary = {'exercises':exercises}
        return render(request, 'learncs/user/content.html',data_dictionary)
