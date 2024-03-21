# Generated by Django 4.2.1 on 2023-07-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_alter_contact_email_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, error_messages={'blank': 'لطفا این فیلد را پر نمایید!', 'invalid': 'لطفا ایمیل معتیر وارد نمایید!', 'max_length': 'تعداد کرکتر وارد شده از حداکثر مجاز بیشتر میباشد!', 'min_length': 'تعداد کرکتر وارد شده از حداقل مجاز کمتر میباشد!', 'required': 'لطفا این فیلد را پر نمایید!'}, max_length=100, null=True, verbose_name='نام و نام خانوادگی'),
        ),
    ]