from django.shortcuts import render,redirect,render_to_response,get_list_or_404,get_object_or_404
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from django.forms.formsets import formset_factory
from . import forms,models
import re,glob,random,os
from collections import defaultdict

def select_img(comiclists,PATH):
    done=[]
    not_done=[]

    for categ_id in comiclists.keys():
        print(comiclists[str(categ_id)])
        img_files=glob.glob(PATH+"static/img/"+comiclists[str(categ_id)]+"/*.jpg")
        for image in img_files:
            img_id=re.sub(PATH+"static/img/"+comiclists[str(categ_id)]+"/","",image)
            img_id=re.sub(".jpg","",img_id)
            not_done.append([categ_id,img_id])
            try:
                h=models.ComicInfo.objects.filter(comic_name=int(categ_id)).get(bubble_id=img_id)
                done.append([categ_id,img_id])
            except:
                pass
    print("ぜんぶ",end="")
    print(not_done)
#    try:
#        h=models.Doing.objects.filter(comic_name=categ_id, flag=1)
#        for i in h:
#            done.append([categ_id,str(i.bubble_id)])
#    except:
#        pass
    print("おわった",end="")
    print(done)
    for i in done:
        not_done.remove(i)
    print("まだ",end="")
    print(not_done)
    return not_done

def select_img2(categ_id,PATH):
    img_files=[]
    h=models.ComicInfo.objects.filter(comic_name=categ_id)
    for i in h:
        if i.availability==1:
            if i.x1==0 and i.y1==0:
                print(i.bubble_id)
                img_files.append([categ_id,i.bubble_id])
    print(img_files)
    return img_files

#アノテーション１段階目
def index(request):
    comiclists=defaultdict(lambda:0)
    PATH=os.path.abspath(__file__)
    PATH=re.sub("comic/views.py","",PATH)
    print(PATH)
    with open(PATH+"com.list","r") as f1:
        for line in f1:
            line=line.strip("\n")
            line=line.strip()
            num,name=line.split(" ")
            comiclists[num]=name
    print(comiclists)
    person_num=0
    bubble_num=0
    flags=0
    message=""
    # このコマを使うか使わないか（喋っている人が１人以上か否か）
    use_form=forms.UseForm(request.GET or None)
    # 吹き出しが何個か
    speaker_form=forms.SpeakerForm(request.GET or None)
    image=""
    ### 表示するコマを設定
    img_list=select_img(comiclists,PATH)
    rest=len(img_list)
    if rest==0:
        try:
            print(request.session['comic_name'])
            print(request.session['bubble_id'])
#            h=models.Doing.objects.get(comic_name=request.session['comic_name'],bubble_id=request.session['bubble_id'])
#            h.flag=0
#            h.save()
        except:
            pass
        if 'flag' in request.POST.keys():
            if int(request.POST['flag']) == 1 and int(request.POST['bubble']) >=1 and int(request.POST['bubble']) <=2:
                print("使える")
                flags=1
            else:
                print("使えない")
                flags=0
            models.ComicInfo.objects.create(
                comic_name=request.session['comic_name'],
                bubble_id=request.session['bubble_id'],
                person_num=request.POST['flag'],
                bubble_num=request.POST['bubble'],
                availability=flags,
            )
        print("おわり")
        request.session.flush()
    else:
        print(request.POST.keys())
        if "regist" in request.POST:
            if "flag" in request.POST.keys() and "bubble" in request.POST.keys():
                print(request.POST['flag'])
                print(request.POST['bubble'])
                person_num=request.POST['flag']
                bubble_num=request.POST['bubble']
                request.session['pre_pnum']=person_num
                request.session['pre_bnum']=bubble_num
                if int(person_num) == 1 and int(bubble_num) >=1 and int(bubble_num) <=2:
                    print("使える")
                    flags=1
                else:
                    print("使えない")
                    flags=0
                #登録
                models.ComicInfo.objects.create(
                    comic_name=request.session['comic_name'],
                    bubble_id=request.session['bubble_id'],
                    person_num=person_num,
                    bubble_num=bubble_num,
                    availability=flags,
                )
#                h=models.Doing.objects.get(comic_name=request.session['comic_name'],bubble_id=request.session['bubble_id'])
#                h.flag=0
#                h.save()
                print("登録")
            else:
                message = '全ての項目を入力してください'
        show=random.choice(img_list)
        print("えらぶ",end="")
        print(show)
        comic_name=str(show[0])
        bubble_id=str(show[1])
