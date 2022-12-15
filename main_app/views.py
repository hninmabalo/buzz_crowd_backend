from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = list(Post.objects.all())
    return render(request, 'index.html', { 'posts': posts})

def about(request):
    return render(request, 'about.html')


