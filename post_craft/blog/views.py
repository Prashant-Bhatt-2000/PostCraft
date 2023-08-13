from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog

# Create your views here.


@login_required
def logout_view(request):
    if request.method == "POST":
        print('logout')
        request.session.flush()
        response = redirect('/accounts/login')
        response.delete_cookie('sessionid')

        messages.success(request, "You have logged out successfully")
        return response

    return render(request, 'base.html')


@login_required
def AllPosts(request): 
    if request.method == "GET":
        blogs = Blog.objects.all()
        print(f'All {blogs}')

        context = {'blogs': blogs}
        print('context : ', context)
    return render (request, 'articles.html', context)


@login_required
def Write_article(request): 
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        content = request.POST.get('content')

        if not title: 
            messages.error(request, "Please give the Title to your Post")
        elif not content: 
            messages.error(request, "Please write something about your topic.")
        else: 
            current_user = request.user
            blog = Blog(author = current_user, postTitle=title, postDescription=description, postBlog=content)

            blog.save()
            messages.success(request, "Blog saved Successfully")
    
    return render(request, "write.html")



@login_required
def YourPosts(request): 
    if request.method == "GET":
        current_user = request.user
        blogs = Blog.objects.filter(author=current_user)
        print(blogs)

        context = {'blogs': blogs}
        print('context : ', context)
    return render(request, "yourPosts.html", context)