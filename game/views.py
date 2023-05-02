from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import MyModel #User_Score
from main.models import Main_User

import random

def startgame(request):
    #User_Score.objects.create(nickname=Main_User.nickname)
    # DB에서 이미지 목록 가져오기
    items =MyModel.objects.all()
    img_list = [item.img.url for item in items]
    selected_imgs = random.sample(set(img_list), 20)
    context = {'selected_imgs':selected_imgs}
    score = 0
    user_input_name = request.POST.get('img_name')
    # score = Main_User.objects.latest('nickname').score
    for  selected_img in enumerate(selected_imgs):
        if request.method == 'POST':
            context['selected_img'] = selected_img
            if  user_input_name is not None and user_input_name.strip():
                if MyModel.objects.filter(name=user_input_name).exists():
                    score += 1

    user = Main_User.objects.latest('nickname')
    user.score = score
    user.save()
    return render(request, 'game/game.html', context)


