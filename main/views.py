from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Main_User

def startmain(request):
    if request.method == 'POST':
        print(1)
        name = request.POST.get('nickname')
        if name != "":
            if Main_User.objects.filter(nickname=name).exists():
                messages.error(request,'이미 사용중인 닉네임입니다.')
                return redirect('/main/startmain/?msg=1')        
            u = Main_User()
            u.nickname = name
            u.save()
            print(2, name)
            return redirect('/game/startgame/',{})
        return render(request, 'main/main.html', {})
    return render(request, 'main/main.html', {})
def static(request):
    return render(request, '/static.html')