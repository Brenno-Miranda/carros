from django.db.models.signals import pre_delete, post_delete, pre_save, post_save
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum
from openai_api.client import get_bio_car_ia

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_sum = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_sum
    )

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print('post_save')
    car_inventory_update()
    

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print('post_delete')
    print(instance.brand)
    print(instance.factory_year)
    print(sender)
    car_inventory_update()

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        bio_ia = get_bio_car_ia(
            instance.model,
            instance.brand,
            instance.value,
            instance.factory_year
        )

        instance.bio = bio_ia