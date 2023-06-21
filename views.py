from django.shortcuts import render,redirect
from django.http import HttpResponse
from agent.models import User,Agent,Postpackage,Requestpackage
from agent.forms import Signupform,Agentform,Packageform
from django.views.generic import CreateView,ListView,DeleteView
from django.db.models.functions import Coalesce
from django.db.models import Max, Value
from datetime import date
from django.template                import RequestContext
from django.contrib.auth            import authenticate, login

def home(request):
    return render(request,"loginn.html")
class Listuser(ListView):
    template_name ="listofusers.html"
    model = User
    context_object_name = "a"
class Listagent(ListView):
    template_name ="listofagents.html"
    model = Agent
    context_object_name = "a"

def log(request):
    return render(request, "loginhome.html")
def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        obj= Agent.objects.filter(email=email,password=password)
        obj2 = User.objects.filter(email=email, password=password)
        if obj.filter(email=email,password=password).exists():
            for i in obj:
                y = i.aid
                x = i.status
                z = i.aname
                request.session['aname'] = z
                request.session['email'] = email
                request.session['password'] = password
                request.session['aid'] = y
                request.session['status'] = x
                if x == 'A':
                    return render(request, "adminhome.html")
                elif x == "AP":
                    return render(request, "agenthome.html")
                elif x == 'R':
                    return render(request, "rejected.html")
                elif x == 'W':
                    return render(request, "proces.html")
                else:
                    return render(request, "userhome.html")


        elif obj2.filter(email=email,password=password).exists():
            for i in obj2:
                z = i.uid
                request.session['uid'] = z
                return render(request, "userhome.html")
        else:
            return render(request, "invalid.html")
    else:
        return render(request, "login.html")
def agentapprove(request):
    orec=Agent.objects.filter(status='W')
    return render(request,'')
def ch(request):
    a = Agent.objects.filter(status='W')
    return render(request, "agentstatus.html",{"a":a})

def updatestatus(request,aid):
    Agent.objects.filter(aid=aid).update(status='AP')
    return render(request,"adminhome.html")


def agentreject(request,aid):
    Agent.objects.filter(aid=aid).update(status='R')
    return render(request, "adminhome.html")

def editagent(request):
    aid=Agent.objects.get(pk=request.session['aid'])  #rec variable rcode is theid
    form=Agentform(instance=aid)
    return render(request,'agentupdate.html',{"form":form,"aid": aid})


def updateagent(request):
    aid=Agent.objects.get(pk=request.session['aid'])
    form=Agentform(request.POST,instance=aid)
    if form.is_valid():
        form.save()
        return render(request, 'rejected.html',{"aid":aid})
    return render(request,'agenthome.html',{"aid":aid})
def deleteagent(request,aid):
    a = Agent.objects.get(aid=aid)
    a.delete()
    return render(request, "adminhome.html")
def usereg(request):
    if request.method=="POST":
        a=request.POST.get('uname')
        b=request.POST.get("phoneno")
        c=request.POST.get("state")
        d=request.POST.get("district")
        e=request.POST.get("address")
        f=request.FILES.get("photo")
        g=request.POST.get("email")
        h=request.POST.get("password")
        if User.objects.filter(email=g):
            msg= {'msg1' : 'email already exists'}
            return render(request, 'emailalreday.html',msg)
        else:
            va=User(uname=a,phoneno=b,state=c,district=d,address=e,photo=f,email=g,password=h)
            va.save()

            return render(request,"index.html")
    else:
        return render(request,'userr.html')
def agentreg(request):
    if request.method=="POST":
        a=request.POST.get('aname')
        b=request.POST.get("phoneno")
        c=request.POST.get("state")
        d=request.POST.get("district")
        i=request.POST.get("area")
        e=request.POST.get("address")
        f=request.FILES.get("photo")
        j=request.POST.get("agender")
        k=request.FILES.get("verification")
        r=request.FILES.get("certification")
        g=request.POST.get("email")
        h=request.POST.get("password")
        if Agent.objects.filter(email=g):
            msg= {'msg1' : 'email already exists'}
            return render(request, 'emailalreday.html',msg)
        else:
            aa = Agent(aname=a, phoneno=b, state=c, district=d, area=i, address=e, photo=f, agender=j, verification=k,
                       certification=r, email=g, password=h)
            aa.save()
            return render(request, "index.html")


    else:
        return render(request,'agentt.html')


def packagepost(request):
    if request.method=="POST":
        z=request.session.get('aname')
        b=request.POST.get("name")
        i=request.POST.get("area")
        e=request.POST.get("description")
        f=request.FILES.get("photo1")
        g = request.FILES.get("photo2")
        h = request.FILES.get("photo3")
        i = request.FILES.get("photo4")
        pp=Postpackage(aname=z,name=b,area=i,description=e,photo=f,photo2=g,photo3=h,photo4=i)
        pp.save()

        return render(request,"agenthome.html")
    else:
        return render(request,'add_package.html')


