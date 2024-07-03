from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post



def post_list(request):
    posts_list = Post.published.all()
    paginator = Paginator(posts_list, 1)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
    # Если page_number не целое число, то
    # выдать первую страницу
        posts = paginator.page(1)
    except EmptyPage:
    # Если page_number находится вне диапазона, то
    # выдать последнюю страницу результатов
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/blog-list.html', {'posts': posts})


def post_detail(request,post,year,month,day):
    post = get_object_or_404(Post,
                             slug = post,
                             status=Post.Status.PUBLISHED,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )

    return render(request, 'blog/blog-details.html', {'post': post})
