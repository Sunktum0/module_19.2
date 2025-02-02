from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    posts = Post.objects.all()

    # Получаем количество постов на странице из параметра запроса, или по умолчанию 5
    posts_per_page = request.GET.get('posts_per_page', 5)

    paginator = Paginator(posts, posts_per_page)  # Показывать заданное количество постов
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'page_obj': page_obj})