def index(request):
    return render(request,"index.html")



def searchpackage(request):
    arec = Postpackage.objects.values('aname').distinct()
    erec = Postpackage.objects.values('name').distinct()
    brec = Postpackage.objects.values('area').distinct()
    crec = Postpackage.objects.values('ptype').distinct()
    if request.method == "POST":
        a = request.POST.get('aname')
        b = request.POST.get('name')
        c = request.POST.get('area')
        d = request.POST.get('ptype')
        result = Postpackage.objects.filter(aname=a, name=b, area=c, ptype=d)
        return render(request, 'searchp.html', {"result": result})
    else:
        return render(request, 'searchp.html',
                      {"arec": arec, "erec": erec, "brec": brec, "crec": crec, })
class Listpackages(ListView):
    template_name ="listofpackages.html"
    model = Postpackage
    context_object_name = "a"

def user_details_update(request):
    if request.method == 'POST':
        aid = request.session['aid']
        up = Agent.objects.get(aid=int(aid))

        aname = request.POST.get('aname')
        phoneno = request.POST.get('phoneno')

        address = request.POST.get('address')
        email = request.POST.get('email')
        photo =request.FILES.get('photo')
        password = request.POST.get('password')

        up.aname = aname
        up.phoneno = phoneno
        up.address = address
        up.email = email
        up.photo = photo
        up.password = password
        up.save()


        context = {'msg': 'User Details Updated','up':up}
        return render(request, 'user_details_update.html',context)

    else:
        aid = request.session['aid']
        up = Agent.objects.get(aid=int(aid))
        context={'up':up}
        return render(request, 'user_details_update.html',context)
def client_details_update(request):
    if request.method == 'POST':
        uid = request.session['uid']
        up = User.objects.get(uid=int(uid))

        uname = request.POST.get('uname')
        phoneno = request.POST.get('phoneno')

        address = request.POST.get('address')
        email = request.POST.get('email')
        photo = request.FILES.get('photo')
        password = request.POST.get('password')

        up.uname = uname
        up.phoneno = phoneno
        up.address = address
        up.email = email
        up.photo = photo
        up.password = password
        up.save()


        context = {'msg': 'Client Details Updated','up':up}
        return render(request, 'client_details_update.html',context)

    else:
        uid = request.session['uid']
        up = User.objects.get(uid=int(uid))
        context={'up':up}
        return render(request, 'client_details_update.html',context)
def deleteclient(request,uid):
    a = User.objects.get(uid=uid)
    a.delete()
    return render(request, "adminhome.html")

def addpackage(request):
    if request.method=="POST":
        a=request.session['aid']
        b=request.session['aname']
        name=request.POST.get('name')
        area=request.POST.get('area')
        description=request.POST.get('description')
        ptype=request.POST.get('ptype')
        photo1=request.FILES.get('photo1')
        photo2 = request.FILES.get('photo2')
        photo3 = request.FILES.get('photo3')
        photo4 = request.FILES.get('photo4')
        sa=Postpackage(aid=a,aname=b,name=name,area=area,description=description,ptype=ptype,photo1=photo1,photo2=photo2,photo3=photo3,photo4=photo4)
        sa.save()
        return render(request,'agenthome.html')
    else:

        return render(request,'package.html')

def listpackage(request):
    a = Postpackage.objects.filter(status='POSTED')
    return render(request, "packagesposted.html",{"a":a})
def packagerequest(request,pid):
    Postpackage.objects.filter(pid=pid).update(status='R')
    return render(request, "clienthome.html")

def viewreq(request,pid):
    a = Postpackage.objects.filter(status='R')
    return render(request, "packagesposted.html", {"a": a})

def request(request,pid,aid):

    bids=request.session['uid']
    if Requestpackage.objects.filter(uid=bids,pid=pid).exists():
        return  HttpResponse("already ")
    else:

        brec=Requestpackage.objects.filter(uid=bids)
        max_rqno=Requestpackage.objects.aggregate(max_rqno=Coalesce(Max('rqno'),Value(0)))['max_rqno']
        rqno=int(max_rqno)+1
        rqdate=date.today()
        if request.method=="POST":
            qp=request.POST.get('t1')
            sa=Requestpackage(rqno=rqno,rqdate=rqdate,uid=bids,pid=pid,status="N",aid=aid)
            sa.save()
            return render(request,"userhome.html")
        else:
            return render(request,"request.html",{"rqno":rqno,"rqdate":rqdate,"pid":pid,"bids":bids})
