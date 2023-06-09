from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Main_User

def startmain(request):
    mvplist = Main_User.objects.filter(score=20)
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
            request.session['id'] = u.id
            request.session['nickname'] = u.nickname

            return redirect('/game/startgame/',{})
        return render(request, 'main/main.html', {'mvplist':mvplist})
    return render(request, 'main/main.html', {'mvplist':mvplist})

def static(request):
    return render(request, '/static.html')
