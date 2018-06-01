from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# request parameter is required by all views
def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    # indicates current page number
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.page(1)

    except EmptyPage:
        # if page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    # render returns html code
    return render(request, 'app/post/list.html', {'page': page,
                                                  'posts': posts})


def post_detail(request, year, month, day, post):
    # gives html 404 error if object is not found
    post = get_object_or_404(Post, slug = post, 
                                   status = 'published',
                                   publish__year = year,
                                   publish__month = month,
                                   publish__day = day)

    return render(request, 'app/post/detail.html', {'post': post})
