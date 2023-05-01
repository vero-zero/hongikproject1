from django.shortcuts import render
from main.models import Main_User
# Create your views here.

def endgame(request):
    userscore =  Main_User.objects.get(nickname_list)
    nickname_list =  [ni.nickname for ni in userscore]
    score_list = [ sc.score for sc in userscore]
    return render (request, 'end/end.html' , {'nickname_list':nickname_list})