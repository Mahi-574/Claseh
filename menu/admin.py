from django.contrib import admin
from .models import Menu, MenuCategory
from home.actions import make_draft, make_published


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_to_str', 'status', 'position')
    list_filter = ('status',)
    search_fields = ('title', 'description', 'shortdescription')
    ordering = ['status']

    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return ",".join([category.title for category in obj.category.all()])

    category_to_str.short_description = "دسته بندی منو"


class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent', 'status')
    list_filter = ('status',)
    search_fields = ('title',)

    actions = [make_published, make_draft]


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuCategory, MenuCategoryAdmin)

make_published.short_description = "انتشار منوهای انتخاب شده"
make_draft.short_description = "پیش نویس شدن منوهای انتخاب شده"
