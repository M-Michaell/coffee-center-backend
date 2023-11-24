from django.db import models
from django.utils import timezone

class SoftDeletionQuerySet(models.QuerySet):
      def delete(self, hard=False):
        if hard:
            super().delete()  
        else:
            self.update(deleted=True, deleted_at=timezone.now()) 


class SoftDeletionManager(models.Manager):
    def get_queryset(self):
        return SoftDeletionQuerySet(self.model, using=self._db).filter(deleted=False)

class SoftDeletionModel(models.Model):
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)

    objects = SoftDeletionManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.deleted = True
        self.deleted_at=timezone.now()
        self.save()

    def restore(self):
        self.deleted = False
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True