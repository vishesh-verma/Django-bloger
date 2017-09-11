# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import blogsSerializers
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,Http404
from .models import blogs
from .models import login


class blogsList(APIView):

    def get(self,request):
        blogss=blogs.objects.all()
        serializers=blogsSerializers(blogss, many=True)
        return Response(serializers.data)


global pass1
def index(request):

    return render(request,"blog/index.html")# invoking view function



def view(request):
    data=blogs.objects.all()
    context={
    'data':data,
    }

    login_data=login.objects.all()
    context2={
     'login_data': login_data
    }
    user=request.POST["username"]
    passward=request.POST["passward"]
    global pass1
    try:
        pass1=login.objects.get(passward=passward,username=user)
    except login.DoesNotExist:
        raise Http404("you have entered a wrong passward")

    return HttpResponseRedirect("/blog/showadd/")
    #return render(request,"blog/details.html",context)
def showadd(request):

    return render(request,"blog/write.html")




def add(request):
    data=blogs.objects.all()
    context={
        'data':data,
    }
    title1=request.POST["title"]
    add=request.POST["blog"]
    global a
    a=blogs(title=title1,para=add,log_in=pass1)
    a.save()
    if a.para == "":
        a.delete()
    return HttpResponseRedirect("/blog/show/")

def show(request):

    blog_= pass1.blogs_set.all()

    context3={
    'blog_':blog_
    }

    return render(request,"blog/show.html",context3)
def signup(request):
         a=0;
         alllogins=login.objects.all()
         user1=request.POST["username1"]
         passward1=request.POST["passward1"]
         b=login(username=user1,passward=passward1)
         for i in alllogins:
             if(i==b):
                 a=a+1;
         if(a>0):
             return HttpResponseRedirect("/blog/signupaf/")
         else:
             b.save()
         return HttpResponseRedirect("/blog/signupaf/")
def signupaf(request):
             return render(request,"blog/index.html")

def delete(request):
    d=request.POST["delete"]
    c=blogs.objects.get(pk=d)
    c.delete()
    return HttpResponseRedirect("/blog/show/")
