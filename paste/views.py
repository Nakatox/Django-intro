from django.shortcuts import render
from paste.models import Markdown
# Create your views here.

def index(request):
    markdown = Markdown.objects.all()
    return render(request, "markdown/index.html", context = {"markdowns":markdown} )
    
def markdownview(request, url):
    un_markdown = Markdown.objects.get(url=url)
    return render(request, "markdown/markdown.html", context = {"markdown":un_markdown})