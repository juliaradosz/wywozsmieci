from django.db import models


class WywozSmieci(models.Model):
    TYPY_ODPADOW = [
        ('zmieszane', 'Zmieszane odpady komunalne'),
        ('opakowaniowe', 'Zmieszane odpady opakowaniowe'),
        ('papier', 'Papier'),
        ('szklo', 'Szkło'),
        ('biodegradowalne', 'Odpady biodegradowalne'),
        ('popiol', 'Popiół'),
    ]

    data = models.DateField()
    typ_odpadu = models.CharField(max_length=20, choices=TYPY_ODPADOW)

    class Meta:
        ordering = ['data']
        verbose_name = 'Wywóz śmieci'
        verbose_name_plural = 'Wywozy śmieci'

    def __str__(self):
        return f"{self.data} - {self.get_typ_odpadu_display()}"
