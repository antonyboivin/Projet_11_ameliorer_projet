from django.db.models import Count
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import NewTopicForm, PostForm
from .models import Heading, Topic, Post

def forum(request):
    headings = Heading.objects.all()
    return render(request, 'forum/forum_home_page.html', {'headings': headings})

def forum_topics(request, pk):
    heading = get_object_or_404(Heading, pk=pk)
    topics = heading.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
    return render(request, 'forum/forum_topics.html', {'heading': heading, 'topics': topics})


def new_topic(request, pk):
    if request.user.is_authenticated:
        heading = get_object_or_404(Heading, pk=pk)
        usertopic = request.user.username

        if request.method == 'POST':
            form = NewTopicForm(request.POST)

            if form.is_valid():
                topic = form.save(commit=False)
                topic.heading = heading
                topic.starter = usertopic
                topic.save()
                post = Post.objects.create(
                    message=form.cleaned_data.get('message'),
                    topic=topic,
                    created_by=usertopic
                )

                return redirect('forum topics', pk=heading.pk)
        else:
            form = NewTopicForm()

        return render(request, 'forum/new_topic.html', {'heading': heading,'form': form})
    else:
        headings = Heading.objects.all()
        return render(request, 'forum/forum_home_page.html', {'headings': headings})

def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, heading__pk=pk, pk=topic_pk)
    heading = get_object_or_404(Heading, pk=pk)
    topic.views += 1
    topic.save()
    return render(request, 'forum/topic_posts.html', {'heading': heading,'topic': topic})

def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, heading__pk=pk, pk=topic_pk)
    userpost = request.user.username
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = userpost
            post.save()
            return redirect('topic posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'forum/reply_topic.html', {'topic': topic, 'form': form})
    