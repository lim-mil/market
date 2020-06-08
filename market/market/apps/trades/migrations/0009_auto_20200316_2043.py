# Generated by Django 2.2 on 2020-03-16 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0008_auto_20200316_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pay',
            field=models.CharField(choices=[(0, '支付宝'), (1, '微信')], default=1, max_length=16, verbose_name='支付方式'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay_no',
            field=models.CharField(blank=True, default='1584362600', max_length=64, null=True, verbose_name='交易号'),
        ),
    ]