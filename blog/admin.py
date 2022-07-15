from django.contrib import admin
from .models import Post,PostImage,PostComment
# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ('title','author','post_date')
    list_filter = ('title','author','post_date')
    search_fields = ('title','author','post_date')
    list_per_page = 5

admin.site.register(Post,AdminPost)
admin.site.register(PostImage)
admin.site.register(PostComment)