from django.contrib import admin
from .models import *

from django.contrib import admin
from .models import User_info

class User_infoAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Address', 'FatherName', 'ContactNumber', 'NidNumber', 'NID')
    # Fields to be displayed in the change form
    fields = ('Name', 'Address', 'FatherName', 'ContactNumber', 'NidNumber', 'NID')
class HousePostAdmin(admin.ModelAdmin):
    list_display = ('Area', 'Rent', 'HouseDetails', 'SquareFeet', 'PhoneNo','HouseImage')
    # Fields to be displayed in the change form
    fields = ('Area', 'Rent', 'HouseDetails', 'SquareFeet', 'PhoneNo', 'HouseImage')

admin.site.register(HousePost, HousePostAdmin)
admin.site.register(User_info, User_infoAdmin)


# admin.site.register(save_user_profile)
# admin.site.register(create_user_profile)
# admin.site.register(AdvertisementImage)
# admin.site.register(Amenities)
# admin.site.register(Division)
# admin.site.register(City)
# admin.site.register(AreaName)
# admin.site.register(Block)
# admin.site.register(HouseAddress)
# admin.site.register(House,HotelAdmin)
# admin.site.register(HouseImage)


