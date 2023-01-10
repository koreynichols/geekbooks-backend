from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json

@api_view(['POST'])
def index(request):
    url = 'https://www.googleapis.com/books/v1/volumes?'
    print(request)
    req_data = request.data
    print(req_data)

    for key in req_data:
        url += key + '='
        url += req_data[key] + '+'

    url = url[:-1]
    url = url.replace(' ', '')

    print(url)

    api_request = requests.get(url)
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error, data not loading"
    
    return Response(api, content_type="application/json")
