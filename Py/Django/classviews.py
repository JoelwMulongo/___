Class based Views

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

class LandingPageView(TemplateView):
    template_name = 'landing.html'

    # change context data dict
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Landing Page'
        return context

class PostsListView(ListView):
    model = Post 
    # or 
    queryset = Post.objects.all() 

    # var name object_list (or post_list) will be available in template
    # context_object_name = "posts" to change object list var name

    # by default the view will open post/post_list.html but that can be change
    template_name = 'posts/post_list.html'

class PostsDetailView(DetailView):
    model = Post # object var in template

    # by default the view will try to open post/post_detail.html 
    template_name = 'posts/post_detail.html'


class PostsCreateView(CreateView):
    form_class = PostForm
    template_name = 'posts/post_create.html'

    # default return is detail view
    def get_success_url(self):
        return reverse('posts-list')

    # we can overwrite form data
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            from.instance.author = self.request.user

        return super().form_valid(form)

class PostsUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_update.html'
    def get_success_url(self):
        return reverse('post-list')

    # change context data dict
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = 'Update'
        return context


class PostsDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts-list')

# Urls.py route declaration
path('<int:pk>/update/', PostsUpdateView.as_view(), name='post-update')