from django.db import models
from django.core.validators import RegexValidator
from datetime import date


class User(models.Model):
    uid=models.IntegerField("Id Of User",primary_key=True)
    uname=models.CharField("Name",max_length=25)
    phoneno = models.IntegerField("Phone No")
    state=models.CharField("State",max_length=6,default='Kerala')

    district =models.CharField("District",max_length=20)
    address = models.CharField("Address", max_length=250)
    photo = models.ImageField("Your Photo", upload_to='images/')
    email = models.EmailField("Email")
    password = models.CharField("Password", max_length=25)
    status= models.CharField("User Status",max_length=2,default='U')

class Agent(models.Model):
    aid=models.IntegerField("Agent ID",primary_key=True)
    aname=models.CharField("Name",max_length=25)
    phoneno = models.IntegerField("Phone No")
    state=models.CharField("State",max_length=6,default='Kerala')
    district =models.CharField("District",max_length=20)
    area = models.CharField("Preffred Area", max_length= 30)
    address = models.CharField("Address", max_length=250)
    photo = models.ImageField("Your Photo", upload_to='images/')

    agender = models.CharField("Gender", max_length=1,default='M')
    verification= models.ImageField("Adhar/Election/Driving/PAN ID", upload_to='images/')
    certification= models.ImageField("CTA (Certified Travel Associate) and CTC (Certified Travel Counsellor).", upload_to='images/')
    email = models.EmailField("Email")
    password = models.CharField("Password", max_length=25)
    status= models.CharField("User Status",max_length=2,default='W')
class Postpackage(models.Model):
    pid=models.IntegerField("Pacakage ID",primary_key=True)
    aid=models.ForeignKey(Agent,on_delete=models.CASCADE)
    aname=models.CharField("Name Of Agent",max_length=26)
    name=models.CharField("Name Of Package",max_length=26)
    area=models.CharField("Preffred Area",max_length=25)
    description=models.CharField("Description",max_length=100)
    ptype = models.CharField("Package Type", max_length=25)
    photo1 = models.ImageField("Photo", upload_to='images/')
    photo2 = models.ImageField("Your Photo", upload_to='images/',default='none')
    photo3 = models.ImageField("Your Photo", upload_to='images/')
    photo4 = models.ImageField("Your Photo", upload_to='images/')
    status = models.CharField("status", default='POSTED', max_length=10)
class Requestpackage(models.Model):
    rqno = models.IntegerField("Request No", primary_key=True)
    rqdate = models.DateField("Request Date", default=date.today)
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    aid = models.ForeignKey(Agent,on_delete=models.CASCADE)
    status = models.CharField("status", default='N', max_length=3)






