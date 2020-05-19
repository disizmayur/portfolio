from django.shortcuts import render,get_object_or_404
from .models import blog
# Create your views here.
def allblogs(request):
    blo=blog.objects
    return render(request,'blogs/blogs.html',{'blo':blo})

def details(request, blog_id):
    dblog=get_object_or_404(blog ,pk=blog_id)
    return render(request,'details.html',{'blog':dblog})