from django.shortcuts import render
# JsonResponse 추가가 필요한 경우 아래 코드 추가
# from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'quietPlace/index.html')


def header(request):
    return render(request, 'quietPlace/header.html')


def cafe(request):
    return render(request, 'quietPlace/cafe.html')
