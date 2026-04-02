from datetime import date

from django.core.management.base import BaseCommand

from harmonogram.models import WywozSmieci


class Command(BaseCommand):
    help = 'Ładuje harmonogram wywozu śmieci gminy Przodkowo na 2026 rok'

    def handle(self, *args, **options):
        WywozSmieci.objects.all().delete()

        dane = []

        # STYCZEŃ 2026
        # Żółty (zmieszane): 5, 19
        # Zielony (opakowaniowe): 7
        # Szary (popiół): 12
        dane += [
            (date(2026, 1, 5), 'zmieszane'),
            (date(2026, 1, 19), 'zmieszane'),
            (date(2026, 1, 7), 'opakowaniowe'),
            (date(2026, 1, 12), 'popiol'),
        ]

        # LUTY 2026
        # Żółty (zmieszane): 2, 16
        # Zielony (opakowaniowe): 4
        # Szary (popiół): 9
        dane += [
            (date(2026, 2, 2), 'zmieszane'),
            (date(2026, 2, 16), 'zmieszane'),
            (date(2026, 2, 4), 'opakowaniowe'),
            (date(2026, 2, 9), 'popiol'),
        ]

        # MARZEC 2026
        # Żółty (zmieszane): 2, 16
        # Zielony (opakowaniowe): 4
        # Niebieski (papier): 18
        # Szary (popiół): 9
        dane += [
            (date(2026, 3, 2), 'zmieszane'),
            (date(2026, 3, 16), 'zmieszane'),
            (date(2026, 3, 4), 'opakowaniowe'),
            (date(2026, 3, 18), 'papier'),
            (date(2026, 3, 9), 'popiol'),
        ]

        # KWIECIEŃ 2026
        # Żółty (zmieszane): 6, 20
        # Zielony (opakowaniowe): 8
        # Brązowy (bio): 22
        dane += [
            (date(2026, 4, 6), 'zmieszane'),
            (date(2026, 4, 20), 'zmieszane'),
            (date(2026, 4, 8), 'opakowaniowe'),
            (date(2026, 4, 22), 'biodegradowalne'),
        ]

        # MAJ 2026
        # Żółty (zmieszane): 4, 18
        # Zielony (opakowaniowe): 6
        # Niebieski (papier): 20
        # Brązowy (bio): 8
        dane += [
            (date(2026, 5, 4), 'zmieszane'),
            (date(2026, 5, 18), 'zmieszane'),
            (date(2026, 5, 6), 'opakowaniowe'),
            (date(2026, 5, 20), 'papier'),
            (date(2026, 5, 8), 'biodegradowalne'),
        ]

        # CZERWIEC 2026
        # Żółty (zmieszane): 1, 15, 29
        # Zielony (opakowaniowe): 3
        # Brązowy (bio): 17
        dane += [
            (date(2026, 6, 1), 'zmieszane'),
            (date(2026, 6, 15), 'zmieszane'),
            (date(2026, 6, 29), 'zmieszane'),
            (date(2026, 6, 3), 'opakowaniowe'),
            (date(2026, 6, 17), 'biodegradowalne'),
        ]

        # LIPIEC 2026
        # Żółty (zmieszane): 13, 27
        # Zielony (opakowaniowe): 1
        # Niebieski (papier): 15
        # Brązowy (bio): 3
        dane += [
            (date(2026, 7, 13), 'zmieszane'),
            (date(2026, 7, 27), 'zmieszane'),
            (date(2026, 7, 1), 'opakowaniowe'),
            (date(2026, 7, 15), 'papier'),
            (date(2026, 7, 3), 'biodegradowalne'),
        ]

        # SIERPIEŃ 2026
        # Żółty (zmieszane): 10, 24
        # Zielony (opakowaniowe): 5
        # Brązowy (bio): 12
        dane += [
            (date(2026, 8, 10), 'zmieszane'),
            (date(2026, 8, 24), 'zmieszane'),
            (date(2026, 8, 5), 'opakowaniowe'),
            (date(2026, 8, 12), 'biodegradowalne'),
        ]

        # WRZESIEŃ 2026
        # Żółty (zmieszane): 7, 21
        # Zielony (opakowaniowe): 2
        # Niebieski (papier): 9
        # Brązowy (bio): 23
        dane += [
            (date(2026, 9, 7), 'zmieszane'),
            (date(2026, 9, 21), 'zmieszane'),
            (date(2026, 9, 2), 'opakowaniowe'),
            (date(2026, 9, 9), 'papier'),
            (date(2026, 9, 23), 'biodegradowalne'),
        ]

        # PAŹDZIERNIK 2026
        # Żółty (zmieszane): 5, 19
        # Zielony (opakowaniowe): 7
        # Brązowy (bio): 21
        dane += [
            (date(2026, 10, 5), 'zmieszane'),
            (date(2026, 10, 19), 'zmieszane'),
            (date(2026, 10, 7), 'opakowaniowe'),
            (date(2026, 10, 21), 'biodegradowalne'),
        ]

        # LISTOPAD 2026
        # Żółty (zmieszane): 2, 16
        # Zielony (opakowaniowe): 4
        # Niebieski (papier): 18
        # Szary (popiół): 30
        dane += [
            (date(2026, 11, 2), 'zmieszane'),
            (date(2026, 11, 16), 'zmieszane'),
            (date(2026, 11, 4), 'opakowaniowe'),
            (date(2026, 11, 18), 'papier'),
            (date(2026, 11, 30), 'popiol'),
        ]

        # GRUDZIEŃ 2026
        # Żółty (zmieszane): 7, 21
        # Zielony (opakowaniowe): 2
        # Szary (popiół): 14
        dane += [
            (date(2026, 12, 7), 'zmieszane'),
            (date(2026, 12, 21), 'zmieszane'),
            (date(2026, 12, 2), 'opakowaniowe'),
            (date(2026, 12, 14), 'popiol'),
        ]

        obiekty = [WywozSmieci(data=d, typ_odpadu=t) for d, t in dane]
        WywozSmieci.objects.bulk_create(obiekty)

        self.stdout.write(self.style.SUCCESS(
            f'Załadowano {len(obiekty)} wpisów do harmonogramu.'
        ))
