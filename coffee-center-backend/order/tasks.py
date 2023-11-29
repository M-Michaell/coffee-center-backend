from django.utils import timezone
from order.models import OrderDetail
from celery import shared_task

@shared_task
def cancel_old_orders():
    specific_hours = 0
    orders_to_cancel = OrderDetail.objects.filter(
        created_at__lte=timezone.now() - timezone.timedelta(hours=specific_hours),
        payment_method__status='NP',
        payment_method__provider='paypal'
    )

    for order in orders_to_cancel:
        order.delete()
        print('deleted')
