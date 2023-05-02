from django.shortcuts import render
from main.models import Main_User
# Create your views here.

def endgame(request):
    lastuser =  Main_User.objects.latest('id')
    lastnick = lastuser.nickname
    lastscore = lastuser.score
    return render (request, 'end/end.html' , {'lastnick':lastnick,'lastscore':lastscore})