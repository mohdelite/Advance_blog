from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from blog.models import Category, Post

def index_view(request):
    # دریافت تمام دسته‌بندی‌ها
    categories = Category.objects.all()

    # دریافت آخرین ۳ پست برای هر دسته‌بندی بر اساس تاریخ انتشار
    posts_cultural = Post.objects.filter(publish_date__lte=timezone.now(), category__name='Cultural').order_by('-publish_date')[:3]
    posts_sports = Post.objects.filter(publish_date__lte=timezone.now(), category__name='Sports').order_by('-publish_date')[:3]
    posts_social = Post.objects.filter(publish_date__lte=timezone.now(), category__name='Social').order_by('-publish_date')[:3]
    posts_economic = Post.objects.filter(publish_date__lte=timezone.now(), category__name='Economic').order_by('-publish_date')[:3]
    posts_political = Post.objects.filter(publish_date__lte=timezone.now(), category__name='Political').order_by('-publish_date')[:3]
    posts_scientific = Post.objects.filter(publish_date__lte=timezone.now(), category__name='Scientific').order_by('-publish_date')[:3]
    posts_artistic = Post.objects.filter(publish_date__lte=timezone.now(), category__name='Artistic').order_by('-publish_date')[:3]

    # دریافت ۵ پست با بیشترین بازدید
    most_viewed_posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-nview')[:5]
    # دریافت ۵ پست با بیشترین لایک
    most_liked_posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-nlikes')[:5]

    return render(request, 'index.html', {
        'categories': categories,
        'posts_cultural': posts_cultural,
        'posts_sports': posts_sports,
        'posts_social': posts_social,
        'posts_economic': posts_economic,
        'posts_political': posts_political,
        'posts_scientific': posts_scientific,
        'posts_artistic': posts_artistic,
        'most_viewed_posts': most_viewed_posts,
        'most_liked_posts': most_liked_posts,
    })

def search(request):
    query = request.GET.get('q')  # دریافت عبارت جستجو از URL
    results = []
    
    if query: 
        # جستجوی پست‌ها بر اساس عنوان و محتوا
        results = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    
    return render(request, 'search_results.html', {'results': results})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:view')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')
