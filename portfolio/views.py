from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import *

import smtplib
import email.message
# Create your views here.
def home(req):
    about = About.objects.first()
    skill = Skill.objects.all()
    project = Project.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    service = Service.objects.all()
    portfolio = Portfolio.objects.all()
    contact = Contact.objects.first()
    if req.POST:
        #get POST Data
        name = req.POST['name']
        mail = req.POST['email']
        subject = req.POST['subject']
        message = req.POST['message']
        
        #for Insert into Query table
        obj = Query()
        obj.name = name
        obj.mail = mail
        obj.subject = subject
        obj.message = message
        obj.status = 1
        
        #for sending a mail      
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        mailmessage = f"""
            Dear Shubham Parmar,<br><br>
                &emsp;Subject: {subject}<br><br>
                &emsp;&emsp;{message}<br><br>
        
            Regards,<br>
            {name}<br>
            {mail}
        """     
        msg = email.message.Message()
        msg['Subject'] = "Query | "+ name
        msg['From'] = 'mailsend817@gmail.com'
        msg['To'] = 'shubhamparmar817@gmail.com'
        password = 'Abc@1234'
        msg.add_header('Content-Type','text/html')
        msg.set_payload(mailmessage)
        server.login(msg['From'],password)
        server.sendmail(msg['From'],msg['To'],msg.as_string())
        
        #Inert obj to Query
        obj.save()
        messages.success(req, 'Thank you!! We will  back to you soon.')
        return render(req, 'index.html', {'About': about, 'Skill': skill, 'Project': project, 'Education': education, 
        'Experience': experience, 'Service': service, 'Portfolio': portfolio, 'Contact': contact})
        
    return render(req, 'index.html', {'About': about, 'Skill': skill, 'Project': project, 'Education': education, 
    'Experience': experience, 'Service': service, 'Portfolio': portfolio, 'Contact': contact})