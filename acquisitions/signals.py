from django.db.models.signals import pre_delete, post_save
from django.dispatch.dispatcher import receiver
from django.db.models import F

from .models import AwardStatus


@receiver(post_save, sender=AwardStatus)
def increment_ordering(instance, created, **kwargs):
    if created:
        statuses_length = len(AwardStatus.objects.filter(track=instance.track))
        if statuses_length > 1 and instance.is_before_id:
            try:
                # Find object currently pointing to is_before
                current_before = AwardStatus.objects.get(
                        track=instance.track,
                        is_before_id=instance.is_before_id,
                        id__lt=instance.id
                    )
                # Borrow the is_before from that object
                instance.is_before_id = current_before.is_before_id
                instance.ordering = current_before.ordering + 1
                # Update object to point to new status
                current_before.is_before_id = instance.id
                current_before.save()
            except instance.DoesNotExist:
                # This is now the first award status in the process
                instance.ordering = 0
            # Find the object that this status is_before
            next_status = AwardStatus.objects.get(
                    track=instance.track,
                    id=instance.is_before_id
                )
            # Find all objects with that order or higher and increment
            # all filtered objects by 1
            later_statuses = AwardStatus.objects.filter(
                    track=instance.track,
                    ordering__gte=next_status.ordering).update(
                            ordering=F('ordering') + 1)
        elif statuses_length > 1:
            # This is now the last award status in the process
            last_status = AwardStatus.objects.filter(
                    track=instance.track,
                    ordering__gte=0).order_by('ordering').last()
            last_status.is_before_id = instance.id
            last_status.save()
            instance.ordering = last_status.ordering + 1
        else:
            # This is the first entry
            instance.ordering = 0
            instance.is_before = None
        instance.save()


@receiver(pre_delete, sender=AwardStatus)
def decrement_ordering(instance, **kwargs):
    current_before = AwardStatus.objects.get(
            track=instance.track,
            is_before_id=instance.id
        )
    current_before.is_before_id = instance.is_before_id
    current_before.save()
