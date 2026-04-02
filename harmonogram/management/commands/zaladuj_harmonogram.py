from datetime import date

from django.core.management.base import BaseCommand

from harmonogram.models import WywozSmieci


class Command(BaseCommand):
    help = 'Ładuje harmonogram wywozu śmieci gminy Przodkowo na 2026 rok'

    def handle(self, *args, **options):
        WywozSmieci.objects.all().delete()

        dane = []

        # PAPIER: 13.01, 10.02, 10.03, 14.04, 12.05, 09.06, 14.07, 11.08, 8.09, 13.10, 10.11, 8.12
        dane += [
            (date(2026, 1, 13), 'papier'),
            (date(2026, 2, 10), 'papier'),
            (date(2026, 3, 10), 'papier'),
            (date(2026, 4, 14), 'papier'),
            (date(2026, 5, 12), 'papier'),
            (date(2026, 6, 9), 'papier'),
            (date(2026, 7, 14), 'papier'),
            (date(2026, 8, 11), 'papier'),
            (date(2026, 9, 8), 'papier'),
            (date(2026, 10, 13), 'papier'),
            (date(2026, 11, 10), 'papier'),
            (date(2026, 12, 8), 'papier'),
        ]

        # OPAKOWANIOWE (plastik): 14.01, 11.02, 11.03, 15.04, 20.05, 10.06, 24.06, 8.07, 22.07, 5.08, 19.08, 16.09, 14.10, 12.11, 9.12
        dane += [
            (date(2026, 1, 14), 'opakowaniowe'),
            (date(2026, 2, 11), 'opakowaniowe'),
            (date(2026, 3, 11), 'opakowaniowe'),
            (date(2026, 4, 15), 'opakowaniowe'),
            (date(2026, 5, 20), 'opakowaniowe'),
            (date(2026, 6, 10), 'opakowaniowe'),
            (date(2026, 6, 24), 'opakowaniowe'),
            (date(2026, 7, 8), 'opakowaniowe'),
            (date(2026, 7, 22), 'opakowaniowe'),
            (date(2026, 8, 5), 'opakowaniowe'),
            (date(2026, 8, 19), 'opakowaniowe'),
            (date(2026, 9, 16), 'opakowaniowe'),
            (date(2026, 10, 14), 'opakowaniowe'),
            (date(2026, 11, 12), 'opakowaniowe'),
            (date(2026, 12, 9), 'opakowaniowe'),
        ]

        # ZMIESZANE: 7.01, 4.02, 4.03, 8.04, 6.05, 3.06, 1.07, 5.08, 2.09, 7.10, 4.11, 2.12
        dane += [
            (date(2026, 1, 7), 'zmieszane'),
            (date(2026, 2, 4), 'zmieszane'),
            (date(2026, 3, 4), 'zmieszane'),
            (date(2026, 4, 8), 'zmieszane'),
            (date(2026, 5, 6), 'zmieszane'),
            (date(2026, 6, 3), 'zmieszane'),
            (date(2026, 7, 1), 'zmieszane'),
            (date(2026, 8, 5), 'zmieszane'),
            (date(2026, 9, 2), 'zmieszane'),
            (date(2026, 10, 7), 'zmieszane'),
            (date(2026, 11, 4), 'zmieszane'),
            (date(2026, 12, 2), 'zmieszane'),
        ]

        # SZKŁO: 16.01, 13.03, 15.05, 17.07, 11.09, 20.11
        dane += [
            (date(2026, 1, 16), 'szklo'),
            (date(2026, 3, 13), 'szklo'),
            (date(2026, 5, 15), 'szklo'),
            (date(2026, 7, 17), 'szklo'),
            (date(2026, 9, 11), 'szklo'),
            (date(2026, 11, 20), 'szklo'),
        ]

        # BIODEGRADOWALNE: 20.01, 17.02, 17.03, 21.04, 5.05, 19.05, 2.06, 23.06, 7.07, 21.07, 4.08, 18.08, 15.09, 29.09, 27.10, 24.11, 29.12
        dane += [
            (date(2026, 1, 20), 'biodegradowalne'),
            (date(2026, 2, 17), 'biodegradowalne'),
            (date(2026, 3, 17), 'biodegradowalne'),
            (date(2026, 4, 21), 'biodegradowalne'),
            (date(2026, 5, 5), 'biodegradowalne'),
            (date(2026, 5, 19), 'biodegradowalne'),
            (date(2026, 6, 2), 'biodegradowalne'),
            (date(2026, 6, 23), 'biodegradowalne'),
            (date(2026, 7, 7), 'biodegradowalne'),
            (date(2026, 7, 21), 'biodegradowalne'),
            (date(2026, 8, 4), 'biodegradowalne'),
            (date(2026, 8, 18), 'biodegradowalne'),
            (date(2026, 9, 15), 'biodegradowalne'),
            (date(2026, 9, 29), 'biodegradowalne'),
            (date(2026, 10, 27), 'biodegradowalne'),
            (date(2026, 11, 24), 'biodegradowalne'),
            (date(2026, 12, 29), 'biodegradowalne'),
        ]

        # POPIÓŁ
        dane += [
            (date(2026, 1, 12), 'popiol'),
            (date(2026, 2, 9), 'popiol'),
            (date(2026, 3, 9), 'popiol'),
            (date(2026, 11, 30), 'popiol'),
            (date(2026, 12, 14), 'popiol'),
        ]

        obiekty = [WywozSmieci(data=d, typ_odpadu=t) for d, t in dane]
        WywozSmieci.objects.bulk_create(obiekty)

        self.stdout.write(self.style.SUCCESS(
            f'Załadowano {len(obiekty)} wpisów do harmonogramu.'
        ))
