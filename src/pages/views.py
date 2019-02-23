from django.shortcuts import render

# Create your views here.
def index(request):

    template_name = "pages/index.html"
    context = {}
    return render(request, template_name, context)

def contact(request):

    template_name = "pages/contact.html"
    context = {}
    return render(request, template_name, context)

def about(request):

    template_name = "pages/about.html"
    context = {}
    return render(request, template_name, context)
