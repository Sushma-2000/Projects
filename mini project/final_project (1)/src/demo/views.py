from __future__ import unicode_literals
import math
import re

from django.db.models.query import EmptyQuerySet
from .nav_test import *
import requests
from fuzzywuzzy import fuzz
from .cosine_similarity import *
# upgrade gensim if you can't import softcossim
from gensim.matutils import softcossim 
from gensim import corpora
import gensim.downloader as api
from gensim.utils import simple_preprocess
fasttext_model300 = api.load('fasttext-wiki-news-subwords-300')

def semantic(model,answer):
  soft=[]
  for model_answer in model:
    documents=[model_answer,answer]
    dictionary=corpora.Dictionary([simple_preprocess(doc) for doc in documents])
    # Prepare the similarity matrix
    similarity_matrix = fasttext_model300.similarity_matrix(dictionary, tfidf=None, threshold=0.0, exponent=2.0, nonzero_limit=100)
    # Convert the sentences into bag-of-words vectors.
    text1=dictionary.doc2bow(simple_preprocess(documents[0]))
    text2=dictionary.doc2bow(simple_preprocess(documents[1]))
    soft.append(softcossim(text1,text2, similarity_matrix))
  return (max(soft))

from django import forms
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
import openpyxl, pyexcel
from .models import Oops_userans, Post
from .models import Question,Oops_modelans,Oops_userans,User,Dbms_Question,Dbms_modelans,Dbms_userans,Os_modelans,Os_Question,Os_userans



from django.shortcuts import render, get_object_or_404
import openpyxl, pyexcel
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
 
def post_list_view(request):
    post_objects=Post.objects.all()
    context={
        'post_objects':post_objects
    }
    return render(request,"posts/index.html",context)
def user(request):
    
    return render(request,"oops/user.html")
def logout(request):
    try:
        del request.session['email']
        del request.session['password']
    except:
        return render(request,"oops/logout.html")
    return render(request,"oops/logout.html")
def uservalidate(request):
    email=request.POST.get("email")
    password=request.POST.get('password')
    request.session['email']=email
    request.session['password']=password
    """userobj=User(mailid=email,password=password)
    userobj.save()"""
    user_objects=User.objects.filter(mailid=email,password=password)
    flag=1
    if(user_objects):
        flag=0
        for user in user_objects:
            if(user.taken_test==True):
                return render(request,"oops/user.html",{
                'user_objects':user_objects,"flag":flag,"taken_test":True
            })
            else:
                return render(request,"oops/instructions.html",{
                'user_objects':user_objects,"flag":flag,"taken_test":False
            })
    else:
        flag=1
        return render(request,"oops/user.html",{
        "flag":flag,'user_objects':user_objects,
    })
    
def question_list_view(request):
    email=request.session['email']
    password=request.session['password']
    question_objects=Question.objects.all()
    context={
        'question_objects':question_objects
    }
    return render(request,"oops/questions.html",context)
def dbms_question_list_view(request):
    email=request.session['email']
    password=request.session['password']
    question_objects=Dbms_Question.objects.all()
    context={
        'question_objects':question_objects
    }
    return render(request,"oops/dbms_questions.html",context)
def os_question_list_view(request):
    email=request.session['email']
    password=request.session['password']
    question_objects=Os_Question.objects.all()
    context={
        'question_objects':question_objects
    }
    return render(request,"oops/os_questions.html",context)

