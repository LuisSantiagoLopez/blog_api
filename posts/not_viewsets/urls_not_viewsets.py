from django.urls import path
from .views import PostList, PostDetail 

from .views import UserList, UserDetail


urlpatterns = [
 path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
 path("", PostList.as_view(), name="post_list"),
 path("users/", UserList.as_view()),
 path("users/<int:pk>/", UserDetail.as_view())
]