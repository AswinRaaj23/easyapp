from django.shortcuts import render

# Create your views here.
def starting_page(request):
    return render(request, 'blog/index.html')

def posts_list(request):
    pass

def posts_detail(request):
    pass