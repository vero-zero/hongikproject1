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
    
    #User_Score.objects.create(nickname=Main_User.nickname)
    # DB에서 이미지 목록 가져오기
    items =MyModel.objects.all()
    img_list = [item.img.url for item in items]
    selected_imgs = random.sample(set(img_list), 20)
    context = {'selected_imgs':selected_imgs}

    #user_input_name = request.POST.get('img_name')
    # score = Main_User.objects.latest('nickname').score
    #for  selected_img in enumerate(selected_imgs):
    #    context['selected_img'] = selected_img
    #user = Main_User.objects.latest('nickname')
    #user.score = score
    #user.save()
    return render(request, 'game/game.html', context)


