from os import link
from django.contrib import admin

from .models import Profile, Tribe, Members, Playlist, Song, Comment, Message, Like

# Register your models here.
admin.site.register(Profile)
admin.site.register(Tribe)
admin.site.register(Playlist)
admin.site.register(Members)
admin.site.register(Song)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Like)
