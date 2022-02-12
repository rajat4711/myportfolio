from django.db import models
from tinymce import models as tinymce_models
from autoslug import AutoSlugField
class Home(models.Model):
    salutation=models.CharField(max_length=200)
    skills1=models.CharField(max_length=200, blank=True)
    skills2=models.CharField(max_length=200,blank=True)
    skills3=models.CharField(max_length=200, blank=True)
    skills4=models.CharField(max_length=200,blank=True)
    desc=tinymce_models.HTMLField()
    your_image=models.ImageField(upload_to="media")
class about(models.Model):
    display_Name=models.CharField(max_length=50, blank=True)
    email=models.EmailField()
    Date_of_Birth=models.DateField(blank=True)
    Phone=models.CharField(max_length=10)
    website=models.CharField(max_length=50, blank=True)
    First_language=models.CharField(max_length=50, blank=True)
    Second_language=models.CharField(max_length=50, blank=True)
    Degree=models.CharField(max_length=50, blank=True)
    sex=models.CharField(max_length=50)
    Experience=models.IntegerField(blank=True)
    Clients=models.IntegerField(blank=True)
    Awards=models.IntegerField(blank=True)
    Projects=models.IntegerField(blank=True)
    Address=models.CharField(max_length=100)
    Resume=models.FileField(upload_to="media")
class skills(models.Model):
    skill_No=models.IntegerField()
    skills_title=models.CharField(max_length=50)
    konwledge_percentage=models.IntegerField(blank=True)
    icon=models.ImageField(upload_to= "media",default="media/default.jpg")
class education(models.Model):
    course_name=models.CharField(max_length=100)
    course_desc=tinymce_models.HTMLField()
    strt_year1=models.CharField(max_length=4)
    end_year1=models.CharField(max_length=4)
class experience(models.Model):
    exp_title=models.CharField(max_length=500)
    strt_year=models.CharField(max_length=4)
    end_year=models.CharField(max_length=4)
    exp_desc=tinymce_models.HTMLField()
class services(models.Model):
    choic=(("fa fa-mobile-alt","mobile_icon"),("fa fa-bullhorn","icon2"),("fa fa-search","search_icon"),("fa fa-code","code_icon"),("fa fa-palette","icon4"),("fa fa-laptop-code","icon5"))
    category=models.CharField(max_length=50,choices=choic)
    service_title=models.CharField(max_length=100)
    service_desc=models.TextField()
class projects(models.Model):
    project_no=models.IntegerField()
    links=models.CharField(max_length=150)
    Portfolio_picture=models.ImageField(upload_to="media")
    project_desc=models.TextField(blank=True)
class contact(models.Model):
    some_text=models.TextField(blank=True)
    email_id=models.EmailField()
    contact_no=models.CharField(max_length=10)
    website_name=models.CharField(max_length=50,blank=True)
    office=models.CharField(max_length=200)
    facebook=models.CharField(max_length=200,blank=True)
    linkedin=models.CharField(max_length=200,blank=True)
    twitter=models.CharField(max_length=200,blank=True)
    instagram=models.CharField(max_length=200,blank=True)
class Messages(models.Model):
    username=models.CharField(max_length=50)
    user_mail_id=models.EmailField()
    sender_mobile=models.CharField(max_length=10)
    Subject=models.CharField(max_length=200)
    content=models.TextField()
class blog(models.Model):
    title=models.CharField(max_length=100)
    date_added=models.DateField(auto_now_add=True)
    author_name=models.CharField(max_length=100,default="unknown")
    feature_image=models.ImageField(upload_to="media",blank=True)
    desc=tinymce_models.HTMLField()
    slug=AutoSlugField(populate_from='title',unique=True,default=None)
    class meta:
        ordering=['-date_added']

# Create your models here.
