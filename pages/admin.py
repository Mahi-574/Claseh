from django.contrib import admin
from .models import Page, PageCategory
from home.actions import make_draft, make_published


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_to_str', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status']

    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return ",".join([category.title for category in obj.category.all()])

    category_to_str.short_description = "دسته بندی"


class PageCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ('status',)
    search_fields = ('title',)

    actions = [make_published, make_draft]


admin.site.register(Page, PageAdmin)
admin.site.register(PageCategory, PageCategoryAdmin)

make_published.short_description = "انتشار صفحات انتخاب شده"
make_draft.short_description = "پیش نویس شدن صفحات انتخاب شده"
