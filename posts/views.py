from django.shortcuts import render, redirect

# Create your views here.
from .models import post
from .forms import PostForm


def all_posts(request):
    all = post.objects.all()
    context = {'objects': all}
    return render(request, 'index.html', context)


def post_content(request, post_slug):
    content = post.objects.get(slug=post_slug)
    context = {'obj': content}
    return render(request, 'post_content.html', context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()
    else:
        form = PostForm()
    context = {"new": form}
    return render(request, 'add_post.html', context)


def edit_post(request, post_slug):
    content = post.objects.get(slug=post_slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()
    else:
        form = PostForm(instance=content)
    context = {"save": form}
    return render(request, 'edit_post.html', context)


def del_post(request, post_slug):
    content = post.objects.get(slug=post_slug)
    content.delete()
    return redirect('/posts')
