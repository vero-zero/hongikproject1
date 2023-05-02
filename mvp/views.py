from django.shortcuts import render,HttpResponse
from main.models import Main_User
# Create your views here.

def mvplist(request):
    mvplist = Main_User.objects.filter(score=10)
    print(len(mvplist))
    return render (request,'mvp/mvp.html',{'mvplist':mvplist})

