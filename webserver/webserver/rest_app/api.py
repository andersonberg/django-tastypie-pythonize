from tastypie.resources import ModelResource
from webserver.rest_app.models import Post

class PostResource(ModelResource):
    class Meta:
        resource_name = 'post'
        queryset = Post.objects.all()
