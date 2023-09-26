from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def apr(request, day_id):
    return render(request, 'challenges/apr/' + str(day_id) + '.html')

def may(request, day_id):
    return render(request, 'challenges/may/' + str(day_id) + '.html')

def jun(request, day_id):
    return render(request, 'challenges/jun/' + str(day_id) + '.html')

def jul(request, day_id):
    return render(request, 'challenges/jul/' + str(day_id) + '.html')

def aug(request, day_id):
    return render(request, 'challenges/aug/' + str(day_id) + '.html')

def sep(request, day_id):
    return render(request, 'challenges/sep/' + str(day_id) + '.html')

def dsa(request, topic='dsaindex'):
    return render(request, 'dsa/'+ topic + '.html')

def articles(request, topic):
    return render(request, 'articles/'+ topic + '.html')