def make_published(modeladmin, request, queryset):
    row_updated =queryset.update(status='p')

    if row_updated == 1:
            message_bit = "منتشر شد"
    else:
            message_bit = "منتشر شدند"

    modeladmin.message_user(request, f"{row_updated} آیتم {message_bit}")


def make_draft(modeladmin, request, queryset):
    row_updated = queryset.update(status='d')
    if row_updated == 1:
            message_bit = "پیش نویس شد"
    else:
            message_bit = "پیش نویس شدند"

    modeladmin.message_user(request, f"{row_updated} آیتم {message_bit}")

