from django.shortcuts import render


# Create your views here.
def blog_home(request):
    context = {'chapter': 'blog'}
    return render(request, 'blog/blog.html', context)
