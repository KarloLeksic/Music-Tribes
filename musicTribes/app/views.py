from multiprocessing import context
from webbrowser import get
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.urls import reverse

from app.forms import NewTribeForm, NewPlaylistForm, MessageForm, NewSongForm, CommentForm
from app.models import Tribe, Members, Message, Playlist, Profile, Song, Like, Comment
from django.contrib.auth.models import User





def index(request):
    all_tribes = Tribe.objects.all()
    if request.user.is_authenticated:
        myTribes = Tribe.objects.filter(chieftain=request.user).all()
        joinedTribes = Members.objects.filter(user=request.user).all()

        tribes = [i.tribe for i in joinedTribes]

        allMembers = Members.objects.filter(user=request.user).all()
        allTribes = [t.tribe for t in allMembers]

        otherTribes = [tribe for tribe in  Tribe.objects.all() if tribe not in allTribes and request.user != tribe.chieftain]

        context = {'myTribes' : myTribes,
                   'joinedTribes' : tribes,
                   'otherTribes' : otherTribes,
                    }

        return render(request, 'app/index.html', context)
    else:
        context = { 'all_tribes': all_tribes,  }
        return render(request, 'app/index.html', context)

def tribePage(request, tribe_id):
    tribe = get_object_or_404(Tribe, pk=tribe_id)
    playlists = Playlist.objects.filter(tribe=tribe)
    members = Members.objects.filter(tribe=tribe)
    chieftain = tribe.chieftain
    messages = Message.objects.filter(tribe=tribe)
    form = MessageForm(request.POST)

    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)
        ifMember = Members.objects.filter(user=user, tribe=tribe)

        if ifMember:
            isJoined = True
        else:
            isJoined = False

        context = { 'tribe' : tribe,
                    'playlists': playlists,
                    'members': members, 
                    'chieftain': chieftain,
                    'isJoined': isJoined,
                    'messages': messages,
                    'form': form,
                    }
    else:
        context = {
            'tribe' : tribe,
            'playlists': playlists,
            'messages': messages,
        }
    
    return render(request, 'app/tribe.html', context)

def newTribe(request):
    if request.method == 'POST':
        form = NewTribeForm(request.POST)
        if form.is_valid():
            tribe = form.save(commit=False)
            tribe.chieftain = request.user
            tribe.save()
            return HttpResponseRedirect(reverse('app:index'))
    else:
        form = NewTribeForm()
    context = { 'form':form, 'action':'create' }
    return render(request, 'app/newTribe.html', context)


def joinTribe(request, tribe_id):
    if request.method == 'POST' and request.user.is_authenticated:
        tribe = get_object_or_404(Tribe, pk=tribe_id)
        user = request.user
        member = Members(user=user, tribe=tribe)
        member.save()
        return HttpResponseRedirect(reverse('app:tribePage', args=(tribe_id, )))

def newPlaylist(request, tribe_id):
    tribe = get_object_or_404(Tribe, pk=tribe_id)
    if request.method == 'POST' and request.user == tribe.chieftain:
        form = NewPlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.tribe = tribe
            playlist.save()
            return HttpResponseRedirect(reverse('app:tribePage', args=(tribe_id, )))
    else:
        form = NewPlaylistForm()
    context = { 'form':form, 
                'tribe':tribe, }
    return render(request, 'app/newPlaylist.html', context)

