from django.db import models

class Category(models.Model):
    # Attributes
    label = models.CharField(max_length=255, unique=True)

    # Methods
    def __str__(self):
        return '%s' % self.label

    # Meta-class
    class Meta:
        ordering = ('label',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Poll(models.Model):
    # Enums
    COLOR_CHOICES = (
        ('0', 'red'),
        ('1', 'black'),
        ('2', 'blue'),
    )
    
    # Attributes
    question = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=1, choices=COLOR_CHOICES)
    category = models.ForeignKey(Category, related_name='polls')

    # Methods
    def __str__(self):
        return '(%s) %s' % (self.get_color_display(), self.question)

    # Meta-class
    class Meta:
        ordering = ('question', 'color',)
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'