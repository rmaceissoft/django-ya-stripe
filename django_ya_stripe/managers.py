import decimal
from django.db.models import manager
from django.contrib.contenttypes.models import ContentType
from django.db.models import F


class SyncChargedObjectManager(manager.Manager):

    def for_model(self, obj):
        """
        look for sync charge record for a given model
        Returns::
            QuerySet instance
        """
        return self.filter(
            content_type = ContentType.objects.get_for_model(obj),
            object_id = obj.pk,
        )

    def has_by_refund_for_model(self, obj):
        """
        look for sync charge record for a given model, if it is pending by refund
        Returns::
            QuerySet instance
        """
        return self.for_model(obj).filter(amount_charged__gt = F('amount_refunded'))

    
    def charge_object(self, django_obj, stripe_charged_obj):
        """
        Mark ``django_obj`` as having been synced to ``stripe_charged_obj``.

        Returns ``(SyncChargedObject, created)``, just like ``get_or_create()``.
        """
        defaults = dict(
            stripe_charge_id   = stripe_charged_obj.id,
            amount_charged     = decimal.Decimal(stripe_charged_obj.amount)/100,
        )

        so, created = self.get_or_create(
            content_type = ContentType.objects.get_for_model(django_obj),
            object_id = django_obj.pk,
            defaults = defaults,
        )
        if not created:
            so.__dict__.update(defaults)
            so.save()

        return so, created