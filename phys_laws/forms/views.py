from django.shortcuts import render

# Create your views here.

def form0(request):
    template_name = 'catalog/form0.html'
    context = {
        'test': "from_form_0",
    }
    return render(request, template_name, context)

def resp0(request, name):
    template_name = 'catalog/form_res.html'
    context = {
        'text': name,
    }
    return render(request, template_name, context)
