from rest_framework import serializers
from .models import Book
from author.models import Author

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.name
        return representation
    
class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Book
        fields = ['id', 'name', 'author_name']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.name
        return representation
    
    def create(self, validated_data):
        author_name = validated_data.pop('author_name', None)
        if author_name:
            # Find or create the author based on the name
            author, created = Author.objects.get_or_create(name=author_name)
            validated_data['author'] = author
        return super().create(validated_data)