from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class User_info(models.Model):
    
    
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Address = models.TextField()
    FatherName = models.CharField(max_length=100)
    ContactNumber = models.CharField(max_length=20)
    NidNumber = models.CharField(max_length=20)
    NID = models.ImageField(upload_to='User/')
    
    def __str__(self):
            return self.FatherName
    
class HousePost(models.Model):
    
    Area = models.CharField(max_length=100)
    Rent = models.CharField(max_length=6)
    HouseDetails = models.CharField( max_length=200)
    SquareFeet = models.CharField( max_length=50)
    PhoneNo = models.IntegerField()
    HouseImage = models.ImageField(upload_to='Post/')

    def __str__(self) -> str:
        return self.HouseDetails 
    
# class Amenities(models.Model):
#     amenity= models.CharField(max_length=100)
#     created_at = models.DateField(auto_now_add=True)
#     Updated_at = models.DateField(auto_now=True)
    
#     def __str__(self) -> str:
#         return self.amenity

# class Division(models.Model):
#     division = models.CharField(max_length=100)
#     created_at = models.DateField(auto_now_add=True)
#     Updated_at = models.DateField(auto_now=True)
#     def __str__(self) -> str:
#         return self.division
    
# class City(models.Model):
#     city = models.CharField(max_length=100)
#     created_at = models.DateField(auto_now_add=True)
#     Updated_at = models.DateField(auto_now=True)
#     def __str__(self) -> str:
#         return self.city
    
# class AreaName(models.Model):
#     area_name = models.CharField(max_length=100)
#     created_at = models.DateField(auto_now_add=True)
#     Updated_at = models.DateField(auto_now=True)
#     def __str__(self) -> str:
#         return self.area_name
    
# class Block(models.Model):
#     block= models.CharField(max_length=100)
#     created_at = models.DateField(auto_now_add=True)
#     Updated_at = models.DateField(auto_now=True)
#     def __str__(self) -> str:
#         return self.block

# class HouseAddress(models.Model):
#     Division = models.ManyToManyField(Division)
#     City = models.ManyToManyField(City)
#     AreaName = models.ManyToManyField(AreaName)
#     Block = models.ManyToManyField(Block)
#     house_name= models.CharField(max_length=100)
#     house_no =models.CharField(max_length=100)
#     created_at = models.DateField(auto_now_add=True)
#     Updated_at = models.DateField(auto_now=True)
    
# class House(models.Model):
#     banner_image = models.ImageField(upload_to='House')
#     house_rent = models.IntegerField()
#     house_description = models.TextField()
#     no_of_bedrooms= models.IntegerField()
#     amenities= models.ManyToManyField(Amenities)
#     created_at = models.DateField(auto_now_add=True)
#     Updated_at = models.DateField(auto_now=True)
    
#     def __str__(self) -> str:
#         return self.house_description


# class HouseImage(models.Model):
#     house=models.ForeignKey(House , on_delete=models.CASCADE)
#     image=models.ImageField(upload_to='House')    
#     created_at = models.DateField(auto_now_add=True)
#     Updated_at = models.DateField(auto_now=True)
#     def __str__(self) -> str:
#         return self.house.house_description


# class RentalAdvertisement(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     address = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     bedrooms = models.IntegerField()
#     bathrooms = models.IntegerField()
#     square_feet = models.IntegerField()
#     is_published = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

# class AdvertisementImage(models.Model):
#     advertisement = models.ForeignKey(RentalAdvertisement, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='rental_images')

#     def __str__(self):
#         return f"{self.advertisement.title} - Image"





# from django.db import models
# from django.contrib.auth.models import User 
# import random
# # Create your models here.
# class UserProfile(models.Model):

#     USER_TYPES = [
#         ('Public', 'Public'),
#         ('Owner','Owner'),
#         ('Admin', 'Admin'),
#     ]
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     profilePicture = models.ImageField(blank=True, null=True)
#     DOB = models.DateField()
#     address = models.TextField()
#     contact_No = models.IntegerField()
#     gender=models.CharField(max_length=50,null=True,blank=True)
#     userType = models.CharField(max_length=10, choices=USER_TYPES, default='Public')
#     verified = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.user.username

# class OTP(models.Model):
#     def Get_OTP():
#         return random.randint(100000, 999999)
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     otp = models.IntegerField(default=Get_OTP)
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.user.username