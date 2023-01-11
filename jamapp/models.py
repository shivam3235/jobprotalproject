from django.db import models

# Create your models here.
class JobSeeker(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    email=models.EmailField(max_length=50,primary_key=True)
    dob=models.CharField(max_length=10)
    qualfication=models.CharField(max_length=30)
    exprience=models.CharField(max_length=30)
    keyskills=models.CharField(max_length=20)
    regdate=models.CharField(max_length=20)

class Login(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=50)

class Employer(models.Model):
    firmname=models.CharField(max_length=100)
    firmwork=models.TextField()
    firmaddress=models.TextField()
    cpname=models.CharField(max_length=50)
    cpcontactno=models.CharField(max_length=15)
    cpemailaddress=models.EmailField(max_length=50,primary_key=True)
    aadharno=models.CharField(max_length=12)
    panno=models.CharField(max_length=10)
    gstno=models.CharField(max_length=20)
    regdate=models.CharField(max_length=20)

class Enquiry(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=8)
    address=models.TextField()
    contactno=models.CharField(max_length=10)
    emailaddress=models.EmailField(max_length=30)
    enquirytext=models.TextField()
    posteddate=models.CharField(max_length=20)

class Jobs(models.Model):
    firmname=models.CharField(max_length=100)
    jobtitle=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    jobdesc=models.TextField()
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=50)
    location=models.CharField(max_length=60)
    salarypa=models.IntegerField()
    posteddate=models.CharField(max_length=40)
    emailaddress=models.EmailField(max_length=40)

class AppliedJobs(models.Model):
    empemailaddress=models.EmailField(max_length=30)
    jobtitle=models.CharField(max_length=100)
    post=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50)
    dob=models.CharField(max_length=10)
    qualfication=models.CharField(max_length=100)
    exprience=models.CharField(max_length=30)
    keyskills=models.TextField()
    applieddate=models.CharField(max_length=30)

class News(models.Model):
    newstext=models.TextField()
    newsdate=models.CharField(max_length=30)

