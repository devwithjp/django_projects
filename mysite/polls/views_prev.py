

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
# from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    context={ 'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
#	try:
#		question = Question.objects.get(pk=question_id)
#	except Question.DoesNotExist:
#		raise Http404("Question does not exist")
	question = get_object_or_404(Question,pk=question_id)
	return render(request,"polls/detail.html",{'question':question})

def results(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request, 'polls/results.html',{'question':question})

def vote(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	try:
		c = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{'question':question, 'error_message':'You did not select a choice',})
	else:
		c.votes +=1
		c.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

def owner(request):
       return HttpResponse("Hello, world. 3d1c8c0a is the polls index.")
