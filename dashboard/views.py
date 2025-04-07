from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Category, Comment
from django.utils import timezone 
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from blog.forms import CommentForm, PostForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse


@login_required
def dashboard_view(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    draft_posts = posts.filter(publish_date__gt=timezone.now()) 
    comments = Comment.objects.all() 
    return render(request, 'dashboard/dashboard.html', {
        'posts': posts,
        'categories': categories,
        'draft_posts': draft_posts,
        'comments': comments,
    })


@login_required  
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'پست با موفقیت ایجاد شد!')
            return redirect(reverse('dashboard:view'))
        else:
            messages.error(request, 'لطفاً خطاهای زیر را اصلاح کنید.')

    else:
        form = PostForm()

    return render(request, 'dashboard/add_post.html', {'form': form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard:view')
    else:
        form = PostForm(instance=post)
    return render(request, 'dashboard/edit_post.html', {'form': form, 'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('dashboard:view')
    return render(request, 'dashboard/delete_post.html', {'post': post})

def manage_categories(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/manage_categories.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('dashboard:view')
    else:
        form = CategoryForm()

    return render(request, 'dashboard/add_category.html', {'form': form})

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dashboard:manage_categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'dashboard/edit_category.html', {'form': form})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('dashboard:manage_categories')
    return render(request, 'dashboard/delete_category.html', {'category': category})

def approve_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.is_approved = True
    comment.save()
    return redirect('dashboard:view')

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('dashboard:view')
