# Generated by Django 4.2.1 on 2023-06-18 16:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_page_status_alter_pagecategory_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات'),
        ),
    ]
