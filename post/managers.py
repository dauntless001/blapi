from django.db import models
from blapi.utils.choices import PostStatusChoices


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=PostStatusChoices.published)
    
    def draft(self):
        return self.filter(status=PostStatusChoices.draft)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()
    
    def draft(self):
        return self.get_queryset().draft()