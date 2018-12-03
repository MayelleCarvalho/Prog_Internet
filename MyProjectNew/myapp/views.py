import datetime

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from myapp.forms import PostForm
from myapp.models import Post


def list_posts(request):

    posts = Post.objects.order_by('-date_published')
    return render(request, "list_posts.html", {'posts' : posts})


def add_post(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.date_published = datetime.datetime.now()
            model_instance.save()
            return redirect('list_posts')
        else:
            return render(request, "add_post.html", {'form': form})
    else:
        form = PostForm()
        return render(request, "add_post.html", {'form' : form})

def edit_post(request, post_id):
    '''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.date_published = datetime.datetime.now()
            model_instance.save()
            return redirect('list_posts')
        else:
            return render(request, "add_post.html", {'form': form})
    else:
        form = PostForm()
        return render(request, "add_post.html", {'form': form})
'''


    post_a_editar = Post.objects.get(id = post_id)
    form = PostForm(request.POST, instance=post_a_editar)
    if form.is_valid():
        model_instance = form.save(commit=False)
        model_instance.date_published = datetime.datetime.now()
        model_instance.save()
        return redirect('list_posts')
    else:
        return render(request, "edit_post.html",
                  {'form' : form})

def detail_post(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, 'detail_post.html', {'post': post})
