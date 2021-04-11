
from django.urls import path
from blog.api.views import PostList, PostDetail

app_name = 'blog_api'

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name='detailcreate'),
    path("", PostList.as_view(), name="listcreate")
]
