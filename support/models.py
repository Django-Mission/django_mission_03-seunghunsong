from multiprocessing.connection import answer_challenge
from turtle import update
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Faq(models.Model):
    class Category(models.TextChoices):
        account = 'AC', ('Account')
        normal = 'NO', ('Normal')
        etc = 'ET', ('Etc')
    title = models.CharField(
        verbose_name='제목',
        max_length=10,
    )
    qusetion = models.TextField(verbose_name='질문')
    categroy = models.CharField(
        verbose_name='카테고리',
        max_length=2,
        choices=Category.choices,
        default=Category.normal,
    )    
    modifier = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True,related_name='+')
    update_at = models.DateTimeField(verbose_name='최종수정일', auto_now=True)

class Inquiry(models.Model):
    class Category(models.TextChoices):
        account = 'AO', ('Account')
        normal = 'NR', ('Normal')
        etc = 'EC', ('Etc')
    title = models.CharField(verbose_name='제목', max_length=10,)
    categroy = models.CharField(verbose_name='카테고리', max_length=2, choices=Category.choices, default=Category.normal,)
    phone_number = models.CharField(verbose_name='휴대폰번호', max_length=11,)
    get_email = models.EmailField(max_length=128, verbose_name='이메일')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    

class Answer(models.Model):
    answer = models.TextField(verbose_name='답변')
    inpuiry= models.ForeignKey(to='inquiry',on_delete=models.CASCADE)