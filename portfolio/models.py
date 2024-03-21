from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class PortfolioManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class PortfolioCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='child', verbose_name="زیردسته")
    slug = models.SlugField(max_length=100, verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="موقعیت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی نمونه کار"
        verbose_name_plural = "دسته یندی های نمونه کار"
        ordering = ['parent__id', 'position']


class Portfolio(models.Model):
    STATUS_CHOICE = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده')
    )
    title = models.CharField(max_length=200, verbose_name="نام نمونه کار")
    category = models.ManyToManyField(PortfolioCategory, verbose_name="دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته بندی")
    description = RichTextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر شاخص")
    url = models.CharField(max_length=100, verbose_name="آدرس سایت")
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, verbose_name="وضعیت نمایش")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "نمونه کار"
        verbose_name_plural = "نمونه کارها"

    objects = PortfolioManager()
