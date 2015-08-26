from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

# Create your views here.
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib import messages


def post_list(request):        
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # messages.add_message(request, messages.INFO, 'Hello world.')
    # messages.info(request, 'Three credits remain in your account.')
    # posts = Post.objects.all()
    # return render(request,'blog/post_list.html', {'posts':posts})   
    return HttpResponse(request.META)

def post_detail(request,pk): 	
	#post = get_object_or_404(Post, pk=pk)
    #return HttpResponse(pk)
    posts = Post.objects.get(id=pk)
    return render(request,'blog/post_detail.html', {'post':posts})   

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
        else:
            return render(request, 'blog/post_edit.html', {'form': form})
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    #post = Post.objects.get(id=pk)
    post = get_object_or_404(Post, pk=pk)

    
    # if request.is_ajax():
    #     import pdb; pdb.set_trace()
    #     post.title = request.POST['title']
    #     post.text = request.POST['text']
    #     post.save()
    #     return redirect('blog.views.post_detail', pk = post.pk)
    
    if request.method == "POST":
        #import pdb; pdb.set_trace()
        form = PostForm(request.POST, request.FILES, instance=post)        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk = post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

 