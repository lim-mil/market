# Generated by Django 2.2 on 2020-03-19 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0010_auto_20200316_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pay_no',
            field=models.CharField(blank=True, default='1584553521', max_length=64, null=True, verbose_name='交易号'),
        ),
    ]
