from django.db import models

class Section(models.Model):
    section = models.CharField(max_length=128)


class Law(models.Model):
    title = models.CharField(max_length=256)
    section_id = models.OneToOneField(
        # Ссылаемся на ...
        Section,
        on_delete=models.CASCADE
    )
