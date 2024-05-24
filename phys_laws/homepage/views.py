from django.shortcuts import render
from catalog.models import Laws


def index(request):
    # laws_list = Laws.objects.values('title', 'text', 'year')  # --.objects.all() - все
    # laws_list = Laws.objects.filter(year__gt=1700)
    # laws_list = Laws.objects.values('title', 'text', 'year', 'section_id__section')
    laws_list = Laws.objects.select_related('section_id')
    context = {
        'laws_list': laws_list,
    }
    template_name = 'homepage/index.html'

    return render(request, template_name, context)


def about(request):
    template_name = 'about/about.html'
    return render(request, template_name)

