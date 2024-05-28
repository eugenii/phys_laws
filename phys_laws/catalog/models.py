from django.db import models

class Authors(models.Model):
    author = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'учёный'
        verbose_name_plural = 'Учёные'

    def __str__(self):
        return self.author

class Sections(models.Model):
    section = models.CharField(max_length=128, verbose_name='раздел')

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.section

class Laws(models.Model):
    title = models.CharField(max_length=256, verbose_name='название закона')
    text = models.TextField('Закон')
    year = models.BigIntegerField('год')
    author_id = models.ForeignKey(
        # Ссылаемся на ...
        Authors,
        on_delete=models.CASCADE,
        verbose_name='закон'
    )
    section_id = models.ForeignKey(
        Sections,
        on_delete=models.CASCADE,
        related_name='laws',
        verbose_name='раздел'
    )

    formula = models.ImageField('формула', upload_to='formulas', blank=True)

    class Meta:
        verbose_name = 'закон'
        verbose_name_plural = 'Законы'
