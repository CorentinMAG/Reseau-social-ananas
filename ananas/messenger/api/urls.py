from django.urls import path, re_path

from .views import (
    ChatListView,
    ChatDetailView,
    ChatCreateView,
    ChatUpdateView,
    ChatDeleteView,
    ChatPublic,
    AllUser,
delete_tag
)

app_name = 'chat'

urlpatterns = [
    path('', ChatListView.as_view()),
    path('public/', ChatPublic.as_view()),
    path('create/', ChatCreateView.as_view()),
    path('<pk>', ChatDetailView.as_view()),
    path('<pk>/update/', ChatUpdateView.as_view()),
    path('<pk>/delete/', ChatDeleteView.as_view()),
    path('users/', AllUser.as_view()),
    path('delete_tag/',delete_tag)
]
