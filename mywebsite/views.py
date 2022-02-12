from django.http import HttpResponse
from django.shortcuts import render
from home.models import about
from home.models import Home
from home.models import skills
from home.models import education
from home.models import experience
from home.models import services
from home.models import projects
from home.models import contact
from home.models import Messages
from django.core.mail import send_mail
from home.models import blog
def index(request):
    about_data=about.objects.all()
    my_data=Home.objects.all()
    skills_data=skills.objects.all()
    education_data=education.objects.all()
    experience_data=experience.objects.all()
    services_data=services.objects.all()
    projects_data=projects.objects.all()[:6]
    contact_data=contact.objects.all()
    form_data=Messages.objects.all()
    blog_data=blog.objects.all()
    ''' form'''
    try:
        if request.method=="POST":
            mail_id=request.POST.get("mails")
            Name1=request.POST.get("Name1")
            subject=request.POST.get("subject")
            msg=request.POST.get("text2")
            mob=request.POST.get("sender_mobile")
            formdata=Messages(username=Name1,user_mail_id=mail_id,Subject=subject,content=msg,sender_mobile=mob)
            formdata.save()
            send_mail(subject,msg,'jsrdevops@gmail.com',['rajatprasad562@gmail.com'],fail_silently=True)
    except:
        pass
    context={'intro':about_data,'Name':my_data,'skill':skills_data,'education':education_data,'experience':experience_data,'service':services_data,'project':projects_data,'contacts':contact_data,'blogs':blog_data}
    return render(request,"index.html",context)
    
def mywork(request):
    projects_data=projects.objects.all()
    context2={'mywork':projects_data}
    return render(request,"portfolio.html",context2)
def myblog(request,slug):
    blugs=blog.objects.get(slug=slug)
    return render(request,"blog_details.html",{'bl':blugs})