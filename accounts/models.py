from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, verbose_name="사용자 닉네임", default="닉네임을 설정해주세요")
    email = models.EmailField(max_length=254, verbose_name="사용자 이메일", null=True, blank=True)
    profile_pic = models.ImageField(upload_to='images/', verbose_name="사용자 프로필사진", blank=True, null=True)
    # 아래는 뭘까 ???
    is_login = False

    def __str__(self):
        return f'id={self.id}, user_id={self.user.id}, nickname={self.nickname}, profile_pic={self.profile_pic}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()