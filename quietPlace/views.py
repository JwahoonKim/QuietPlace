from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from quietPlace.models import Cafe, Review, Cafe_Photo, Like, Tag
from django.contrib.auth.models import User
from accounts.models import Profile
from django.http import JsonResponse
# JsonResponse 추가가 필요한 경우 아래 코드 추가
# from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'quietPlace/index.html')


def show(request, id):
    cafe = Cafe.objects.get(id=id)
    # cafe_photo = Cafe_Photo.objects.get(cafe=cafe)
    reviews_num = cafe.review_set.count()
    return render(request, 'quietPlace/cafe.html', {'cafe': cafe, 'reviews_num': reviews_num})


def recommendation(request):
    return render(request, 'quietPlace/recommendation.html')


def my_page(request):
    if request.user.is_authenticated:
        return render(request, 'quietPlace/my_page.html')
    else:
        return render(request, 'registration/login.html')


def likeCafe(request):
    user = User.objects.get(id=request.user.id)
    like_cafes = user.like_cafes.all()
    return render(request, 'quietPlace/likeCafeList.html', {'like_cafes': like_cafes, 'user': user})


def cafeList(request):
    if request.method == "POST":
        cafes = Cafe.objects.all().filter(
            cafe_name__icontains=request.GET['search_value'])
        return render(request, 'quietPlace/cafeList.html', {"cafes": cafes})
    cafes = Cafe.objects.all()
    cafe_box = [[]]
    region_buttons = [['#서울대입구역', '서울대입구역'], ['#대학동', '대학동']]
    tag_buttons = [ ['#의자가 편해요', 'chair'], ['#테이블이 커요', 'table'], ['#콘센트가 많아요', 'socket'], ['#화장실이 청결해요', 'bathroom'], ['#와이파이 있어요', 'wifi'], ['#조용해요', 'volume'],
                   ['#공간이 넓어요', 'place_size'], ['#다인원 토론공간이 있어요', 'discussion_room'], ['#예약이 가능해요', 'booking_available']]
    return render(request, 'quietPlace/cafeList.html', {"cafes": cafes, "tag_buttons": tag_buttons, 'region_buttons': region_buttons})


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
            cafe_name=cafe_name, cafe_description=cafe_description, working_hour=working_hour, working_detail=working_detail, phone=phone, address=address, category=category, region=region
        )
        for img in request.FILES.getlist('imgs'):
            Cafe_Photo.objects.create( cafe = cafe, cafe_img = img )

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
        return redirect(f'/posts/cafe/{cafe.id}')


class Reviewview:
    def create(request, id):
        content = request.POST['content']
        review = Review.objects.create(
            cafe_id=id, content=content, author=request.user)
        cafe = Cafe.objects.get(id=id)
        return JsonResponse({
            'reviewId': review.id,
            'reviewCount': cafe.review_set.count(),
            'author_nickname': request.user.profile.nickname
        })

    def delete(request, id, cid):
        review = Review.objects.get(id=cid)
        review.delete()
        return redirect(f'/posts/cafe/{id}')


def cafe_like(request, id):
    cafe = Cafe.objects.get(id=id)
    like_list = cafe.like_set.filter(user_id=request.user.id)
    if like_list.count() > 0:
        cafe.like_set.get(user=request.user).delete()
    else:
        Like.objects.create(user=request.user, cafe=cafe)
    return JsonResponse({
        'cafeLikeOfUser': like_list.count(),
        'cafeLikeCount': cafe.like_set.count(),
        # 'userLikeCount' : request.user.like_cafes.count()
    })