def storeans(request):
        if request.method == 'POST':
            email=request.session['email']
            password=request.session['password']
            question_objects=Question.objects.all()
            flag=0
            anslist=[]
            returnlist=[]
            sum=0
            for i in range(0,len(question_objects)+1):
                s=str(i)
                if request.POST.get(s):
                    answer= request.POST.get(s)
                    anslist.append(answer)
                    if(len(Oops_userans.objects.filter(mailid=email))>=5):
                        userans=Oops_userans.objects.filter(mailid=email,num=i).update(answer=answer)
                    else:
                        userans=Oops_userans(mailid=email,answer=answer,num=i)
                        userans.save()
                    print(userans)
                    
                if(i==len(question_objects)):
                    flag=1
            if flag==1:
                #for i in range(1,11):
                """     model_ans=Oops_modelans.objects.get(id=str(i))
                    user_ans=Oops_userans.objects.get(id=(str(i)))
                    returnvar=givVal.givVal(model_ans,user_ans)"""
                answer1_list=Oops_modelans.objects.values_list('answer1')
                answer2_list=Oops_modelans.objects.values_list('answer2')
                answer3_list=Oops_modelans.objects.values_list('answer3')
                userans_list=Oops_userans.objects.filter(mailid=email)
                x=[]
                returnlist=[]
                nblist=[]
                semlist=[]
                sum=0
                for i,userans,answer1,answer2,answer3 in zip(range(0,len(question_objects)+1),userans_list,answer1_list,answer2_list,answer3_list):
                    userans=str(userans_list[i])
                    answer1=' '.join(answer1_list[i])
                    answer2=' '.join(answer2_list[i])
                    answer3=' '.join(answer3_list[i])
                    x.append(userans)
                    model_list=[answer1,answer2,answer3]
                    
                    if(userans in model_list):
                        returnvar=100
                    else:
                        returnvar=givVal(model_list,userans)
                    nbclass=predict_class(model_list,userans)
                    sum+=returnvar
                    returnlist.append(str(returnvar))
                    semlist.append(semantic(model_list,userans))
                    nblist.append(str(nbclass))
                average=sum/len(question_objects)
                combo=zip(returnlist,nblist,semlist)
                user=User.objects.filter(mailid=email).update(oops_score=average)
                if(user):
                    s="done"
                context={"returnlist":returnlist,"average":average,"s":s,"ans":x,"nblist":combo}
                return render(request,'oops/success.html',context) 
            else:
                context={"question_objects":question_objects}
                return render(request,'oops/questions.html',context)
def dbms_storeans(request):
        if request.method == 'POST':
            email=request.session['email']
            question_objects=Dbms_Question.objects.all()
            flag=0
            anslist=[]
            returnlist=[]
            sum=0
            for i in range(0,len(question_objects)+1):
                s=str(i)
                if request.POST.get(s):
                    answer= request.POST.get(s)
                    anslist.append(answer)
                    if(len(Dbms_userans.objects.filter(mailid=email))>=5):
                        userans=Dbms_userans.objects.filter(mailid=email,num=i).update(answer=answer)
                    else:
                        userans=Dbms_userans(mailid=email,answer=answer,num=i)
                        userans.save()
                if(i==len(question_objects)):
                    flag=1
            if flag==1:
                #for i in range(1,11):
                    #model_ans=Oops_modelans.objects.get(id=str(i))
                    #user_ans=Oops_userans.objects.get(id=(str(i)))
                    #returnvar=givVal.givVal(model_ans,user_ans)"""
                answer1_list=Dbms_modelans.objects.values_list('answer1')
                answer2_list=Dbms_modelans.objects.values_list('answer2')
                answer3_list=Dbms_modelans.objects.values_list('answer3')
                userans_list=Dbms_userans.objects.filter(mailid=email)
                x=[]
                returnlist=[]
                nblist=[]
                sum=0
                semlist=[]
                for i,userans,answer1,answer2,answer3 in zip(range(0,len(question_objects)+1),userans_list,answer1_list,answer2_list,answer3_list):
                    userans=str(userans_list[i])
                    answer1=' '.join(answer1_list[i])
                    answer2=' '.join(answer2_list[i])
                    answer3=' '.join(answer3_list[i])
                    model_list=[answer1,answer2,answer3]
                    x.append(userans)
                    if(userans in model_list):
                        returnvar=100
                    else:
                        returnvar=givVal(model_list,userans)
                    nbclass=predict_class(model_list,userans)
                    nblist.append(nbclass)
                    semlist.append(semantic(model_list,userans))
                    sum+=returnvar
                    returnlist.append(str(returnvar))
                average=sum/len(question_objects)
                user=User.objects.filter(mailid=email).update(dbms_score=average)
                combo=zip(returnlist,nblist,semlist)
                if(user):
                    s="done"
                context={"returnlist":returnlist,"average":average,"s":s,"ans":x,"nblist":combo}
                return render(request,'oops/dbms_success.html',context) 
            else:
                context={"question_objects":question_objects}
                return render(request,'oops/dbms_questions.html',context)
