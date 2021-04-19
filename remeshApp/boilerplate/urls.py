from django.urls import path, re_path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.conversations, name='conversations'),
    re_path(r'^conversation/(?P<uuid>.*)/$', views.messages_for_conversation),
    re_path(r'^messages/(?P<uuid>.*)/$', views.thoughts_for_message),
    re_path(r'^conversation_submit/$', views.conversation_post),
    re_path(r'^message_submit/$', views.message_post),
    re_path(r'^thought_submit/$', views.thought_post)
]