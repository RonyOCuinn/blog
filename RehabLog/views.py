from django.shortcuts import render, get_object_or_404
from RehabLog.models import Post

#Works yo
def index(request):
    #Get the blog posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered templatee
    return render(request, 'RehabLog/index.html', {'posts':posts})

#Works yo
def post(request, slug):
    #Get the post objects
    post = get_object_or_404(Post, slug=slug)
    #Return rendered templatee
    return render(request, 'RehabLog/post.html', {'post': post})