#        h=models.Doing.objects.get(comic_name=comic_name,bubble_id=bubble_id)
#        h.flag=1
#        h.save()
        request.session['comic_name']=comic_name
        request.session['bubble_id']=bubble_id
        image="img/"+comiclists[comic_name]+"/"+bubble_id+".jpg"

        # 変数をページに引き渡す
    d={
        'use_form' : use_form,
        'speaker_form' : speaker_form,
        'image' : image,
        'message' : message,
        'person_num' : person_num,
        'bubble_num' : bubble_num,
        'rest' : rest,
    }
    # index.html で表示させる
    return render(request, 'index.html', d)

#アノテーション２段階目
def second(request):
    PATH=os.path.abspath(__file__)
    PATH=re.sub("comic/views.py","",PATH)
    print(PATH)
    bubble=[]
    message=""
    image=""
    bubble_num=""
    comic_name=""
    bubble_id=""
    ### フォームを読み込む
    utter_form1=forms.UtterForm1(request.GET or None)
    utter_form2=forms.UtterForm2(request.GET or None)
    positive_form=forms.PositiveForm(request.GET or None)
    ### 表示するコマを設定
    img_list=select_img2(0,PATH)
    rest=len(img_list)
    print("img_list:",end="")
    print(img_list)
    if rest==0:
        print("おわり")
        request.session.flush()
    else:
        print(request.POST.items())
        print(request.session.items())
        # 1回目が押された時
        if "regist0.x" in request.POST:
            if len(request.POST["utter1"])!=0 and "pn" in request.POST.keys():
                print("登録",end="")
                print(request.session["bubble_id"])
                h=models.ComicInfo.objects.get(comic_name=request.session["comic_name"],bubble_id=request.session["bubble_id"])
                h.x1=request.POST["regist0.x"]
                h.y1=request.POST["regist0.y"]
                h.utter1=request.POST['utter1']
                if len(request.POST["utter2"])!=0:
                    h.utter2=request.POST["utter2"]
                h.save()
        # 2回目が押された時
        if "regist1.x" in request.POST and "regist1.y" in request.POST:
            print("登録",end="")
            print(request.session["comic_name"])
            print(request.session["bubble_id"])
            h=models.ComicInfo.objects.get(comic_name=request.session["comic_name"],bubble_id=request.session["bubble_id"])
            h.x2=request.POST["regist1.x"]
            h.y2=request.POST["regist1.y"]
            h.save()
            
        if "bubble_num" in request.session.keys():
            if request.session["bubble_num"]==2 and models.ComicInfo.objects.get(comic_name=request.session["comic_name"],bubble_id=request.session["bubble_id"]).y2==0:
                image="img/"+comiclists[comic_name]+"/"+bubble_id+".jpg"
                image=request.session["image"]
                bubble_num=request.session["bubble_num"]
                comic_name=request.session["comic_name"]
                bubble_id=request.session["bubble_id"]
                bubble=[]
                print(bubble_num)
                for i in range(bubble_num):
                    bubble.append(i)
                    print(bubble)
                
            else:# request.session["bubble_num"]==1:
                #### 表示するコマを設定
                img_list=select_img2(0,PATH)
                rest=len(img_list)
                print(img_list)
                if len(img_list)!=0:
                    show=random.choice(img_list)
                    print("えらぶ",end="")
                    print(show)
                    comic_name=str(show[0])
                    bubble_id=str(show[1])
                    image="img/"+comiclists[comic_name]+"/"+bubble_id+".jpg"
                    request.session["image"]=image
                    print(image)
                    bubble_num=models.ComicInfo.objects.get(comic_name=comic_name, bubble_id=bubble_id).bubble_num
                    print(bubble_num)
                    request.session["bubble_num"]=bubble_num
                    request.session['comic_name']=comic_name
                    request.session['bubble_id']=bubble_id
                    bubble=[]
                    print(bubble_num)
                    for i in range(bubble_num):
                        bubble.append(i)
                        print(bubble)
                else:
                    print("おわり")
        else:
            ### 表示するコマを設定
            #            img_list=select_img2(0,PATH)
            #            rest=len(img_list)
            show=random.choice(img_list)
            print("えらぶ",end="")
            print(show)
            comic_name=str(show[0])
            bubble_id=str(show[1])
            image="img/"+comiclists[comic_name]+"/"+bubble_id+".jpg"
            print(image)
            request.session["image"]=image
            bubble_num=models.ComicInfo.objects.get(comic_name=comic_name, bubble_id=bubble_id).bubble_num
            request.session["bubble_num"]=bubble_num
            request.session['comic_name']=comic_name
            request.session['bubble_id']=bubble_id
            bubble=[]
            print(bubble_num)
            for i in range(bubble_num):
                bubble.append(i)
                print(bubble)

    d={
        'utter_form1' : utter_form1,
        'utter_form2' : utter_form2,
        'image' : image,
        'message' : message,
        'positive_form' : positive_form,
        'bubble_num' : bubble,
        'rest' : rest,
    }
    # index.html で表示させる
    return render(request, 'second.html', d)