def deletePlaylist(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    if request.method == 'POST' and request.user == playlist.tribe.chieftain:
        playlist.delete()
    return HttpResponseRedirect(reverse('app:tribePage', args=(playlist.tribe.id, )))

def editPlaylist(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    if request.method == 'POST' and request.user == playlist.tribe.chieftain:        
        form = NewPlaylistForm(request.POST, instance=playlist)        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app:tribePage', args=(playlist.tribe.id, )))
    else:
        form = NewPlaylistForm(instance=playlist)
    context = { 'form': form, 
                'playlist': playlist}

    return render(request, 'app/editPlaylist.html', context)

def removeMember(request, tribe_id, member_id):
    tribe = get_object_or_404(Tribe, pk=tribe_id)
    user = get_object_or_404(Members, pk=member_id)
    member = Members.objects.filter(user=user.user, tribe=tribe)
    if request.method == 'POST' and request.user == tribe.chieftain:
        member.delete()
    return HttpResponseRedirect(reverse('app:tribePage', args=(tribe.id, )))

def leaveTribe(request, tribe_id):
    tribe = get_object_or_404(Tribe, pk=tribe_id)
    user = get_object_or_404(User, pk=request.user.id)
    member = Members.objects.filter(user=user, tribe=tribe)
    if request.method == 'POST':
        member.delete()
    return HttpResponseRedirect(reverse('app:tribePage', args=(tribe.id, )))

def sendMessage(request, tribe_id):
    tribe = get_object_or_404(Tribe, pk=tribe_id)
    user = get_object_or_404(User, pk=request.user.id)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST' and request.user.is_authenticated:
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = profile
            message.tribe = tribe
            message.save()
            return HttpResponseRedirect(reverse('app:tribePage', args=(tribe_id, )))
    
def deleteMessage(request, message_id):
    message = Message.objects.get(id=message_id)
    tribe = message.tribe
    if request.method == 'POST' and request.user == tribe.chieftain:
        message.delete()
    return HttpResponseRedirect(reverse('app:tribePage', args=(tribe.id, )))
    
def playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    tribe = get_object_or_404(Tribe, pk=playlist.tribe.id)
    songs = Song.objects.filter(playlist=playlist)
    likes = [song.liked_by(request.user) for song in songs]
    numComments = [song.num_comments() for song in songs]
    comments = [song.get_comments() for song in songs]

    if songs:
        empty = False
    else:
        empty = True

    if request.user.is_authenticated:
        member = Members.objects.filter(user=request.user, tribe=tribe)
    
        commentForm = CommentForm()
        
        if member:
            ifMember = True
        else:
            ifMember = False

        context = {
            'playlist' : playlist,
            'tribe' : tribe,
            'songs_with_likes_and_comments' : zip(songs, likes, numComments, comments),
            'empty' : empty,
            'ifMember' : ifMember,
            'form' : commentForm,
        }
    else:
        context = {
            'playlist' : playlist,
            'tribe' : tribe,
            'songs_with_likes_and_comments' : zip(songs, likes, numComments, comments),
            'empty' : empty,
        }

    return render(request, 'app/playlist.html', context)

def newSong(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    user = get_object_or_404(User, pk=request.user.id)
    tribe = get_object_or_404(Tribe, pk=playlist.tribe.id)
    member = Members.objects.filter(user=user, tribe=tribe)

    if member:
        ifMember = True
    else:
        ifMember = False

    if request.method == 'POST' and ifMember or request.method == 'POST' and request.user == tribe.chieftain:        
        form = NewSongForm(request.POST)        
        if form.is_valid():
            song = form.save(commit=False)
            song.playlist = playlist
            song.user = user
            song.save()
            return HttpResponseRedirect(reverse('app:playlist', args=(playlist_id, )))
    else:
        form = NewSongForm()

    context = { 'form': form, 
                'playlist': playlist,}

    return render(request, 'app/newSong.html', context)

def likeSong(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    user = get_object_or_404(User, pk=request.user.id)
    like = Like.objects.filter(user=user, song=song).first()
    tribe = get_object_or_404(Tribe, pk=song.playlist.tribe.id)
    member = Members.objects.filter(user=user, tribe=tribe)

    if member:
        ifMember = True
    else:
        ifMember = False

    if request.method == 'POST' and ifMember:
        if like:
            if like.like:
                like.like = False
                like.save()
                return HttpResponseRedirect(reverse('app:playlist', args=(song.playlist.id, )))
            else:
                like.like = True
        else:
            like = Like(song=song, user=user, like=True)
        
        try:
            like.full_clean()
            like.save()
        except:
            return None
        else:
            return HttpResponseRedirect(reverse('app:playlist', args=(song.playlist.id, )))

    
def postComment(request, song_id):
    user = get_object_or_404(User, pk=request.user.id)
    profile = Profile.objects.get(user=user)
    song = get_object_or_404(Song, pk=song_id)
    member = Members.objects.filter(user=user, tribe=song.playlist.tribe)

    if member:
        ifMember = True
    else:
        ifMember = False

    if request.method == 'POST' and (ifMember or request.user == song.playlist.tribe.chieftain): 
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = profile
            comment.song = song
            comment.save()
            return HttpResponseRedirect(reverse('app:playlist', args=(song.playlist.id, )))

def deleteSong(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    tribe = song.playlist.tribe
    if request.method == 'POST' and (request.user == tribe.chieftain or request.user.is_superuser or request.user == song.user):
        song.delete()
    return HttpResponseRedirect(reverse('app:playlist', args=(song.playlist.id, )))

def deleteComment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    tribe = comment.song.playlist.tribe
    if request.method == 'POST' and (request.user == tribe.chieftain or request.user.is_superuser):
        comment.delete()
    return HttpResponseRedirect(reverse('app:playlist', args=(comment.song.playlist.id, )))