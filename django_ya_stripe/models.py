import datetime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey

from .managers import SyncChargedObjectManager

class SyncChargedObject(models.Model):

    # The Django object charged with stripe that's been synced.
    # shopping cart or order instance
    content_type = models.ForeignKey(ContentType, related_name='stripes_charges_synced_objects')
    object_id    = models.PositiveIntegerField()
    object       = GenericForeignKey('content_type', 'object_pk')

    # The Stripe's charges that's been synced to.
    stripe_charge_id = models.CharField(max_length=50)

    amount_charged = models.DecimalField(max_digits=9, decimal_places=2)
    amount_refunded = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    # When we last did a sync.
    last_updated = models.DateTimeField(default=datetime.datetime.now)

    objects = SyncChargedObjectManager()

