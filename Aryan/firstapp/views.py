from django.shortcuts import render
from .models import *
from .forms import Purchaseform
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')
def index2(request):
    return render(request,'second.html')
def take_input(request):
    user_name=request.POST.get("user_name")
    email_id=request.POST.get("email_id")
    newinput=Database(username=user_name,email=email_id)
    newinput.save()
    return render(request,'second.html')
def show_data(request):
    context={
        "all_data":companyinfo.objects.all(),
        "countone":companyinfo.objects.all().count(),
    }
    return render(request,"show_data.html",context=context)


def showform(request):
    form=Purchaseform(request.POST)
    if(form.is_valid()):
        form.save()
        return render(request,"index.html")
    context={
        "formshow":form,
    }
    return render(request,"form.html",context=context)
def formsubmit(request):
    return render(request,"index.html")

def search(request):
    posts = companyinfo.objects.all()
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        posts = posts.filter(Q(company_name__icontains=search_term)
        )
        context={
            "showvalue":posts,

        }
        return render(request,"search.html",context=context)
    else:
        return render(request,"search.html",{})
    
     

    # mydata=companyinfo.objects.filter(Q(contact__icontains=value))
    # context={
    #     "searchdata":mydata,
    # }
    # return render(request,"display.html",context)

def formdisplay(request):
    return render(request,"display.html")


