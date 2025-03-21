from django.db.models.signals import pre_save, post_save,pre_delete, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from gemini_api. client import car_gemini_ai

@receiver(pre_save, sender=Car) 
def car_pre_save(sender, instance, **kwargs): 
   if not instance.bio: ai_bio = car_gemini_ai( instance.model, instance.brand, instance.factory_years ) 
   instance.bio = ai_bio

def car_invnetury_update():
   cars_count = Car.objects.all().count()
   cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']

   CarInventory.objects.create(cars_count=cars_count, cars_value= cars_value)

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
  car_invnetury_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
   car_invnetury_update()