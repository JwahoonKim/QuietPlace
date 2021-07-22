from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import Profile


class Cafe(models.Model):
    cafe_name = models.CharField(max_length=100)
    # 카페에 대한 한 줄 설명
    cafe_description = models.TextField(blank=True, null=True)
    working_hour = models.CharField(max_length=100, blank=True, null=True)
    working_detail = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    like_users = models.ManyToManyField(
        User, blank=True, related_name='like_cafes', through='Like')

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.cafe_name


class Review(models.Model):
    # 이미지 필드 추가
    content = models.TextField()
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # like_users는 넣어야할 필드인지 잘 모르겟네?
    # like_users = models.ManyToManyField(
    #     User, blank=True, related_name='like_comments')
    star = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    def __str__(self):
        return f'[cafe: {self.cafe}], {self.content}'


class Cafe_Photo(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, null=True)
    cafe_img = models.ImageField(
        upload_to='images/cafe_pic', blank=True, null=True)


class Review_Photo(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    review_img = models.ImageField(
        upload_to='images/review_pic', blank=True, null=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class Tag(models.Model):
    cafe = models.OneToOneField(Cafe, on_delete=models.CASCADE)
    chair = models.TextField(blank=True, null=True)
    table = models.TextField(blank=True, null=True)
    socket = models.TextField(blank=True, null=True)
    bathroom = models.TextField(blank=True, null=True)
    wifi = models.TextField(blank=True, null=True)
    volume = models.TextField(blank=True, null=True)
    place_size = models.TextField(blank=True, null=True)
    discussion_room = models.TextField(blank=True, null=True)
    booking_available = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'[cafe: {self.cafe}], {self.content}'
