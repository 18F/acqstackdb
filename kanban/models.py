from django.db import models


# Create your models here.
class Item(models.Model):
    item = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    days = models.IntegerField()
    # current = models.BooleanField()

    def __str__(self):
        return "%s - %s (%s)" % (self.item, self.state, self.days)


class WIP(models.Model):
    state = models.CharField(max_length=100, blank=False)
    wip_limit = models.IntegerField()
