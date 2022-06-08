from django.urls import path
from .views import ViewComment, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, ViewDetilComment, ViewLike

urlpatterns = [
    #_____________new_code____________
    path('like/<int:pk>', ViewLike,name="like_post"),
    path('post/<int:pk>/comments/', ViewDetilComment.as_view(), name='Comment_detail'),
    path('post/<int:pk>/comment/', ViewComment.as_view(), name='Post_Comment'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    #_____________new_code____________
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    
]