from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import serializers
from app.gallery.models import Gallery

class UserRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        )

class GallerySerializer(serializers.ModelSerializer):
    user = UserRelatedSerializer(many=False, read_only=True)
    content_type = serializers.CharField(read_only=True)
    class Meta:
        model = Gallery
        fields = '__all__'
    
    def save(self, **kwargs):
        self.validated_data['user'] = self.context['request'].user
        return super().save(**kwargs)

# Create your views here.
class GalleryListView(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    def get_queryset(self):
        qs = self.queryset
        return qs.filter(user=self.request.user)

class GalleryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer