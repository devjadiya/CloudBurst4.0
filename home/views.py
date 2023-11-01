from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,"index.html")
# def acadmics(request):
#     return render(request,"acadmics.html")
# def code(request):
#     return render(request,"code.html")
# def clubs(request):
#     return render(request,"clubs.html")
# def happenings(request):
#     return render(request,"happenings.html")
# def projects(request):
#     return render(request,"projects.html")
# def contribution(request):
#     return render(request,"contribution.html")
# def developers(request):
#     return render(request,"developers.html")
