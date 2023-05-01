from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import MyModel #User_Score
from main.models import Main_User

import random
import time

def startgame(request):
    #User_Score.objects.create(nickname=Main_User.nickname)
    # DB에서 이미지 목록 가져오기
    items =MyModel.objects.all()
    img_list = [item.img.url for item in items]
    print(img_list)
    selected_imgs = random.sample(img_list, 20)
    context = {'selected_imgs':selected_imgs}
    score = 0
    user_input_name = request.POST.get('img_name')
    # score = Main_User.objects.latest('nickname').score
    for i, selected_img in enumerate(selected_imgs):
        if request.method == 'POST':
            context['selected_img'] = selected_img
            if request.POST.get('img_name'):
                if MyModel.objects.filter(name=user_input_name).exists():
                    score += 1
                else :
                    score += 0
            else :
                score += 0
                # 5초 동안 대기
    user = Main_User.objects.latest('nickname')
    user.score = score
    user.save()
    return render(request, 'game/game.html', context)


