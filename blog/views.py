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

# Создание нового поста
def create_post(title, content, published_at=None):
    post = Post.objects.create(title=title, content=content, published_at=published_at)
    return post

# Получение всех постов
def get_all_posts():
    return Post.objects.all()

# Обновление поста
def update_post(post_id, title=None, content=None):
    post = Post.objects.get(id=post_id)
    if title:
        post.title = title
    if content:
        post.content = content
    post.save()

# Удаление поста
def delete_post(post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

# Фильтрация по дате публикации
def filter_posts_by_year(year):
    return Post.objects.filter(published_at__year=year)