from django.shortcuts import render
from .main import table
from django.http import JsonResponse

def adminn(request):
    return render(request, "index.html")

def get_all_data(request):
    #СОРТИРОВКА ПО ИМЕНИ
    # result = table().get_data()

    # # Сортировка данных по ключу "name"
    # sorted_data = sorted(result, key=lambda x: x["name"])

    # return JsonResponse(sorted_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})

    #Выбор группы прописан в маин пай, хз как это во вьющке сделать


    #сортировка по годам
    # result = table().get_data()

    # # Сортировка данных по ключу "years"
    # sorted_data = sorted(result, key=lambda x: x["years"])

    # return JsonResponse(sorted_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})