from django.contrib import admin
from .models import BlogData #, Comment

# Register your models here.

"""
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
"""
class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title']
    #inlines = [CommentInline]
    list_display = ('title', 'source', 'published_date')



admin.site.register(BlogData, BlogAdmin)
#admin.site.register(Comment)