from PythonGirls.blog.models import Categoria, Autor, Tag, Banner, Post
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.


def index(request):
    return render_to_response('index.html', {
        'categorias': Categoria.objects.all(),
        'posts': Post.objects.all()[:5]
    })


def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })


def view_category(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    return render_to_response('view_category.html', {
        'categoria': categoria,
        'posts': Post.objects.filter(categoria=categoria)[:5]
    })


