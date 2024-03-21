from django.db import models

messages = {
    'required': 'لطفا این فیلد را پر نمایید!',
    'invalid': 'لطفا ایمیل معتیر وارد نمایید!',
    'min_length': 'تعداد کرکتر وارد شده از حداقل مجاز کمتر میباشد!',
    'max_length': 'تعداد کرکتر وارد شده از حداکثر مجاز بیشتر میباشد!',
    'blank': 'لطفا این فیلد را پر نمایید!',
}


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی", error_messages=messages, blank=False)
    email = models.EmailField(verbose_name="ایمیل", error_messages=messages, help_text="لطفا ایمیل متبر با @ وارد نمایید.", blank=False)
    message = models.TextField(verbose_name="پیام", default=None, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس های ما"
