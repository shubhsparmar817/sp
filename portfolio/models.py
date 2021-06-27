from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(default="",blank=True,null=True,max_length=50)
    field = models.CharField(default="",blank=True,null=True,max_length=50)
    fieldDesc =  models.TextField(default="")
    profile = models.ImageField(upload_to="Profile/",default="",blank=True, null=True,max_length=300)
    birthdate = models.CharField(default="",blank=True,null=True,max_length=20)
    age = models.IntegerField(default="",blank=True,null=True)
    phone = models.CharField(default="",blank=True,null=True,max_length=20)
    degree = models.CharField(default="",blank=True,null=True,max_length=20)
    city = models.CharField(default="",blank=True,null=True,max_length=50)
    mail = models.EmailField(default="",blank=True,null=True,max_length=100)
    about = models.TextField(default="")
    
class Skill(models.Model):
    name = models.CharField(default="",blank=True,null=True,max_length=100)
    percentage = models.IntegerField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name +' ['+ str(self.percentage) +'%]'
    
class Project(models.Model):
    name = models.CharField(default="",blank=True,null=True,max_length=100)
    desc= models.TextField(default="")
    
    def __str__(self):
        return self.name
    
class Education(models.Model):
    name = models.CharField(default="",blank=True,null=True,max_length=200)
    start = models.IntegerField(default="",blank=True,null=True)
    end = models.IntegerField(default="",blank=True,null=True)
    college = models.CharField(default="",blank=True,null=True,max_length=200)
    university = models.CharField(default="",blank=True,null=True,max_length=100)
    location = models.CharField(default="",blank=True,null=True,max_length=50)
    percentage = models.CharField(default="",blank=True,null=True,max_length=20)
    percentageType = models.CharField(default="",blank=True,null=True,max_length=10)
    
    def __str__(self):
        return self.name
    
class Experience(models.Model):
    title = models.CharField(default="",blank=True,null=True,max_length=200)
    employmentType = models.CharField(default="",blank=True,null=True,max_length=100)
    start = models.CharField(default="",blank=True,null=True,max_length=50)
    end = models.CharField(default="",blank=True,null=True,max_length=50)
    company = models.CharField(default="",blank=True,null=True,max_length=200)
    location = models.CharField(default="",blank=True,null=True,max_length=50)
    website = models.CharField(default="",blank=True,null=True,max_length=200)
    websiteUrl = models.CharField(default="",blank=True,null=True,max_length=200)
    desc1 = models.TextField(default="")
    desc2 = models.TextField(default="",blank=True)
    desc3 = models.TextField(default="",blank=True)
    desc4 = models.TextField(default="",blank=True)
    desc5 = models.TextField(default="",blank=True)
    
    def __str__(self):
        return self.company
    
class Service(models.Model):
    name = models.CharField(default="",blank=True,null=True,max_length=200)
    icon = models.CharField(default="",blank=True,null=True,max_length=20)
    desc = models.TextField(default="")
    
    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    name = models.CharField(default="",blank=True,null=True,max_length=200)
    image = models.ImageField(upload_to="Portfilio/",default="",blank=True, null=True,max_length=300)
    url = models.CharField(default="",blank=True,null=True,max_length=200)
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    addressLine1 = models.CharField(default="",blank=True,null=True,max_length=200)
    addressLine2 = models.CharField(default="",blank=True,null=True,max_length=200)
    city = models.CharField(default="",blank=True,null=True,max_length=50)
    district = models.CharField(default="",blank=True,null=True,max_length=50)
    state = models.CharField(default="",blank=True,null=True,max_length=50)
    country = models.CharField(default="",blank=True,null=True,max_length=50)
    pincode = models.IntegerField(default="",blank=True,null=True)
    linkedin = models.CharField(default="",blank=True,null=True,max_length=200)
    skype = models.CharField(default="",blank=True,null=True,max_length=200)
    twitter = models.CharField(default="",blank=True,null=True,max_length=200)
    
class Query(models.Model):
    name = models.CharField(default="",blank=True,null=True,max_length=200)
    mail = models.EmailField(default="",blank=True,null=True,max_length=100)
    subject = models.CharField(default="",blank=True,null=True,max_length=200)
    message = models.TextField(default="",blank=True)
    status = models.IntegerField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name