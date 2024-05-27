from django.shortcuts import render
from phys_laws.forms import AuthorForm
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
        'text': request.GET.get('year'),
    }
    return render(request, template_name, context)

def author(request):
    template_name = 'catalog/form_author.html'
    form = AuthorForm()
    context = {'form': form}
    print(request.GET)
    return render(request, template_name, context)
