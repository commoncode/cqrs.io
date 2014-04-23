from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets, routers
from rest_framework import routers
from ecommerce import views


# ViewSets define the view behavior.
"""
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group
"""

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'products', views.ProductViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoadmin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)
