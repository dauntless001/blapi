from django.db import models

class PostStatusChoices(models.TextChoices):
    draft = 'draft','Draft'
    published = 'published', 'Published'