from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def cookies_sesion(request):
    request.session.set_test_cookie()
    return HttpResponse('<h1>Datos</h1>')

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Sesion<br> Cookie Create")
    else:
        response = HttpResponse("Your browser don't accept cookie")
    return response

def create_sesion(request):
    print("Diccionario Header \n",request.headers)
    print("Objecto Request \n",request)
    print(request.headers)
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>Sesion<br> is set</h1>")

def access_sesion(request):
    response = "<h1>Welcome to Session App</h1>"
    if request.session.get('name'):
        response += "Name: {}<br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password: {}".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')
def delete_sesion(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<h1>Sesion data cleaned</h1>")

