# from django.shortcuts import render
# from django.http import HttpResponse
# def index(request):
#     return render(request, 'index.html')

# def userForm(request):
#     name = request.POST.get('InpName', "Неизвестый")
#     date = request.POST.get("UserDate")
#     email = request.POST.getlist("stud")

#     return HttpResponse(f"{name}, {date}, {email}, {student}")

# def djangoForms(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         hours = request.POST.get("hours")
#         return HttpResponse(f"{name}, {hours}")
#     else:
#         usform = Faculter()
#         return render



from django.shortcuts import render

def user_form(request):
    if request.method == 'POST':
        context = {
            'submitted': True,
            'name': request.POST.get('InpName', ''),
            'date': request.POST.get('date', ''),
            'email': request.POST.get('InpEmail', ''),
        }
        return render(request, 'user_form.html', context)
    return render(request, 'user_form.html', {'submitted': False})