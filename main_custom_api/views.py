from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
from main_custom_api.api import get_inst_data
from main_custom_api.Json_writer import put_user_data


def index(request):
    if request.GET:
        username = request.GET.get('username', '-----')
        data = get_inst_data(username)
        if data is None:
            return JsonResponse({'message': 'unsuccess'})
        json_data = put_user_data(data)
        return JsonResponse(json_data)
    return JsonResponse({'Message': 'Empty'})
