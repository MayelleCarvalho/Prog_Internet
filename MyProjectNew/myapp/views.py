from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from myapp.forms import PostForm
from myapp.models import Post


def list_posts(request):

    posts = Post.objects.all()
    return render(request, "list_posts.html", {'posts' : posts})


def add_post(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        #age = form['age']
        #age_int = form.cleaned_data['age']
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_posts')
    else:
        form = PostForm()
        return render(request, "add_post.html", {'form' : form})