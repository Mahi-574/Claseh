from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class MenuManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class MenuCategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class MenuCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='child', verbose_name="زیردسته")
    slug = models.SlugField(max_length=100, verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="ترتیب نمایش")
    innerpages = models.BooleanField(verbose_name="نمایش در صفحات داخلی")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی منو"
        verbose_name_plural = "دسته بندی های منو"
        ordering = ['parent__id', 'position']

    objects = MenuCategoryManager()


class Menu(models.Model):
    STATUS_CHOICE = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده')
    )
    FOOTER_CHOICE = (
        ('n', 'نمایش داده نشود'),
        ('y', 'نمایش داده شود')
    )
    title = models.CharField(max_length=200, verbose_name="نام منو")
    category = models.ManyToManyField(MenuCategory, related_name="menus",  verbose_name="دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس منو")
    shortdescription = models.TextField(verbose_name="توضیح مختصر")
    description = RichTextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر شاخص")
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, verbose_name="وضعیت نمایش")
    footer = models.CharField(max_length=1, choices=FOOTER_CHOICE, verbose_name="وضعیت نمایش در فوتر")
    position = models.IntegerField(verbose_name="ترتیب نمایش")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "منو"
        verbose_name_plural = "منوها"

    objects = MenuManager()

