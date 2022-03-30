from django.db import models

class BlogStatusChoices(models.TextChoices):
    draft = 'draft','Draft'
    published = 'published', 'Published'