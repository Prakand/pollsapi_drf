from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Poll

# Create your views here.

def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {
        "result" : list(polls.values("question","created_by_username","pub_date"))
    }
    return JsonResponse(data)


def polls_detail(request, pk):
    poll = get_object_or_404(Poll,pk=pk)
    data ={
        "result" : {
            "question" : poll.question,
            "created_by" : poll.created_by_username,
            "pub_date" : poll.pub_date
        }
    }
    return JsonResponse(data)

