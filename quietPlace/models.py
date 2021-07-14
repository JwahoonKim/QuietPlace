from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Cafe(models.Model):
    cafe_name = models.CharField(max_length=100)
    # 카페에 대한 한 줄 설명
    cafe_description = models.TextField()
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

    def __str__(self):
        return f'[cafe: {self.cafe}], {self.content}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

class Tag(models.Model):
    star = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    review = models.ForeignKey(Review, on_delete=models.CASCADE)