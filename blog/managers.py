from django.db import models
from blapi.utils.choices import BlogStatusChoices


class BlogQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=BlogStatusChoices.published)
    
    def draft(self):
        return self.filter(status=BlogStatusChoices.draft)


class BlogManager(models.Manager):
    def get_queryset(self):
        return BlogQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()
    
    def draft(self):
        return self.get_queryset().draft()