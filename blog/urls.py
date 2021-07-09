from django.urls import path
from . import views

path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
