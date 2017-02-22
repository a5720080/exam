from django.shortcuts import render,get_object_or_404
from .models import Exam ,Quiz,Choice
from django.http import HttpResponse

def index(request):
    # get all published exams
    exam_pub = Exam.objects.filter(published=True)
    context = {'exam_pub':exam_pub}
    
    
    return render(request, 'index.html', context)



def detail(request, exam_id):
    try:
        exam = Exam.objects.get(pk=exam_id)
    except Exam.DoesNotExist:
        raise Http404("Exam does not exist")
    return render(request, 'detail.html', {'exam': exam})

def score(request,exam_id):
    exam = Exam.objects.get(pk=exam_id)
    score = 0
    try:
        for i in range (1,exam.quiz_set.count()+1):
            answer = request.POST.get("quiz"+str(i))
            selected_choice = Choice.objects.get(pk=answer)
            if selected_choice.corrected:
                score = score + 1
                 
            else:
                print("quiz"+str(i))
    except:
        pass
    context = {'score':score , 'exam':exam  }  
    return render(request,'score.html',context)    

