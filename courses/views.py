from django.shortcuts import render,get_object_or_404,redirect
from .models import Course
from .forms import CommentForm

# Create your views here.
def index(request):
	return render(request,'index.html')

def courses(request):
	return render(request,'courses.html')

def chemistry(request):
	course_list=Course.objects.filter(categories__title='Chemistry')

	context = {

        'course_list':course_list
    } 	
	return render(request, 'chemistry.html' ,context)

def biology(request):
	course_list=Course.objects.filter(categories__title='Biology')

	context = {

        'course_list':course_list
    } 	
	return render(request, 'biology.html' ,context)


def course_detail(request, course_id):
	course =get_object_or_404(Course,id=course_id)
	form=CommentForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			form.instance.user=request.user
			form.instance.course =course
			form.save()
			return redirect('course_detail',course_id=course_id)
	context ={
	    'course':course,
	    'form':form
	}
	return render(request,'course_detail.html',context)

def contact(request):
	return render(request,'contact.html')
    
    
    
    

