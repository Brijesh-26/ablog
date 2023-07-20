
from django.urls import path, include
from .views import HomeView , ArticleDetailView, AddPost , UpdatePost, DeletePost
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name= 'article-detail'),
    path('add_post/', AddPost.as_view(), name= 'add_post'),
    path('article/update/<int:pk>', UpdatePost.as_view(), name = 'update_post'),
    path('article/<int:pk>/delete', DeletePost.as_view(), name= 'delete_post'),
    path('teams/', views.team, name= 'teams'),
    path('like/<int:pk>/', views.likePost, name= "likepost"),
    path('article/<int:pk>/comment/', views.post_detail, name='add_comment'),
    path('contact/', views.contact)
    # path('article/<int:pk>/comment/', AddComment.as_view(), name= 'add_comment'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
