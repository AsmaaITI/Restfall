from django.shortcuts import render
from app.serializers import BookSerializer,AuthorSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from app.models import Book,Author
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

class JSONResponse(HttpResponse):
	def __init__(self,data,**kwargs):
		json_data = JSONRenderer().render(data)
		kwargs['content_type']='application/json'
		return super(JSONResponse,self).__init__(json_data,**kwargs)



@api_view(['GET','POST'])
def listAuthors(request):
	if request.method == "GET":
		authors = Author.objects.all()
		serializer = AuthorSerializer(authors,many=True)
		return Response(serializer.data)
	elif request.method == "POST":
		serializer = AuthorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)	
		return Response(serializer.errors)	



@api_view(['PUT','DELETE','GET'])
def manipulateAuthor(request,id):
	try:
		author = Author.objects.get(pk=id)
	except Author.DoesNotExist:
		return Response(status.HTTP_404_NOT_FOUND)
	
	if request.method=="GET":
		serializer = AuthorSerializer(author)
		return Response(serializer.data)	
	
	elif request.method=="PUT":
		serializer= AuthorSerializer(author,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
	
	elif request.method=="DELETE":
		author.delete()
		serializer = AuthorSerializer(Author.objects.all(),many=True)		
		return Response(serializer.data)



@api_view(['GET','POST'])
def list(request):
	if request.method=="GET":
		books = Book.objects.all()
		serializer  = BookSerializer(books,many=True)
		# return JSONResponse(serializer.data)
		return Response(serializer.data)

	elif request.method=="POST":
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)

@api_view(['PUT','DELETE','GET'])
def get(request,id):
	try:
		book = Book.objects.get(pk=id)
	except Book.DoesNotExist:
		return Response(status.HTTP_404_NOT_FOUND)
	
	if request.method=="GET":
		serializer = BookSerializer(book)
		return Response(serializer.data)
	elif request.method=="PUT":
		serializer = BookSerializer(book,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
	elif request.method=="DELETE":
		book.delete()
		return Response(status.HTTP_204_NO_CONTENT)