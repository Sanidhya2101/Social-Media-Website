from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from social.models import ToDoList,Item
from django.shortcuts import render
from .forms import CreateNewList

# Create your views here.
def index(response,id):
    ls=ToDoList.objects.get(id=id)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()        

        elif response.POST.get("newitem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text= txt,complete = False)     
    return render(response,'social/index.html',{"ls":ls})

def home(request):
    return render(request,'social/base.html',{})
def create(response):
    if response.method == "POST":
        form=CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)   
    else:    
        form= CreateNewList()
    return render(response,"social/create.html",{"form" : form})    