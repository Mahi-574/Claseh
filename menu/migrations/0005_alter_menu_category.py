# Generated by Django 4.2.1 on 2023-06-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_menu_description_alter_menucategory_innerpages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ManyToManyField(related_name='menus', to='menu.menucategory', verbose_name='دسته بندی'),
        ),
    ]
