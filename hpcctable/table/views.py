from django.shortcuts import render
from .main import table
from django.http import JsonResponse

def adminn(request):
    return render(request, "index.html")

def get_all_data(request):
    result = table().get_data()
    return JsonResponse(result)


