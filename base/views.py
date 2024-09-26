from django.shortcuts import render, redirect
from .form import *

# Create your views here.
def home(request):
    context = {'blogs': BlogModel.objects.all()}
    return render(request, 'base/home.html', context)

def login(request):
    print(request.user.is_authenticated)
    return render(request, 'base/login.html')

def register(request):
    return render(request, 'base/register.html')

def blog_detail(request, slug):
    context = {}
    try:
        blog = BlogModel.objects.filter(slug = slug).first()
        context['blog'] = blog

    except Exception as e:  
        print(e)

    return render(request, 'base/blog_detail.html', context)

def see_blog(request):
    context ={}
    try:
        blog_obj = BlogModel.objects.filter(user = request.user)
        context['blog_obj'] = blog_obj 

    except Exception as e:
        print(e)

    return render(request, 'base/see_blog.html', context)

def add_blog(request):
    context ={'form': BlogForm} 
    try:
        if request.method == "POST":
            form = BlogForm(request.POST)
            image = request.FILES['image']   
            title = request.POST.get('title')
            user = request.user 
            content = request.POST.get('content')

            if form.is_valid():
                content = form.cleaned_data['content']

            BlogModel.objects.create(
                user = user, title = title,
                content = content, image = image
            )

            return redirect('/add-blog/')

    except Exception as e:
        print(e)

    return render(request, 'base/add_blog.html', context)

def blog_update(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.get(slug= slug)

        if blog_obj.user != request.user:
            return redirect('/')
        
        context['blog_obj'] = 'blog_obj'
        
    except Exception as e:
        print(e)

    return render(request, 'base/update_blog.html', context)


def blog_delete(request, id):

    try:
        blog_obj = BlogModel.objects.get(id = id)

        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e:
        print(e)

    return redirect('/see_blog/')

