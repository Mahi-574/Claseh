# Generated by Django 4.2.1 on 2023-07-01 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contact_comment_remove_contact_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(help_text='لطفا ایمیل خود را وارد نمایید!', max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default=None, help_text='لطفا پیام خود را وارد نمایید!', verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(help_text='لطفا نام خود را وارد نمایید!', max_length=100, verbose_name='نام و نام خانوادگی'),
        ),
    ]
