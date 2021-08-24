from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BlogPost, Comments
from .forms import BlogCommentForm


# Create your views here.
def blog(request):
    blog_posts = BlogPost.objects.all()

    template = 'blog/blog.html'

    context = {
        'blog_posts': blog_posts,
    }

    return render(request, template, context)


def blog_detail(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    # comments = blog_post.comments.all()
    comments = Comments.objects.all(blogpost=blog_post_id)
    new_comment = None

    if request.method == 'POST':
        comment_form = BlogCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog_post = blog_post
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect(reverse('blog_detail', args=[blog_post.id]))
        else:
            messages.error(request, 'Please check the form for errors. \
                Comment failed to post.')
    else:
        comment_form = BlogCommentForm()

    template = 'blog/blog_detail.html'

    context = {
        'blog_post': blog_post,
        'comments': comments,
        'comment_form': comment_form,
        'new_comment': new_comment,
    }

    return render(request, template, context)
