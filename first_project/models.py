from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Users(models.Model):
    useremail = models.EmailField(max_length=30, primary_key=True, verbose_name="이메일(아이디)")
    username = models.CharField(max_length=12,verbose_name="사용자 이름")
    password = models.CharField(max_length=12, verbose_name="비밀 번호")
    registered_dttm = models.DateField(auto_now_add=True, verbose_name="가입 시간")

    def __str__(self):
        return self.username

class Upload(models.Model):
    # type_choices = {('a','말티즈'), ('b','푸들'),('c','시츄')}
    # , choices = type_choices, null = True
    type = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    datetime = models.DateTimeField(null=True)
    gender = models.TextField()
    feature = models.TextField()
    # phone = models.CharField(max_length=15)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    place = models.TextField()
    photo = models.FileField(blank=True)  #, upload_to="photo_%Y_%m_%d")