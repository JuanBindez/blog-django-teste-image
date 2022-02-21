from django.shortcuts import render
from .models import Post

# Create your views here.
def hello_home(request):
    list_posts = Post.objects.all()
    data = {'posts': list_posts }
    return render(request, 'index.html', data)

def hello_calc(request):
    return render(request, 'calc.html')