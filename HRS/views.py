import os
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from HRSApp.models import *
from HRSApp.views import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def sign_up(request):

    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')            
        username = request.POST.get('username')
        email = request.POST.get('email') 
        password = request.POST.get('password')        
        new_user=User.objects.create_user(username,email,password)
        new_user.first_name=fname
        new_user.last_name=lname        
        new_user.save()
        
        return redirect('login')            
    return render(request,"signUp.html",{})
    
def login_page(request): 

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse('Error, User does not exist')
        login(request, user)
        return redirect('home')
    return render(request, 'login.html')


def home_page(request):
    return render(request,"homePage.html")


def profile(request):

    if request.method == 'POST':
        # Retrieve the form data
        Name = request.POST.get('Name')
        Address = request.POST.get('Address')
        FatherName = request.POST.get('FatherName')
        ContactNumber = request.POST.get('ContactNumber')
        NidNumber = request.POST.get('NidNumber')
        NID = request.FILES.get('NID')

        new_profile = User_info(
            Name = Name,
            Address = Address,
            FatherName = FatherName,
            ContactNumber = ContactNumber,
            NidNumber = NidNumber,
            NID = NID
        )

        new_profile.save()  # Save the instance to the database

        return redirect('home')  # Redirect to the home page after successful profile creation

    return render(request, 'profile.html')



def RentPost(request):
    
    if request.method == "POST":
        Area = request.POST.get('Area')
        Rent = request.POST.get('Rent')
        HouseDetails = request.POST.get('HouseDetails')
        SquareFeet = request.POST.get('SquareFeet')
        PhoneNo = request.POST.get('PhoneNo')
        HouseImage = request.FILES.get('HouseImage')

        new_house = HousePost(
            Area=Area,
            Rent=Rent,
            HouseDetails=HouseDetails,
            SquareFeet=SquareFeet,
            PhoneNo=PhoneNo,
            HouseImage=HouseImage
        )
        new_house.save()

        return redirect('index')

    return render(request, "houseReg.html", {})

def index(request):
    blog = HousePost.objects.all()

    return render(request,"index.html",{"blogs" : blog })

def search_results(request):
    query = request.GET.get('query')
    results = HousePost.objects.filter(Area__icontains=query)
    # results = HousePost.objects.filter(Q(Rent__icontains=query) | Q(Rent__lt=query))
    context = {'results': results}
    return render(request, 'search_results.html', context)

def LogoutPage(request):
    logout(request)
    return redirect('login')



# if request.GET.get('sort_by'):
            # sort_by_value = request.GET.get('sort_by')
            # if sort_by_value == 'asc':
            #     blog= blog.order_by('Rent')
            # elif sort_by_value == 'dsc':
            #     blog = blog.order_by('-Rent')

            # if request.GET.get('amount'):
            #     amount = request.GET.get('Rent')
            #     blog = blog.filter(rent__lte=amount)
# def index(request):
    
#     return render(request,"index.html",{})

# def get_house(request):
#     try:
#         house_objs = HousePost.objects.all()

#         if request.GET.get('sort_by'):
#             sort_by_value = request.GET.get('sort_by')
#             if sort_by_value == 'asc':
#                 house_objs = house_objs.order_by('Rent')
#             elif sort_by_value == 'dsc':
#                 house_objs = house_objs.order_by('-Rent')

#         if request.GET.get('amount'):
#             amount = request.GET.get('amount')
#             house_objs = house_objs.filter(rent__lte=amount)

#         payload = []
#         for house_obj in house_objs:
#             payload.append({
#                 'house_image': '/media/Post/' + str(house_obj.HouseImage),
#                 'rent': house_obj.Rent,
#                 'area': house_obj.Area,
#                 'square_feet': house_obj.SquareFeet,
#                 'house_details': house_obj.HouseDetails,
#                 'phone_number': house_obj.PhoneNo,
#             })

#         return JsonResponse(payload, safe=False)

#     except Exception as e:
#         print(e)

#     return JsonResponse({'message': 'Something went wrong'})
#     # return redirect('home')
#     # return render(request,"index.html",{})

    

    

# def rental_advertisement_detail(request, pk):
#     # Get the rental advertisement object
#     rental_advertisement = RentalAdvertisement.objects.get(pk=pk)

#     # Render the rental advertisement detail HTML template with the rental advertisement object in the context
#     context = {'rental_advertisement': rental_advertisement}
#     return render(request, 'rental_advertisement.html', context)


