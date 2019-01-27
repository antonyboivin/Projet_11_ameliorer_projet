from django.shortcuts import render
from .models import Heading

def forum(request):
    headings = Heading.objects.all()
    return render(request, 'forum/forum_home_page.html', {'headings': headings})