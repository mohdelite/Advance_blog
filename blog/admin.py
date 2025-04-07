from django.contrib import admin
from .models import Category, Post, Comment
from django.utils import timezone
import jdatetime

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # نمایش نام دسته‌بندی
    search_fields = ('name',)  # قابلیت جستجو بر اساس نام دسته‌بندی

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'nview', 'nlikes', 'get_created_at', 'get_publish_date', 'is_draft')  # نمایش اطلاعات پست
    list_filter = ('category', 'author', 'created_at', 'publish_date')  # فیلتر بر اساس دسته‌بندی، نویسنده، تاریخ ایجاد و تاریخ انتشار
    search_fields = ('title', 'content', 'author__username')  # قابلیت جستجو بر اساس عنوان، محتوا و نام کاربری نویسنده
    ordering = ('-publish_date',)  # مرتب‌سازی بر اساس تاریخ انتشار به صورت نزولی

    def get_publish_date(self, obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.publish_date).strftime('%Y/%m/%d')  # تبدیل تاریخ به شمسی
    get_publish_date.short_description = 'تاریخ انتشار'

    def get_created_at(self, obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.created_at).strftime('%Y/%m/%d')  # تبدیل تاریخ به شمسی
    get_created_at.short_description = 'تاریخ ایجاد'

    def is_draft(self, obj):
        return obj.publish_date > timezone.now()  # بررسی اینکه آیا پست در حالت پیش‌نویس است
    is_draft.boolean = True  # نمایش به صورت آیکون بولی
    is_draft.short_description = 'Draft'  # عنوان ستون

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'content', 'get_created_at', 'is_approved')  # نمایش اطلاعات نظر
    list_editable = ('is_approved',)  # قابلیت ویرایش وضعیت تایید نظر
    list_filter = ('post', 'is_approved')  # فیلتر بر اساس پست و وضعیت تایید
    search_fields = ('name', 'content')  # قابلیت جستجو بر اساس نام و محتوا

    def get_created_at(self, obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.created_at).strftime('%Y/%m/%d')  # تبدیل تاریخ به شمسی
    get_created_at.short_description = 'تاریخ ایجاد'

# ثبت مدل‌ها در پنل مدیریت
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
