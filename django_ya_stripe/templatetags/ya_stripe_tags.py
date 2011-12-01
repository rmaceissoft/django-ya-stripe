from django import template

from django_ya_stripe.models import SyncChargedObject

register = template.Library()

@register.filter(name='has_by_refund')
def has_by_refund(obj):
    return SyncChargedObject.objects.has_by_refund_for_model(obj).exists()
