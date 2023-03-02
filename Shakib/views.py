
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render , redirect
from .forms import userForm

from service.models import service,Contact
from news.models import News
from django.core.paginator import Paginator

def aboutUs(request):
    if request.method == "GET" :
         result = request.GET.get("res")
    return render(request,"about.html",{"result":result})
def index(request):
    # data={
    #     "title":"new page",
    #     "name":"Shakib",
    #     "courselist":["c++","Python","C","Java"],
    #     "numbers":[67,90,78,99,100,89],
    #     "student_details":[
    #         {"name":"Shakib", "phone":"01741162765"},
    #         {"name":"Hasan","phone":"12137443535"}
    #     ] 
        # list of dictionary inside a dictionary

    # }
    # Hidding service part
    # servicedata = service.objects.all().order_by("service_icon") #it will give me all data
    servicedata = service.objects.all()
    news_data = News.objects.all()
    if request.method =="GET":
         s = request.GET.get("servicename")
         if s !=None:
            servicedata = service.objects.filter(service_title__icontains=s)
    
  
    # # l = len(servicedata)
    # data={
    #      "servicedata":servicedata,
    #     #  "le":l, 
    #      "Newsdata":news_data
    # }
    
    pagi = Paginator(servicedata,2)
    page_number = request.GET.get("page") #here page will go to url
    showdata = pagi.get_page(page_number)
    print(showdata)
    totalpage = showdata.paginator.num_pages
    data={
         "servicedata":showdata,
         "pagelist":[n+1 for n in range(totalpage)],
         "Newsdata":news_data,
    }

    return render(request,"index.html",data)

def course(request):
    return HttpResponse("Welcome to course page")

def aboutdetails(request,courseid):
    return HttpResponse(courseid)

def form(request):
    
    
    f = userForm()
    output={"form":f}
    res=0
    try:
        # if request.method =="POST":

            # n1 = int(request.POST['num1'])
            # n2 =  int(request.POST['num2'])
            # res = n1+n2
            output={
                 "form":f,
                 "res":res
            }
            # url = "/about/?res={}".format(res)
            # return redirect(url)
    except:
        pass
    return render(request,"userform.html",output)

def submit(request):
     return HttpResponse(request)


def calculator(request):
    c=""
    try:
         if request.method=="POST":
              n1 = eval(request.POST.get("num1"))
            #   eval will handle int and float
              n2 = eval(request.POST.get("num2"))
              opr = request.POST.get("operator")
              if opr == "+":
                   c = n1+n2
              elif opr == '-':
                   c = n1-n2
              elif opr == '*':
                   c = n1*n2
              elif opr == '/':
                   c = n1/n2
    
    
    except:
         c="invalid operation"
    print(c)
    return render(request,"calculator.html",{"c":c})


def evenodd(request):
    c=''
    if request.POST.get("num1")=="":
         return render(request,"evenodd.html", {"error":True})
    else:  
        try:
            if request.method =="POST":
                n=eval(request.POST.get("num1"))
                if n%2==0:
                    c="even"
                else:
                    c="odd"
        except:
            c="invalid operation"
    return render(request,"evenodd.html",{"c":c})



def newsdetails(request,newsid):
     singlenews = News.objects.get(id=newsid) 
     #for fetching a single data we use objects.get insted of objects.all . here id is holding the newsid which we have passed through url
     data={
          "newsdata":singlenews,
     }
     return render(request,"newsdetails.html",data)


def contact(request):
     n=''
     if request.method =="POST":
          name = request.POST.get("name")
          email = request.POST.get("email")
          password = request.POST.get("password")
          address= request.POST.get("address")
          city = request.POST.get("city")
          #inside contact left side- field name of contact class, right side->value
          final = Contact(name=name,email=email,password=password,address=address,city=city)
          final.save()
          n="Data Insserted"
     userdata = Contact.objects.all()
     data ={
          "n":n,
          "userdata":userdata
     }
     return render(request,"contact.html",data)