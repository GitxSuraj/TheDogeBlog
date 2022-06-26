from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from .models import Blog, Contact

def index(request):
    return render(request, "Blogs/home.html")
def posts(request):
    allBlogs =[]
    blogs= Blog.objects.all()
    allBlogs.append(blogs)
    params={'allBlogs': allBlogs}
    return render(request, "Blogs/blogs.html", params)


def about(request):
    return render(request, "Blogs/about.html")

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
def contact(request):
    if request.method == "POST":
        user_name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc_type = request.POST.get('desc_type', '')
        desc = request.POST.get('desc', '')
        print(user_name, email, desc_type, desc)
        contact = Contact(user_name=user_name, email=email,
                          desc_type=desc_type, desc=desc)
        template = render_to_string('Blogs/email.html', {'name': user_name, 'desc_type':desc_type, 'desc':desc })
        email = EmailMessage(
        'Thanks for conatcting us',
        template,
        settings.EMAIL_HOST_USER,
        [email])
        email.fail_silently=False
        email.send()
        contact.save()
    return render(request, 'Blogs/contact.html')

def blogView(request, blog_id, blog_title):
    blog_view = Blog.objects.filter(blog_id=blog_id, blog_title=blog_title)
    print(blog_view)
    return render(request, "Blogs/blog.html", {'blog_view': blog_view[0]})


# Error Pages
def error_404(request, exception):
    data = {}
    return render(request, 'Blogs/404.html', data)


def error_500(request, *args, **argv):
    data = {}
    return render(request, 'Blogs/500.html', data)
