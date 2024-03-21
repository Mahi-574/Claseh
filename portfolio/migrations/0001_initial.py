# Generated by Django 4.2.1 on 2023-06-06 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='نام نمونه کار')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('thumbnail', models.ImageField(upload_to='images', verbose_name='تصویر شاخص')),
                ('url', models.CharField(max_length=100, verbose_name='آدرس سایت')),
                ('status', models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده')], max_length=1)),
            ],
        ),
    ]
