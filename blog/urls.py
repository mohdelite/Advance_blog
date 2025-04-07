from django.urls import path
from .views import single_blog_view, list_blog_view, increment_likes
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('post/<int:post_id>/', single_blog_view, name='detail'),
    path('archive/', list_blog_view, name='archive'),
    path('increment_likes/<int:post_id>/', increment_likes, name='increment_likes'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)