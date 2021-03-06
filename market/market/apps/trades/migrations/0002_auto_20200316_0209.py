# Generated by Django 2.2 on 2020-03-16 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='estate',
            field=models.CharField(default='', max_length=64, verbose_name='小区'),
        ),
        migrations.AddField(
            model_name='order',
            name='house',
            field=models.CharField(default='', max_length=64, verbose_name='门牌号'),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=16, verbose_name='收货人'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=11, verbose_name='手机号'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='收货人')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('estate', models.CharField(max_length=64, verbose_name='小区')),
                ('house', models.CharField(max_length=64, verbose_name='门牌号')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '收货地址',
                'verbose_name_plural': '收货地址',
                'ordering': ('-created_time',),
            },
        ),
    ]
