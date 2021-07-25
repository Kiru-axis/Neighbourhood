from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('all-hoods/', views.hoods, name='hood'),
    path('new-hood/', views.create_hood, name='new-hood'),
    path('single-hood/<id>', views.single_hood, name='single-hood'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


