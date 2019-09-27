from django.db import models


class FavoriteColor(models.Model):
    name = models.CharField(max_length=30)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']
