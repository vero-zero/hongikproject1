from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Main_User

def startmain(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        if nickname != "":
            if Main_User.objects.filter(nickname=nickname).exists():
                messages.error(request,'이미 사용중인 닉네임입니다.')
                return redirect('/main/startmain/?msg=1')        
            u = Main_User()
            u.nickname = nickname
            u.save()
            return redirect('/game/startgame/',{})
        return render(request, 'main/main.html', {})
    return render(request, 'main/main.html', {})
def static(request):
    return render(request, '/static.html')