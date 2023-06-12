from django.contrib import admin
from .models import Post, Image
# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image
@admin.register(Post)
class PostSiteAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated','author', 'status']
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ['author']
    inlines = [ImageInline]