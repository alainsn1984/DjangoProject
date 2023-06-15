from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Like
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', { 'posts': posts })

def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        print("Datos del fronted",post_id)
        likepost = Post.objects.get(pk = post_id)
        m = Like(likepost)
        m.save()
        return HttpResponse('Success')
    else:
        return HttpResponse('UnSuccess')

