from django.urls import path
from . import views
from siteblog import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns=[
    path('home.html', views.home, name='home'),
    path('datascience/', views.datascience, name='datascience'),
    path('webdevelopment/', views.webdevelopment, name='webdevelopment'),
    path('blog/', views.PostViewList.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
