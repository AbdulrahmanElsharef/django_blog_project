from django.shortcuts import render

# Create your views here.
from .models import post


def all_posts(request):
    all = post.objects.all()
    return render(request, 'index.html', {'objects': all})

def post_content(request,post_id):
    content=post.objects.get(id=post_id)
    return render(request,'post_content.html',{'obj':content})