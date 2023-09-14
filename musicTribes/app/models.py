from sqlite3 import Timestamp
from django.db import models
from django.db.models import constraints, fields
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class TimeStamped(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()

        self.updated_at = timezone.now()
        return super(TimeStamped, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePicUrl = models.CharField(max_length=512, blank=True) 

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Tribe(TimeStamped):
    chieftain = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    logoUrl = models.CharField(max_length=512, blank=True) 
    genre = models.CharField(max_length=50, blank=False)

    '''
    def userJoinTribe(self, user):
        member = Members.objects.create(tribe=self, user=user)
        member.save()
        return member
    '''

    def __str__(self):
        return self.name

class Members(TimeStamped):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE)
    
class Playlist(TimeStamped):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE)

class Song(TimeStamped):
    name = models.CharField(max_length=200, blank=False)
    artist = models.CharField(max_length=300, blank=False)
    duration = models.CharField(max_length=20, blank=False)
    url = models.CharField(max_length=512)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def num_likes(self):
        return self.like_set.filter(like=True).count()

    def liked_by(self,user):
        if user.is_authenticated:
            return Like.objects.filter(user=user, song=self).first()
        else:
            return None

    def num_comments(self):
        return self.comment_set.filter(song=self).count()

    def get_comments(self):
        return Comment.objects.filter(song=self)

class Comment(TimeStamped):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)

class Message(TimeStamped):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE)

class Like(TimeStamped):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

