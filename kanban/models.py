from django.db import models


# Create your models here.
class KanbanBoard(models.Model):
    name = models.CharField(max_length=100, blank=False)

    objects = models.Manager()

    class Meta:
        abstract = True


class KanbanProcess(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    wip_limit = models.IntegerField(default=5)
    time_allotment = models.IntegerField(default=5)
    ordering = models.IntegerField(editable=False, null=True)
    is_before = models.ForeignKey('self', null=True, blank=True,
                                  on_delete=models.DO_NOTHING)

    objects = models.Manager()

    def __str__(self):
        return "%s - %s" % (self.name, self.owner)

    class Meta:
        abstract = True


class KanbanCard(models.Model):
    objects = models.Manager()
    # current = models.BooleanField()

    # def __str__(self):
    #     return "%s - %s (%s)" % (self.item, self.state, self.days)

    class Meta:
        abstract = True
