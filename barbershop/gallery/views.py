from django.shortcuts import render
from .models import GalleryImage

def gallery_home(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery/home.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        # Handle image upload logic here
        pass
    return render(request, 'gallery/upload.html')

def gallery_category(request, category):
    images = GalleryImage.objects.filter(category=category)
    return render(request, 'gallery/category.html', {'images': images, 'category': category})
