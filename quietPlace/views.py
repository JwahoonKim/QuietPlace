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

def recommendation(request):
    return render(request, 'quietPlace/recommendation.html')

def my_page(request):
    return render(request, 'quietPlace/my_page.html')

def likeCafe(request):
    return render(request, 'quietPlace/likeCafeList.html')

def cafeList(request):
    return render(request, 'quietPlace/cafeList.html')

def cafe_review(request):
    return render(request, 'quietPlace/cafe_review.html')