from django.db import models

class Authors(models.Model):
    author = models.CharField(max_length=128)

class Sections(models.Model):
    section = models.CharField(max_length=128)

class Laws(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    year = models.BigIntegerField()
    author_id = models.OneToOneField(
        # Ссылаемся на ...
        Authors,
        on_delete=models.CASCADE
    )
    section_id = models.ForeignKey(
        Sections,
        on_delete=models.CASCADE
    )
