from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class PageManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class PageCategory(models.Model):
    STATUS_CHOICE = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده')
    )
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, verbose_name="آدرس دسته بندی")
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, verbose_name="وضعیت نمایش")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی صفحه داخلی"
        verbose_name_plural = "دسته بندی های صفحه داخلی"


class Page(models.Model):
    STATUS_CHOICE = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده')
    )
    title = models.CharField(max_length=200, verbose_name="نام صفحه داخلی")
    category = models.ManyToManyField(PageCategory,  verbose_name="دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس صفحه داخلی")
    description = RichTextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر شاخص")
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, verbose_name="وضعیت نمایش")
    position = models.IntegerField(verbose_name="ترتیب نمایش")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "صفحه داخلی"
        verbose_name_plural = "صفحات داخلی"

    objects = PageManager()