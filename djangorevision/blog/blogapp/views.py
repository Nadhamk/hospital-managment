from django.shortcuts import render, redirect
from .models import Post,Data,Login
from django.contrib.auth import logout

# Create your views here.

def forms(request):
    title=request.POST['title']
    content=request.POST['content']
    author=request.POST['author']
    data=Post(title=title,content=content,author=author)
    data.save()
    
    return render(request,"index.html")

def show(request):
    data=Post.objects.all()
    return render(request,"forms.html",{"results":data})

def registerpg(request):
    return render(request,"registerpg.html")

def registerview(request):
    name=request.POST['name']
    username=request.POST['username']
    password=int(request.POST['password'])
    info=Data(name=name, username=username,password=password)
    info.save()
    
    logdata=Login(username=username,password=password,type=1)
    logdata.save() 
    return render(request,"registerpg.html")


def index(request):
    return render(request,"index.html")

def updateData(request,pk):
    edit=Post.objects.get(id=pk)
    if request.method=='POST':
        edit.title=request.POST.get('title')
        edit.content=request.POST.get('content')
        edit.author=request.POST.get('author')
        edit.save()
        return redirect('show')  
    else:
        return render(request,'updatepost.html')

def deleteData(request,id):
    d=Post.objects.get(id=id)
    d.delete()
    return redirect("/")

def loginpg(request):
    return render(request,"loginpg.html")

def check(request):
    username=(request.POST['username'])
    password=(request.POST['password'])
    logdata=Login.objects.get(username=username,password=password)
    if logdata.type==1:
        request.session['username']=logdata.username
        return render(request,'index.html')
    elif logdata.type==0:
       request.session["username"]=logdata.username
       return render(request,'updatepost.html')
   
def logoutuser(request):
    logout(request)
    return redirect('login')
        





