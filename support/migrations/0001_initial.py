# Generated by Django 4.0.4 on 2022-05-04 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='제목')),
                ('phone_number', models.CharField(max_length=10, verbose_name='휴대폰번호')),
                ('get_email', models.EmailField(max_length=128, verbose_name='이메일')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('answer', models.TextField(verbose_name='답변')),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='제목')),
                ('qusetion', models.TextField(verbose_name='질문')),
                ('categroy', models.CharField(choices=[('AC', 'Account'), ('NO', 'Normal'), ('ET', 'Etc')], default='NO', max_length=2, verbose_name='카테고리')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='최종수정일')),
                ('modifier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
