from rest_framework import serializers
from app.models import Book,Author


class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields= ('name',)

class BookSerializer(serializers.ModelSerializer):
	#author_name = AuthorSerializer(source='author',read_only=`True`)
	author_name = AuthorSerializer(source='author',read_only=`True`)
	class Meta:
		model = Book
		fields= ('title','author_name','description')



