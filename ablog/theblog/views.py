from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
        model = Post
        template_name = 'article_details.html'
        
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):  
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'  
    #fields = ['title', 'FILE_UPLOAD', 'body']

class DeletePostView(DeleteView):  
    model = Post
    template_name = 'delete_post.html'  
    success_url = reverse_lazy('home')

class SearchView(ListView):
    model = Post
    template_name = 'search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.none()
