from django.shortcuts import render
from main.models import Main_User
# Create your views here.

def endgame(request):
    id = request.session.get('id')
    user =  Main_User.objects.get(id=id)
    nickname = user.nickname
    score = user.score
    return render (request, 'end/end.html' , {'user': user})