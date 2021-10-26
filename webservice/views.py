from django.shortcuts import render
from django.urls.base import reverse_lazy
from webservice.models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, CommentForm, UserRegisterForm
from django.urls import reverse_lazy
#from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


def index(req):
    return render(req, 'index.html')


#def test_func(user):
#    return user.email.endswith('@mail.ru')

#@user_passes_test(test_func)
#@login_required
#@permission_required('user.view_user', raise_exception=True)
def about(req):
    return render(req, 'about.html')

#class MyView(UserPassesTestMixin, View):
    
 #   def test_func(self):
 #       return self.request.user.email.endswith('@example.com')
class RegisterForm(UserPassesTestMixin,CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')



class PostsView(ListView):
    model = Post
    template_name = "index.html" 
    ordering = ['-created_at']

class DetailPostView(DetailView):
    model = Post
    template_name = "detail_post.html"    

class CreatePostView(PermissionRequiredMixin,CreateView):
    permission_required = 'webservice.add_post'
    model = Post
    template_name = "create_post.html"    
    form_class = PostForm

class UpdatePostView(PermissionRequiredMixin,UpdateView):
    permission_required = 'webservice.change_post'
    model = Post
    template_name = "create_post.html" 
    form_class = PostForm   

class DeletePostView(PermissionRequiredMixin,DeleteView):
    permission_required = 'webservice.delete_post'
    model = Post
    template_name = "delete_post.html"  
    success_url = reverse_lazy('index')

class AddCommentView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = "add_comment.html"  
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

