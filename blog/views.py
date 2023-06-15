from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView
from .forms import EmailPostForm
from django.shortcuts import redirect
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request,'home.html')

def datascience(request):
    return render(request,'datascience.html')

def contact(request):
    return render(request,'contact.html')
    
def webdevelopment(request):
    return render(request,'webdevelopment.html')

class PostViewList(ListView):
    queryset = Post.published.all()
    paginate_by = 4
    context_object_name = 'posts'
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, publish__year= year, publish__month=month, publish__day=day, slug=post, status = Post.Status.PUBLISHED)
    return render(request,'blog/post/detail.html', {'post':post})

def post_share(request,post_id):
    post = get_object_or_404(Post, id = post_id, status = Post.Status.PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            

    else:
        form = EmailPostForm()
    return render(request,
                      'blog/post/share.html', 
                      {'post':post,
                       'form':form})

