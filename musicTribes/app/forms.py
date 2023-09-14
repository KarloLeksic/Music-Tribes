from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Playlist, Profile, Song, Tribe, Message, Comment


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profilePicUrl']

class NewTribeForm(forms.ModelForm):
    class Meta:
        model = Tribe
        fields = ['name', 'logoUrl', 'genre']

class NewPlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'description']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']
    
class NewSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['artist', 'name', 'url', 'duration']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

