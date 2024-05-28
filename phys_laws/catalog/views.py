from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from .models import Laws
from .forms import LawForm

class LawsListView(ListView):
    # Указываем модель, с которой работает CBV...
    model = Laws
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 3


def law_list(request):
    template_name = 'catalog/law_list.html'
    title = 'список законов'
    laws = Laws.objects.all()
    context = {
        'laws': laws,
        'title': title,
    }
    return render(request, template_name, context)


def law_detail(request, pk):
    template_name = "catalog/law_detail.html"
    law = Laws.objects.get(pk=pk+1)
    context = {
        # 'law_detail': phys_laws_catalog[pk]  # старый вариант
        'law': law,
    }
    return render(request, template_name, context)


def law_add(request, pk=None):
    # Добавим закон в базу
    template_name = 'catalog/law_add.html'
    if pk is not None:
        # Получаем объект модели или выбрасываем 404 ошибку.
        instance = get_object_or_404(Laws, pk=pk)
    # Если в запросе не указан pk
    # (если получен запрос к странице создания записи):
    else:
        # Связывать форму с объектом не нужно, установим значение None.
        instance = None
    # Передаём в форму либо данные из запроса, либо None. 
    # В случае редактирования прикрепляем объект модели.
    form = LawForm(
        request.POST or None,
        # Файлы, переданные в запросе, указываются отдельно.
        files=request.FILES or None,
        instance=instance
    )
    context = {'form': form}
    # Сохраняем данные, полученные из формы, и отправляем ответ:
    if form.is_valid():
        form.save()
    
    return render(request, template_name, context)

def law_delete(request, pk):
    # Получаем объект модели или выбрасываем 404 ошибку.
    instance = get_object_or_404(Laws, pk=pk)
    # В форму передаём только объект модели;
    # передавать в форму параметры запроса не нужно.
    form = LawForm(instance=instance)
    context = {'form': form}
    # Если был получен POST-запрос...
    if request.method == 'POST':
        # ...удаляем объект:
        instance.delete()
        # ...и переадресовываем пользователя на страницу со списком записей.
        return redirect('catalog:law_list')
    # Если был получен GET-запрос — отображаем форму.
    return render(request, 'catalog/law_add.html', context)


phys_laws_catalog = [
    {
        'id': 1,
        'title': 'Закон Ома для участка цепи',
        'section': 'Электродинамика',
        'author': 'Георг Ом',
        'year': 1827,
        'text': 'Сила тока в участке цепи прямо пропорциональна <b>напряжению</b>'
                ' на концах этого участка и обратно пропорциональна'
                ' сопротивлению этого участка',
        'country': 'Германия',
    },
    {
        'id': 2,
        'title': '1 закон Ньютона',
        'section': 'Механика',
        'author': 'Исаак Ньютон',
        'year': 1687,
        'text': 'Существуют такие системы отсчёта, в которых тела сохраняют '
                'состояние покоя или прямоленейного и равномерного двжения'
                ' если равнодействующая всех сил, приложенных к телу'
                ' равна нулю',
        'country': 'Англия',
    },
    {
        'id': 3,
        'title': 'Закон Архимеда',
        'section': 'Механика',
        'author': 'Архимед',
        'year': -300,
        'text': 'На тело, погружённое в жидкость или в газ действует'
                ' выталкивающая сила, равная весу вытесненной жидкости (газа)',
        'country': 'Греция',
    },
    {
        'id': 4,
        'title': 'Закон электромагнитной индукции',
        'section': 'Электродинамика',
        'author': 'Майкл Фарадей',
        'year': 1857,
        'text': 'ЭДС индукции в замкнутом контуре равна и противоположна'
                ' по знаку скорости изменения магнитного потока через'
                ' поверхность, ограниченную контуром.',
        'country': 'Англия',
    },
    {
        'id': 5,
        'title': 'Давление смеси газов',
        'section': 'МКТ и Т/Д',
        'author': 'Джон Дальтон',
        'year': 1801,
        'text': 'Давление смеси газов равно сумме'
                ' парциальных давлений газов смеси',
        'country': 'Англия',
    },
]
