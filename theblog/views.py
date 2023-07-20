from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.
@csrf_exempt
def likePost(request, pk):
    print(request.method)
    if request.method=='POST':
        post= get_object_or_404(Post, id= request.POST['pk'])
        post.likes.add(request.user)
        return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))
    
    return render(request, 'article-detail.html')


class HomeView(ListView):
    model: Post
    template_name= 'home.html'
    
    
    def get_queryset(self):
        """Return Schools """
        return Post.objects.order_by('id')
    
    
class ArticleDetailView(DetailView):
    model: Post
    template_name= 'article_detail.html'
    queryset = Post.objects.all()
    
    
class AddPost(CreateView):
    model: Post
    template_name= 'add_post.html'
    fields= '__all__'
    
    def get_queryset(self):
        """Return Schools """
        return Post.objects.order_by('id')
    
    
    def get_success_url(self):
        return reverse('home')
    
class UpdatePost(UpdateView):
    model: Post
    template_name= 'update_post.html'
    fields= ['title', 'desc']
    
    def get_queryset(self):
        """Return Schools """
        return Post.objects.order_by('id')
    
    def get_success_url(self):
        return reverse('home')


class DeletePost(DeleteView):
    model: Post
    template_name= 'delete_post.html'
    queryset = Post.objects.all()
    
    
    def get_success_url(self):
        return reverse('home')
    
def team(request):
    return render(request, 'team.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # user= get_object_or_404(User, pk= pk)

    if request.method == 'POST':
        msg= request.POST['msg']        
        name= request.user.username
        comment = Comment(post=post,name= name, body=msg)
        comment.save()
            
        return redirect('article-detail', pk=pk)

    return render(request, 'add_comment.html', {'post': post})


def contact(request):
    return render(request, 'contact.html')


    
    