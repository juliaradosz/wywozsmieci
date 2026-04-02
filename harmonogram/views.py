import calendar
from datetime import date

from django.shortcuts import get_object_or_404, redirect, render

from .forms import WywozForm
from .models import WywozSmieci

NAZWY_MIESIECY = [
    '', 'Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec',
    'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień'
]

IKONY = {
    'zmieszane': '🗑️',
    'opakowaniowe': '♻️',
    'papier': '📄',
    'biodegradowalne': '🌿',
    'popiol': 'ite',
}


def harmonogram(request):
    dzisiaj = date.today()
    wybrany_miesiac = request.GET.get('miesiac')
    wybrany_rok = request.GET.get('rok', dzisiaj.year)

    if wybrany_miesiac:
        miesiac = int(wybrany_miesiac)
        rok = int(wybrany_rok)
    else:
        miesiac = dzisiaj.month
        rok = dzisiaj.year

    wywozki = WywozSmieci.objects.filter(data__year=rok, data__month=miesiac)
    najblizsze = WywozSmieci.objects.filter(data__gte=dzisiaj).order_by('data')[:5]

    cal = calendar.Calendar(firstweekday=0)
    dni_miesiaca = cal.monthdayscalendar(rok, miesiac)

    wywozki_dict = {}
    for w in wywozki:
        if w.data.day not in wywozki_dict:
            wywozki_dict[w.data.day] = []
        wywozki_dict[w.data.day].append({
            'typ': w.typ_odpadu,
            'id': w.id,
            'ikona': IKONY.get(w.typ_odpadu, ''),
        })

    kalendarz = []
    for tydzien in dni_miesiaca:
        tydzien_dane = []
        for dzien in tydzien:
            if dzien == 0:
                tydzien_dane.append({'dzien': 0, 'wywozki': []})
            else:
                tydzien_dane.append({
                    'dzien': dzien,
                    'wywozki': wywozki_dict.get(dzien, []),
                    'dzisiaj': dzien == dzisiaj.day and miesiac == dzisiaj.month and rok == dzisiaj.year,
                })
        kalendarz.append(tydzien_dane)

    if miesiac == 1:
        prev_miesiac, prev_rok = 12, rok - 1
    else:
        prev_miesiac, prev_rok = miesiac - 1, rok

    if miesiac == 12:
        next_miesiac, next_rok = 1, rok + 1
    else:
        next_miesiac, next_rok = miesiac + 1, rok

    # Ile dni do najbliższego wywozu
    dni_do = None
    if najblizsze:
        dni_do = (najblizsze[0].data - dzisiaj).days

    context = {
        'kalendarz': kalendarz,
        'najblizsze': najblizsze,
        'miesiac': miesiac,
        'rok': rok,
        'nazwa_miesiaca': NAZWY_MIESIECY[miesiac],
        'prev_miesiac': prev_miesiac,
        'prev_rok': prev_rok,
        'next_miesiac': next_miesiac,
        'next_rok': next_rok,
        'dzisiaj': dzisiaj,
        'dni_do': dni_do,
        'ikony': IKONY,
    }
    return render(request, 'harmonogram/index.html', context)


def dodaj(request):
    if request.method == 'POST':
        form = WywozForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('harmonogram')
    else:
        form = WywozForm()
    return render(request, 'harmonogram/formularz.html', {
        'form': form,
        'tytul': 'Dodaj wywóz',
    })


def edytuj(request, pk):
    wywoz = get_object_or_404(WywozSmieci, pk=pk)
    if request.method == 'POST':
        form = WywozForm(request.POST, instance=wywoz)
        if form.is_valid():
            form.save()
            return redirect('harmonogram')
    else:
        form = WywozForm(instance=wywoz)
    return render(request, 'harmonogram/formularz.html', {
        'form': form,
        'tytul': 'Edytuj wywóz',
        'wywoz': wywoz,
    })


def usun(request, pk):
    wywoz = get_object_or_404(WywozSmieci, pk=pk)
    if request.method == 'POST':
        wywoz.delete()
        return redirect('harmonogram')
    return render(request, 'harmonogram/potwierdz_usuniecie.html', {
        'wywoz': wywoz,
    })


def lista(request):
    rok = int(request.GET.get('rok', date.today().year))
    wywozki = WywozSmieci.objects.filter(data__year=rok).order_by('data')

    pogrupowane = {}
    for w in wywozki:
        m = w.data.month
        if m not in pogrupowane:
            pogrupowane[m] = {'nazwa': NAZWY_MIESIECY[m], 'wywozki': []}
        pogrupowane[m]['wywozki'].append(w)

    return render(request, 'harmonogram/lista.html', {
        'pogrupowane': dict(sorted(pogrupowane.items())),
        'rok': rok,
        'ikony': IKONY,
    })
