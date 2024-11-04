from django.contrib import admin

from blogs.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'views', 'published_date')
    list_filter = ('title', 'published_date')

