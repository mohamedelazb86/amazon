from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user=models.OneToOneField(User,related_name='profile_user',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photo_user')
    code=models.CharField(max_length=25,default=generate_code)

    def __str__(self):
        return str(self.user)
# create signals
@receiver(post_save,sender=User)   
def create_profile(sender,instance,created,**kwargs):
    if created :
        Profile.objects.create(
            user=instance
        )


NUMBER_TYPE=[
    ('Home','Home'),
    ('Office','Office'),
    ('Others','Others')
    ]
    
class Contact(models.Model):
    user=models.ForeignKey(User,related_name='contact_user',on_delete=models.CASCADE)
    number=models.CharField(max_length=25)
    number_type=models.CharField(max_length=100,choices=NUMBER_TYPE)

    def __str__(self):
        return str(self.user)


ADDRESS_TYPE=[
     ('Home','Home'),
    ('Office','Office'),
    ('Others','Others')
    ]
class Address(models.Model):
    user=models.ForeignKey(User,related_name='address_user',on_delete=models.CASCADE)
    address=models.CharField(max_length=150)
    address_type=models.CharField(max_length=100,choices=ADDRESS_TYPE)

    def __str__(self):
        return str(self.user)
