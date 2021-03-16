from django.db import models
from datetime import date
import re



class UserManager(models.Manager):
    print('Welcome to the Validator**********************************')
    
    
    def registrationValidator(self, formInfo):
        print('Registration Validator Welcomes You')
        errors={}
        today=date.today()
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        

        usersWithMatchingEmail=User.objects.filter(email=formInfo['email'])
        print(usersWithMatchingEmail)

        if len(formInfo['first_name'])<1:
            print("working********")
            errors['first_name']="Who is this?"
            
        if len(formInfo['last_name'])<1:
            print("working********")
            errors['nameRequired']="Who is this?"
        
        if len(formInfo['email'])<1:
            errors['emailRequired']="Do you even know what email is?"
        
        elif not EMAIL_REGEX.match(formInfo['email']):
            errors['emailInvalid']="Can't Fool me bro, that is not a  real email."
            
        elif len(usersWithMatchingEmail)>0:
            errors['matchingemail']="Please make sure this is your email"
        
        if len(formInfo['password'])<8:
            errors['passwordRequired']="Please enter Password"
        
        if formInfo['confirm']!=formInfo['password']:
            errors['passwordmatch']="Please match Passwords"
        
        if int(formInfo['branch'])<1:
            print("Branch Passed***************************")
            errors['branch']="Please select a Branch!"
        
        return errors
    
    

    def loginValidator(self, formInfo):
        print("*" *30)
        errors = {}
        usersWithMatchingEmail=User.objects.filter(email=formInfo['email'])
        if len(formInfo['email'])<1:
            errors['emailRequired']="Please provide a valid email before logging in"
        elif len(usersWithMatchingEmail)==0:
            errors['emailNotfound']="Are you sure you are registered?"
        else:
            #check password
            print('******* printing the found users password below*********')
            if usersWithMatchingEmail[0].password!=formInfo['password']:
                errors['incorrectpw']="Save your password next time!"
            

        return errors


    

class Branch(models.Model):
    title=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255, null=True)
    branch=models.ForeignKey(Branch, related_name="military", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=255)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    