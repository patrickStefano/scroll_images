from django.shortcuts import render
from django.http import HttpResponse
from .models import Categories, Photo


def venu(request):
  return HttpResponse("I am Testing my git branch! so i hope it is going to work out!")

def galery(request):
     categories = Categories.objects.all()
     photos = Photo.objects.all()
     context = {'categories':categories,'photos':photos}
    
     return render(request, 'pictures/galery.html', context)

def ajouter(request):
   return render(request, 'pictures/ajouter.html')

def photo(request, pk):
   photos = Photo.objects.get(id=pk)  # we use 'get' in case we wanna get y url
   context = {'photos':photos}
   return render(request, 'pictures/photo.html', context)