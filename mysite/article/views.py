from .models import Post, Post2, Post3
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, PostForm2, PostForm3
from django.shortcuts import redirect

# Create your views here.
def com_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'article/com_list.html', {'posts': posts})

def com_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'article/com_detail.html', {'post': post})

def com_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('com_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'article/com_edit.html', {'form': form})


def com_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('com_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'article/com_edit.html', {'form': form})

def article(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'article/article1.html', {'posts': posts})



#Вторая статья
def com_list2(request):
    posts = Post2.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'article/com_list2.html', {'posts': posts})

def com_detail2(request, pk):
    post = get_object_or_404(Post2, pk=pk)
    return render(request, 'article/com_detail2.html', {'post': post})

def com_new2(request):
    if request.method == "POST":
        form = PostForm2(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('com_detail2', pk=post.pk)
    else:
        form = PostForm2()
    return render(request, 'article/com_edit2.html', {'form': form})


def com_edit2(request, pk):
    post = get_object_or_404(Post2, pk=pk)
    if request.method == "POST":
        form = PostForm2(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('com_detail2', pk=post.pk)
    else:
        form = PostForm2(instance=post)
    return render(request, 'article/com_edit2.html', {'form': form})

def article2(request):
    posts = Post2.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'article/article2.html', {'posts': posts})

#Третья статья
def com_list3(request):
    posts = Post3.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'article/com_list3.html', {'posts': posts})

def com_detail3(request, pk):
    post = get_object_or_404(Post3, pk=pk)
    return render(request, 'article/com_detail3.html', {'post': post})

def com_new3(request):
    if request.method == "POST":
        form = PostForm3(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('com_detail3', pk=post.pk)
    else:
        form = PostForm3()
    return render(request, 'article/com_edit3.html', {'form': form})


def com_edit3(request, pk):
    post = get_object_or_404(Post3, pk=pk)
    if request.method == "POST":
        form = PostForm3(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('com_detail3', pk=post.pk)
    else:
        form = PostForm3(instance=post)
    return render(request, 'article/com_edit3.html', {'form': form})

def article3(request):
    posts = Post3.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'article/article3.html', {'posts': posts})