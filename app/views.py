from django.shortcuts import render
from app.models import *
# Create your views here.

def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)


def display_webpages(request):
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    return render(request,'display_webpages.html',d)

def display_access(request):
    LOA=AccessRecord.objects.all()
    d={'access':LOA}
    return render(request,'display_accessrecords.html',d)



def update_webpages(request):
    #Webpage.objects.filter(topic_name='chess').update(name='GANESH')
    TO=Topic.objects.get_or_create(topic_name='MIND')[0]
    TO.save()
    Webpage.objects.update_or_create(name='GANI',defaults={'topic_name':TO,'url':'http://gani.in','email':'gani@gmail.com'})
    d={'webpages':Webpage.objects.all()}
    return render(request,'display_webpages.html',d)


def delete_webpages(request):
    Webpage.objects.filter(name='GANI').delete()
    d={'webpages':Webpage.objects.all()}
    return render(request,'display_webpages.html',d)


