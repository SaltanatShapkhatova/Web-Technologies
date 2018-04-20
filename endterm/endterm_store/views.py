from django.shortcuts import render, redirect
from endterm_store.models import Blog


# Create your views here.
def blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {"blogs": blogs, "active_menu": "blog"})

def blog_details(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blog_details.html', {"blog": blog, "active_menu": "blog"})

def blog_add (request):
    if (request.method == 'POST'):
        title = request.POST['title']
        body = request.POST['body']
        blog = Blog (title=title, body=body)
        blog.save()
        return redirect('/blogs')
    else:
        return render(request, "blog_add.html", {"active_menu": "blog"})

def blog_delete (request, blog_id):
    blog = Blog.objects.get (pk=blog_id)
    blog.delete()
    return redirect('/blogs')

def blog_update (request, blog_id):
    blog = Blog.objects.get (pk=blog_id)
    if (request.method == 'POST'):
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()
        return redirect('/blogs')
    else:
        return render(request, "blog_update.html", {"active_menu": "blog", "blog": blog})


