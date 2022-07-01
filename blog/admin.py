from django.contrib import admin
from .models import Post, Comment, SocialMediaPlatform
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    list_filter = ('status', 'created_on')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    search_fields = ('name', 'email', 'created_on')
    list_filter = ('approved', 'created_on')
    actions = ('approved')

    def approved(self, request, queryset):
        queryset.update(approved=True)


@admin.register(SocialMediaPlatform)
class SocialPlatformAdmin(admin.ModelAdmin):

    list_display = ('name', 'font_awesome_class', 'base_url')
#     search_fields = ('name', 'font_awesome_class', 'base_url')
#     prepopulated_fields = {'base_url': ('name',)}


# @admin.register(SocialMediaPage)
# class SocialPageAdmin(admin.ModelAdmin):

#     list_display = ('Platform', 'handle', 'last_updated')
#     search_fields = ('Platform', 'handle', 'last_updated')
#     list_filter = ('approved', 'created_on')
#     actions = ('approved')

#     def approved(self, request, queryset):
#         queryset.update(approved=True)
