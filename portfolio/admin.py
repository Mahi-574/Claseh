from django.contrib import admin
from .models import Portfolio, PortfolioCategory
from home.actions import make_draft, make_published


# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_to_str', 'status', 'url')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    ordering = ['status']

    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return ",".join([category.title for category in obj.category.all()])

    category_to_str.short_description = "دسته بندی"


class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent', 'status')
    list_filter = ('status',)
    search_fields = ('title',)


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)

make_published.short_description = "انتشار نمونه کار انتخاب شده"
make_draft.short_description = "پیش نویس شدن نمونه کارهای انتخاب شده"

