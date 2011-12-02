import datetime
import logging
import stripe

from django.conf import settings

from django_ya_stripe.models import SyncChargedObject

def sync_charge_object(obj, stripe_charge):
    #TODO: add logic of call stripe.Charge.create method here...
    SyncChargedObject.objects.charge_object(obj, stripe_charge)


def refund_object(obj, amount_to_refund=None):
    """
    refund a given amount of django model instance specified
    returns:
        a tuple (SyncChargedObject instance, refund success?)
    """
    try:
        sync_charged_object = SyncChargedObject.objects.for_model(obj).get()
    except SyncChargedObject.DoesNotExists, ex:
        raise ex
    else:
        try:
            if not amount_to_refund:
                amount_to_refund = sync_charged_object.amount_by_refund
            stripe_charge = stripe.Charge.retrieve(sync_charged_object.stripe_charge_id, settings.STRIPE_SECRET)
            stripe_charge.refund(amount=int(amount_to_refund*100))
        except Exception, ex:
            logging.error(ex)
            return sync_charged_object, False
        else:
            sync_charged_object.amount_refunded += amount_to_refund
            sync_charged_object.last_updated = datetime.datetime.now()
            sync_charged_object.save()
            return sync_charged_object, True

        

  