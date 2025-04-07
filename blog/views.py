from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from django.utils import timezone 
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .forms import CommentForm
from django.core.paginator import Paginator

def single_blog_view(request, post_id):
    # دریافت پست بر اساس شناسه و بررسی تاریخ انتشار
    post = get_object_or_404(Post, id=post_id, publish_date__lte=timezone.now())
    
    # افزایش تعداد بازدیدهای پست
    post.nview += 1
    post.save()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # ذخیره نظر جدید
            comment = form.save(commit=False)
            comment.post = post 
            comment.save()
            return redirect('blog:detail', post_id=post.id) 
    else:
        form = CommentForm() 

    # فیلتر کردن نظرات تایید شده
    comments = post.comment_set.filter(is_approved=True)    
    return render(request, 'blog/blog_single.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

def list_blog_view(request):
    # دریافت پست‌ها بر اساس تاریخ انتشار
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

    # صفحه‌بندی پست‌ها
    paginator = Paginator(posts, 10) 
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  

    return render(request, 'blog/blog_list.html', {
        'page_obj': page_obj,
        'is_paginated': paginator.num_pages > 1,
        'paginator': paginator,
    })

@require_POST
def increment_likes(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.nlikes += 1
    post.save()
    return JsonResponse({'likes': post.nlikes})
