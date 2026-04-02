from datetime import date

from django.shortcuts import render

from .models import WywozSmieci


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

    wywozki = WywozSmieci.objects.filter(
        data__year=rok,
        data__month=miesiac,
    )

    najblizsze = WywozSmieci.objects.filter(data__gte=dzisiaj).order_by('data')[:5]

    import calendar
    cal = calendar.Calendar(firstweekday=0)
    dni_miesiaca = cal.monthdayscalendar(rok, miesiac)

    wywozki_dict = {}
    for w in wywozki:
        if w.data.day not in wywozki_dict:
            wywozki_dict[w.data.day] = []
        wywozki_dict[w.data.day].append(w.typ_odpadu)

    kalendarz = []
    for tydzien in dni_miesiaca:
        tydzien_dane = []
        for dzien in tydzien:
            if dzien == 0:
                tydzien_dane.append({'dzien': 0, 'typy': []})
            else:
                tydzien_dane.append({
                    'dzien': dzien,
                    'typy': wywozki_dict.get(dzien, []),
                    'dzisiaj': dzien == dzisiaj.day and miesiac == dzisiaj.month and rok == dzisiaj.year,
                })
        kalendarz.append(tydzien_dane)

    nazwy_miesiecy = [
        '', 'Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec',
        'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień'
    ]

    if miesiac == 1:
        prev_miesiac, prev_rok = 12, rok - 1
    else:
        prev_miesiac, prev_rok = miesiac - 1, rok

    if miesiac == 12:
        next_miesiac, next_rok = 1, rok + 1
    else:
        next_miesiac, next_rok = miesiac + 1, rok

    context = {
        'kalendarz': kalendarz,
        'najblizsze': najblizsze,
        'miesiac': miesiac,
        'rok': rok,
        'nazwa_miesiaca': nazwy_miesiecy[miesiac],
        'prev_miesiac': prev_miesiac,
        'prev_rok': prev_rok,
        'next_miesiac': next_miesiac,
        'next_rok': next_rok,
        'dzisiaj': dzisiaj,
    }
    return render(request, 'harmonogram/index.html', context)
