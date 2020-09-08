from rest_framework import serializers  #모델폼비슷
from post.models import Post

    

        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('title',)