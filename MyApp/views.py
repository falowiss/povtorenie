from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')

def userForm(request):
    name = request.POST.get('InpName', "Неизвестый")
    date = request.POST.get("UserDate")
    email = request.POST.getlist("stud")

    return HttpResponse(f"{name}, {date}, {email}")