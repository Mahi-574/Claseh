# Generated by Django 4.2.1 on 2023-06-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='ShortDescription',
            new_name='shortdescription',
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ManyToManyField(default=False, to='menu.menucategory', verbose_name='دسته بندی'),
        ),
    ]