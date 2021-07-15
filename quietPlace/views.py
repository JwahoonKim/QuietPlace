from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import quietPlace
from quietPlace.models import Cafe, Review, Cafe_Photo, Like, Tag
from accounts.models import Profile
from django.http import JsonResponse
# JsonResponse 추가가 필요한 경우 아래 코드 추가
# from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'quietPlace/index.html')


def cafe(request):
    return render(request, 'quietPlace/cafe.html')


def show(request, id):
    cafe = Cafe.objects.get(id=id)
    return render(request, 'quietPlace/cafe.html', {'cafe': cafe})


def recommendation(request):
    return render(request, 'quietPlace/recommendation.html')


def my_page(request):
    return render(request, 'quietPlace/my_page.html')


def likeCafe(request):
    return render(request, 'quietPlace/likeCafeList.html')


def cafeList(request):
    if request.method == "GET":
        cafes = Cafe.objects.all().filter(
            cafe_name__icontains=request.GET['search_value'])
        return render(request, 'quietPlace/cafeList.html', {"cafes": cafes})

    cafes = Cafe.objects.all()
    return render(request, 'quietPlace/cafeList.html', {"cafes": cafes})


def cafe_review(request):
    return render(request, 'quietPlace/cafe_review.html')


def new_cafe(request):
    if request.method == 'GET':
        return render(request, 'quietPlace/newcafe.html')
    if request.method == 'POST':
        cafe_name = request.POST['cafe_name']
        cafe_description = request.POST['cafe_description']
        working_hour = request.POST['working_hour']
        working_detail = request.POST['working_detail']
        phone = request.POST['phone']
        address = request.POST['address']
        category = request.POST['category']
        region = request.POST['region']
        cafe = Cafe.objects.create(
            cafe_name=cafe_name, cafe_description=cafe_description, working_hour=working_hour, phone=phone, address=address, category=category, region=region
        )
        for img in request.FILES.getlist('imgs'):
            cafe_photo = Cafe_Photo()
            cafe_photo.cafe = cafe
            cafe_photo.cafe_img = img
            cafe_photo.save()

        chair = request.POST['chair']
        table = request.POST['table']
        socket = request.POST['socket']
        bathroom = request.POST['bathroom']
        wifi = request.POST['wifi']
        volume = request.POST['volume']
        place_size = request.POST['place_size']
        discussion_room = request.POST['discussion_room']
        booking_available = request.POST['booking_available']
        tag = Tag.objects.create(
            cafe=cafe, chair=chair, table=table, socket=socket, bathroom=bathroom, wifi=wifi, volume=volume,
            place_size=place_size, discussion_room=discussion_room, booking_available=booking_available
        )
        return render(request, 'quietPlace/cafe.html', {'cafe': cafe, 'tag': tag})
