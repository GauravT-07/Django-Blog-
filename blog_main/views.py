from django.shortcuts import render
from blogs.models import Category,Blog
from social_media.models import About

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    try:
        about = About.objects.get()
    except:
        about = "Hi, I'm Gaurav!"
    context = {
        'featured_posts' : featured_posts,
        'posts' : posts,
        'about' : about,
    }
    return render(request, 'home.html', context)