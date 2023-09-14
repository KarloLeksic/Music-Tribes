from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('newTribe/', views.newTribe, name='newTribe'),
    path('<int:tribe_id>/joinTribe', views.joinTribe, name="joinTribe"),
    path('<int:tribe_id>', views.tribePage, name="tribePage"),
    path('<int:tribe_id>/newPlaylist', views.newPlaylist, name="newPlaylist"),
    path('deletePlaylist/<int:playlist_id>', views.deletePlaylist, name="deletePlaylist"),
    path('editPlaylist/<int:playlist_id>', views.editPlaylist, name="editPlaylist"),
    path('<int:tribe_id>/removeMember/<int:member_id>', views.removeMember, name="removeMember"),
    path('<int:tribe_id>/leaveTribe', views.leaveTribe, name="leaveTribe"),
    path('<int:tribe_id>/sendMessage', views.sendMessage, name="sendMessage"),
    path('deleteMessage/<int:message_id>', views.deleteMessage, name="deleteMessage"),
    path('playlist/<int:playlist_id>', views.playlist, name="playlist"),
    path('<int:playlist_id>/newSong', views.newSong, name="newSong"),
    path('<int:song_id>/likeSong', views.likeSong, name="likeSong"),
    path('<int:song_id>/postComment', views.postComment, name="postComment"),
    path('<int:song_id>/deleteSong', views.deleteSong, name="deleteSong"),
    path('<int:comment_id>/deleteComment', views.deleteComment, name="deleteComment"),
]
