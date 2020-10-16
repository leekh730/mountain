from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
    return HttpResponse("Start Project!") # django 제대로 실행 여부 확인용