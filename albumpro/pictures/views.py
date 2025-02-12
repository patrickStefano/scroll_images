from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categories, Photo


def venu(request):
  return HttpResponse("I am Testing my git branch! so i hope it is going to work out!")


#la section des categories ici********************
def galery(request):
     categori = request.GET.get('categori')
     if  categori == None:
           photos = Photo.objects.all()
     else:
           photos = Photo.objects.filter(categories__name=categori)


     categories = Categories.objects.all()

     context = {'categories':categories,'photos':photos}
    
     return render(request, 'pictures/galery.html', context)

#la section deds ajouts des images ici****************
def ajouter(request):
   categories = Categories.objects.all()

   if request.method == 'POST':
      data = request.POST
      image = request.FILES.get('image')
      
      if data['categories'] != 'none':
         categories = Categories.objects.get(id=data['categories'])
      elif data['creer'] != '':
         categories, created = Categories.objects.get_or_create(name=data['creer'])
      else:
         categories = None

      photos = Photo.objects.create(
         categories = categories,
         desciption= data['desciption'],
         image=image,
      )

      return redirect('galery')
  


   context = {'categories':categories}
   return render(request, 'pictures/ajouter.html', context)

#la section des photos ici******************************
def photo(request, pk):
   photos = Photo.objects.get(id=pk)  # we use 'get' in case we wanna get y url
   context = {'photos':photos}
   return render(request, 'pictures/photo.html', context)