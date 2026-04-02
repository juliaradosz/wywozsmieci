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

        # ZMIESZANE: 14.01, 11.02, 11.03, 15.04, 20.05, 10.06, 24.06, 8.07, 22.07, 5.08, 19.08, 16.09, 14.10, 12.11, 9.12
        dane += [
            (date(2026, 1, 14), 'zmieszane'),
            (date(2026, 2, 11), 'zmieszane'),
            (date(2026, 3, 11), 'zmieszane'),
            (date(2026, 4, 15), 'zmieszane'),
            (date(2026, 5, 20), 'zmieszane'),
            (date(2026, 6, 10), 'zmieszane'),
            (date(2026, 6, 24), 'zmieszane'),
            (date(2026, 7, 8), 'zmieszane'),
            (date(2026, 7, 22), 'zmieszane'),
            (date(2026, 8, 5), 'zmieszane'),
            (date(2026, 8, 19), 'zmieszane'),
            (date(2026, 9, 16), 'zmieszane'),
            (date(2026, 10, 14), 'zmieszane'),
            (date(2026, 11, 12), 'zmieszane'),
            (date(2026, 12, 9), 'zmieszane'),
        ]

        # OPAKOWANIOWE
        dane += [
            (date(2026, 1, 7), 'opakowaniowe'),
            (date(2026, 2, 4), 'opakowaniowe'),
            (date(2026, 3, 4), 'opakowaniowe'),
            (date(2026, 4, 8), 'opakowaniowe'),
            (date(2026, 5, 6), 'opakowaniowe'),
            (date(2026, 6, 3), 'opakowaniowe'),
            (date(2026, 7, 1), 'opakowaniowe'),
            (date(2026, 8, 5), 'opakowaniowe'),
            (date(2026, 9, 2), 'opakowaniowe'),
            (date(2026, 10, 7), 'opakowaniowe'),
            (date(2026, 11, 4), 'opakowaniowe'),
            (date(2026, 12, 2), 'opakowaniowe'),
        ]

        # BIODEGRADOWALNE
        dane += [
            (date(2026, 4, 22), 'biodegradowalne'),
            (date(2026, 5, 8), 'biodegradowalne'),
            (date(2026, 6, 17), 'biodegradowalne'),
            (date(2026, 7, 3), 'biodegradowalne'),
            (date(2026, 8, 12), 'biodegradowalne'),
            (date(2026, 9, 23), 'biodegradowalne'),
            (date(2026, 10, 21), 'biodegradowalne'),
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
