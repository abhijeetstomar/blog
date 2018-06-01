from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

# request parameter is required by all views
def post_list(request):
    posts = Post.published.all()
    # render returns html code
    return render(request, 'app/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    # gives html 404 error if object is not found
    post = get_object_or_404(Post, slug = post, 
                                   status = 'published',
                                   publish__year = year,
                                   publish__month = month,
                                   publish__day = day)

    return render(request, 'app/post/detail.html', {'post': post})
