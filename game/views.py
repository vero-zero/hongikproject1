from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import MyModel #User_Score
from main.models import Main_User

import random

def startgame(request):
    if request.method == 'POST':
        img_names = request.POST.getlist('img_name')
        print(img_names)
        score = 0
        for name in img_names:
            try:
                MyModel.objects.get(name=name)
                score += 1
            except:
                pass
        id = request.session.get('id')
        user = Main_User.objects.get(pk=id)
        user.score = score
        user.save()

        return redirect('/end/endgame/')
    

    # DB에서 이미지 목록 가져오기 
    items =MyModel.objects.all()
    img_list = [item.img.url for item in items]
    selected_imgs = random.sample(set(img_list), 10)#랜덤문으로 40개의 수량만 확보 후 리스트로 재정렬
    context = {'selected_imgs':selected_imgs}

    return render(request, 'game/game.html', context)