def os_storeans(request):
        if request.method == 'POST':
            email=request.session['email']
            question_objects=Os_Question.objects.all()
            flag=0
            anslist=[]
            returnlist=[]
            sum=0
            for i in range(0,len(question_objects)+1):
                s=str(i)
                if request.POST.get(s):
                    answer= request.POST.get(s)
                    anslist.append(answer)
                    if(len(Os_userans.objects.filter(mailid=email))>=5):
                        userans=Os_userans.objects.filter(mailid=email,num=i).update(answer=answer)
                    else:
                        userans=Os_userans(mailid=email,answer=answer,num=i)
                        userans.save()
                if(i==len(question_objects)):
                    flag=1
            if flag==1:
                #for i in range(1,11):
                    #model_ans=Oops_modelans.objects.get(id=str(i))
                    #user_ans=Oops_userans.objects.get(id=(str(i)))
                    #returnvar=givVal.givVal(model_ans,user_ans)"""
                answer1_list=Os_modelans.objects.values_list('answer1')
                answer2_list=Os_modelans.objects.values_list('answer2')
                answer3_list=Os_modelans.objects.values_list('answer3')
                userans_list=Os_userans.objects.filter(mailid=email)
                x=[]
                returnlist=[]
                sum=0
                nblist=[]
                semlist=[]
                for i,userans,answer1,answer2,answer3 in zip(range(0,len(question_objects)+1),userans_list,answer1_list,answer2_list,answer3_list):
                    userans=str(userans_list[i])
                    answer1=' '.join(answer1_list[i])
                    answer2=' '.join(answer2_list[i])
                    answer3=' '.join(answer3_list[i])
                    model_list=[answer1,answer2,answer3]
                    x.append(userans)
                    if(userans in model_list):
                        returnvar=100
                    else:
                        returnvar=givVal(model_list,userans)
                    nbclass=predict_class(model_list,userans)
                    nblist.append(nbclass)
                    semlist.append(semantic(model_list,userans))
                    sum+=returnvar
                    returnlist.append(str(returnvar))
                average=sum/len(question_objects)
                user=User.objects.filter(mailid=email).update(os_score=average)
                combo=zip(returnlist,nblist,semlist)
                if(user):
                    s="done"
                context={"returnlist":returnlist,"average":average,"s":s,"ans":x,"nblist":combo}
                return render(request,'oops/os_success.html',context) 
            else:
                context={"question_objects":question_objects}
                return render(request,'oops/os_questions.html',context)
def final(request):
    email=request.session['email']
    password=request.session['password']
    user_objects=User.objects.filter(mailid=email,password=password)
    user_objects1=User.objects.filter(mailid=email,password=password).update(taken_test=True)
    context={
    'user_objects':user_objects
    }
    return render(request,"oops/final.html",context)
# Download the FastText model
def givVal(model_answer,answer):
    out_of=5
    if (len(answer.split())) <= 5:
        return 0
    temp=givKeywordsValue(model_answer, answer)
    #softcosine=semantic(model_answer,answer)
    k1 = temp[1]
    k2=  temp[0]
    req = requests.get("https://api.textgears.com/check.php?text=" + answer + "&key=iJyw2qQ7eLW5iUFd")
    no_of_errors = len(req.json()['errors'])
    g2=0
    if no_of_errors > 5 or k1 == 6:
        g = 0
    else:
        g = 1
        g2=100
    q1 = math.ceil(fuzz.token_set_ratio(model_answer, answer) * 6 / 100)
    q2 = (fuzz.token_set_ratio(model_answer, answer))
    print("Keywords : ", k1)
    print("Grammar  : ", g)
    print("QST      : ", q1)
    predicted =predict(k1, g, q1)
    #predicted=5
    result = predicted * out_of / 10
    #percentage=math.ceil(((k2*0.60)+(g2*0.05)+(q2*0.15)/3))
    percentage=math.ceil(((k2*1)+(g2*0)+(q2*0)))
    return percentage
def predict_class(model_answer,answer):
    out_of=5
    if (len(answer.split())) <= 5:
        return 0
    temp=givKeywordsValue(model_answer, answer)
    #softcosine=semantic(model_answer,answer)
    k1 = temp[1]
    k2=  temp[0]
    req = requests.get("https://api.textgears.com/check.php?text=" + answer + "&key=iJyw2qQ7eLW5iUFd")
    no_of_errors = len(req.json()['errors'])
    g2=0
    if no_of_errors > 5 or k1 == 6:
        g = 0
    else:
        g = 1
        g2=100
    q1 = math.ceil(fuzz.token_set_ratio(model_answer, answer) * 6 / 100)
    q2 = (fuzz.token_set_ratio(model_answer, answer))
    print("Keywords : ", k1)
    print("Grammar  : ", g)
    print("QST      : ", q1)
    predicted =predict(k1, g, q1)
    #predicted=5
    result = predicted * out_of / 10
    #percentage=math.ceil(((k2*0.60)+(g2*0.05)+(q2*0.15)/3))
    percentage=math.ceil(((k2*1)+(g2*0)+(q2*0)))
    return predicted
# Create your views here.


