from django.contrib import admin

# Register your models here.
from .models import Post, Profile, LikePost

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(LikePost)