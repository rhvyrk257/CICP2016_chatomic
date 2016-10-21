from django.shortcuts import render,redirect,render_to_response,get_list_or_404,get_object_or_404
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from django.forms.formsets import formset_factory
from . import forms,models
import re,glob,random

#トップページを設定
def index(request):
    person_num=0
    bubble_num=0
    flags=0
    message=""
    image="img/test.png"
    ### フォームを読み込む
    # このコマを使うか使わないか（喋っている人が１人以上か否か）
    use_form=forms.UseForm(request.GET or None)
    # 吹き出しが何個か
    speaker_form=forms.SpeakerForm(request.GET or None)
    print(request.POST.keys())
    if "confirm" in request.POST:
        if "flag" in request.POST.keys() and "bubble" in request.POST.keys():
            print(request.POST['flag'])
            print(request.POST['bubble'])
            message = "確認：喋っている人："+request.POST['flag']+"人, 吹き出し数："+request.POST['bubble']+"こ"
            person_num=request.POST['flag']
            bubble_num=request.POST['bubble']
            request.session['pre_pnum']=person_num
            request.session['pre_bnum']=bubble_num
        else:
            message = '全ての項目を入力してください'
    elif "regist" in request.POST:
        print(request.session.keys())
        person_num=request.session['pre_pnum']
        bubble_num=request.session['pre_bnum']
        print(person_num)
        print(bubble_num)
        if int(person_num) ==1 and int(bubble_num) >=0 and int(bubble_num) <=2:
            print("使える")
            flags=1
        else:
            print("使えない")
            flags=0
        #登録
        models.ComicInfo.objects.create(
            file_name=image,
            person_num=person_num,
            bubble_num=bubble_num,
            availability=flags,
        )
        print("登録")
        message="登録しました"
        person_num=""
        bubble_num=""
    
    # 変数をページに引き渡す
    d={
        'use_form' : use_form,
        'speaker_form' : speaker_form,
        'image' : image,
        'message' : message,
        'person_num' : person_num,
        'bubble_num' : bubble_num,
    }
    # index.html で表示させる
    return render(request, 'index.html', d)
