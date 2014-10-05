from django.conf.urls import patterns, include, url
from django.contrib import admin
from webserver.rest_app.api import PostResource, UserResource

user_resource = UserResource()
post_resource = PostResource()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(post_resource.urls)),
    url(r'^api/', include(user_resource.urls)),
)
