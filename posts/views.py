"""Posts views."""

#Django
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
#Utilities
from datetime import datetime

#Model
from posts.models import Post

#FORM
from posts.forms import PostForm
# Create your views here.

class PostFeedView(LoginRequiredMixin, ListView):
    """Returns all published posts."""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 2
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new posts."""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

#class UpdatePostLike(LoginRequiredMixin, UpdateView):
#    """Update Like in post"""

#    template_name = 'posts/feed.html'
#    model = Post
#    fields = ['like']

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        likes_update = get_object_or_404(Post, id=self.kwargs['pk'])

    
#@login_required
#def list_posts(request):
#    """List existing posts."""
#    posts = Post.objects.all().order_by('-created')
#    return render(request, 'posts/feed.html', {'posts': posts})

#@login_required
#def create_post(request):
#    """Create new post view."""
#    if request.method == 'POST':
#        form = PostForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('posts:feed')
#    else:
#        form = PostForm

#    return render(request, 
#                template_name='posts/new.html', 
#                context={
#                        'form': form,
#                        'user': request.user,
#                        'profile': request.user.profile
#                })

#Clase 8
#def list_posts(request):
#    """List existing posts."""
#    content = []
#    for post in posts:
#        content.append(""" 
#            <p><strong>{name}</strong></p>
#            <p><strong>{user} -<i>{timestamp}</i></strong></p>
#            <figure><img src="{picture}"/></figure>
#        """.format(**post))
#    return HttpResponse('<br>'.join(content))

