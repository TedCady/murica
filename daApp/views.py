from django.shortcuts import render, HttpResponse, redirect
from .models import User, Branch, Contact
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def AF(request):
    return render(request, 'airForce.html')


def Army(request):
    return render(request, 'army.html')


def Coast(request):
    return render(request, 'coastGuard.html')


def Marines(request):
    return render(request, 'marines.html')


def Navy(request):
    return render(request, 'navy.html')


def info(request):
    return render(request, 'about.html')


def register(request):
    try:
        context={
            'branch': Branch.objects.all(),
            'first_name': getSet(request, 'first_name'),
            'last_name': getSet(request, 'last_name'),
            'email': getSet(request, 'email'),
            'branchId': int(getSet(request, 'branch'))
        }
    except:
        context={
            'branch': Branch.objects.all(),
            }
        print(context)
    return render(request, "register.html", context)


def reg(request):

    print('hello from the beginning')
    print(request.POST)
    try:
        getSet(request, 'first_name')
        getSet(request, 'last_name')
        getSet(request, 'email')
        getSet(request, 'branch')
        print(int(request.POST['branch']))
    except:
        pass
    errorsFromValidator=User.objects.registrationValidator(request.POST)

    print("PRINTING ERRORS FROM VALIDATOR BELOW!")
    print(errorsFromValidator)
    print("*******")
    if len(errorsFromValidator) > 0:
        for key, value in errorsFromValidator.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/register')
    else:
        try:
            newbie=User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=request.POST['password'],
                branch=Branch.objects.get(
                    id=request.POST['branch']
                )
            )
            request.session['yourId']=newbie.id
            request.session['first_name']=''
            request.session['last_name']=''
            request.session['email']=''
            request.session['branch']=''

        except:
            print("Code above failed")
        # newbie = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'], branch=Branch.objects.get(id=request.POST['branch']))
            return redirect('/register')
    return redirect('/welcome')


def login(request):
    return render(request, 'login.html')

def loginVal(request):
    errorsFromValidator=User.objects.loginValidator(request.POST)

    print("PRINTING ERRORS FROM VALIDATOR BELOW!")
    print(errorsFromValidator)
    print("*******")
    if len(errorsFromValidator)>0:
        for key, value in errorsFromValidator.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/login')
    else:
        print("*" *30)
        matchingEmail=User.objects.filter(email=request.POST['email'])
        request.session['loggedInUser']=matchingEmail[0].id

    return redirect('/welcome')
    


def contact(request):
    return render(request, 'contact.html')


def welcome(request):
    if 'loggedInUser' not in request.session:
        return redirect('/')
    context={
        'loggedInUser': User.objects.get(id=request.session['loggedInUser'])
    }

    return render(request, 'hello.html', context)

def contactUS(request):
    Contact.objects.create(
        name=request.POST["name"], 
        email=request.POST["email"], 
        message=request.POST["message"])
    return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')


def getSet(request, name):
    response=''
    try:
        if request.POST[name]:
            response=request.POST[name]
            request.session[name]=response
    except:
        pass
    for key, value in request.session.items():
        if key==name:
            response=value

    return response
