from django.shortcuts import render,redirect
from VFpages.models import UserTable,PagesTable,UserReviews,TeamName,Member,Destination,InternationalCity,InternationalAttraction,HomepageSlider,Category,CategoriesDestination,Lead,ContinentMetas,DestinationMeta
from VFpages.models import UserTable,PagesTable,UserReviews,TeamName,Member,Destination,InternationalCities,Packages
from VFpages.models import UserTable,PagesTable,UserReviews,BlogUs,FooterHeader,FooterTitle,Userdetails
from django.http import JsonResponse
from VFpages.models import Blog,BlogDetails
from django.http import JsonResponse
import shutil
from django.contrib.auth import logout
from datetime import datetime
from django.http import HttpResponse
from django.utils import timezone
import json
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from django.utils import timezone

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from VFpages.models import Tags
from VFpages.header_utils import adminheader


# Create your views here.
# Create your views here.
def login(request):
        return render(request, "admin/adminlogin.html")
def adminlogin(request):
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user_row = UserTable.objects.get(username=username, password=password)
        except UserTable.DoesNotExist:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
        
        # Retrieve the role associated with the user
        role = user_row.role
        
        # Store username and role in session
        request.session['username'] = username
        request.session['role'] = role
        request.session['password'] = password

        # Authentication successful, redirect to dashboard
        return redirect('Homepage_slider')

    # If request method is not POST, render the login page
    return render(request, 'admin/adminlogin.html')

    
# ----------------------------------------------insrt function--------------------------------------
def  about_us_update(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee' and role != 'data':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    about_page = PagesTable.objects.filter(pagesname='about_us').first()
    about_us_details = about_page.description.get('aboutus_details', {})
    return render(request, "admin/about_us_update.html", {'aboutus_admin': about_us_details,"userdetails":userdetails})

def about_us_new(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee'and role != 'data':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    about_page = PagesTable.objects.filter(pagesname='about_us').first()
    about_us_details = about_page.description.get('aboutus_details', {})
    update_time = datetime.now().strftime('%Y-%m-%d')
    username = request.session.get('username')
    if request.method == 'POST':
        about_us_details['subtitle'] = request.POST.get('Sub_Title')
        about_us_details['content_para_1'] = request.POST.get('content_para-1')
        about_us_details['content_para_2'] = request.POST.get('content_para-2')
        about_us_details['years_experiences'] = request.POST.get('Years_Experiences')
        about_us_details['meta_keyword'] = request.POST.get('meta_keyword')
        about_us_details['meta_description'] = request.POST.get('meta_description')
        about_us_details['meta_title'] = request.POST.get('meta_title')
        about_us_details['tour_packages'] = request.POST.get('Tour_Packages')
        about_us_details['happy_customers'] = request.POST.get('Happy_Customers')
        about_us_details['servicable_countries'] = request.POST.get('Servicable_Countries')
        about_page.updated_by =update_time
        # about_page.created_by =update_time
        # about_page.created_name =username
        about_page.updated_name =username

        if 'image-file' in request.FILES:
            old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/about_us_image/', about_us_details['image_file_path'])
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = request.FILES['image-file']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/about_us_image', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
            about_us_details['image_file_url'] = os.path.join('/image/about_us_image', img_path)
            about_us_details['image_file_path'] = img_path

            

        if 'image-file-2' in request.FILES:
            old_image_path2 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/about_us_image/', about_us_details['review_image_path'])
            if os.path.exists(old_image_path2):
                os.remove(old_image_path2)

            new_image2 = request.FILES['image-file-2']
            img_path2 = new_image2.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/about_us_image', img_path2)
            with open(image_path, 'wb') as destination:
                for chunk in new_image2.chunks():
                    destination.write(chunk)
            about_us_details['review_image_url'] = os.path.join('/image/about_us_image', img_path2)
            about_us_details['review_image_path'] = img_path2
            
        if 'Desktopimage-file' in request.FILES:
            old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/about_us_image/', about_us_details['Desktopimage_path'])
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = request.FILES['Desktopimage-file']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/about_us_image', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
            about_us_details['Desktopimage_url'] = os.path.join('/image/about_us_image', img_path)
            about_us_details['Desktopimage_path'] = img_path
        if 'Tabimage-file' in request.FILES:
            old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/about_us_image/', about_us_details['Tabimage_path'])
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = request.FILES['Tabimage-file']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/about_us_image', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
            about_us_details['Tabimage_url'] = os.path.join('/image/about_us_image', img_path)
            about_us_details['Tabimage_path'] = img_path

        if 'Mobileimage-file' in request.FILES:
            old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/about_us_image/', about_us_details['Mobileimage_path'])
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = request.FILES['Mobileimage-file']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/about_us_image', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
            about_us_details['Mobileimage_url'] = os.path.join('/image/about_us_image', img_path)
            about_us_details['Mobileimage_path'] = img_path


          

        about_page.save()
        return redirect('about_us_update')
    

# ------------------------------------------client review function----------------------------
def client_review_insert(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee'and role != 'data':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if request.method == 'POST':
        ClientName = request.POST.get('ClientName')
        Clientrating = request.POST.get('ClientRating')
        Client_content = request.POST.get('ClientReview')
        reviewlink = request.POST.get('reviewlink')
        Clientpackage = request.POST.get('Clientpackage')

        if 'ClientImages' in request.FILES:
            ClientImages = request.FILES['ClientImages']
            img_path = ClientImages.name
            # Save the uploaded file to your desired location
            ClientImagesimage_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/client_image', ClientImages.name)
            with open(ClientImagesimage_path, 'wb') as destination:
                for chunk in ClientImages.chunks():
                    destination.write(chunk)
            image_url_review = os.path.join('/image/client_image', ClientImages.name)
        else:
            image_url_review = None

        current_time = timezone.now()
        current_time_str = current_time.strftime("%Y-%m-%d %H:%M")
        description = {
            "ClientName": ClientName,
            "Clientrating": Clientrating,
            "Client_content": Client_content,
            # "image_url": image_url_review,
            "image_path":img_path,
            "curentdate": current_time_str,
            "reviewlink":reviewlink,
            "Clientpackage":Clientpackage,
        }
        user_review = UserReviews.objects.create(content=description)
        user_review.save()
        return redirect('about_us_review')
        
        
def client_review_update(request,id):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee'and role != 'data':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
        
    review = UserReviews.objects.get(id=id)
    reviews = review.content
    if request.method == 'POST':
        reviews["ClientName"] = request.POST.get('ClientName')
        reviews["Clientrating"] = request.POST.get('ClientRating')
        reviews["Client_content"] = request.POST.get('ClientReview')
        reviews["reviewlink"] = request.POST.get('reviewlink')
        reviews["Clientpackage"] = request.POST.get('Clientpackage')
        

        if 'ClientImages' in request.FILES:
            old_image_path2 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/client_image/', reviews['image_path'])
            if os.path.exists(old_image_path2):
                os.remove(old_image_path2)
                
            new_image = request.FILES['ClientImages']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/client_image', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
                    
            reviews['image_path'] = img_path
        else:
            image_url_review = None

        current_time = timezone.now()
        current_time_str = current_time.strftime("%Y-%m-%d %H:%M")
        reviews["curentdate"]=current_time_str
        review.save()
        return redirect('about_us_review')
    

def about_us_review(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee'and role != 'data':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    user_reviews_list = UserReviews.objects.all()
    all_content = []
    for user_review in user_reviews_list:
        review_data = {
            'id': user_review.id,
            'content': user_review.content
        }
        all_content.append(review_data)
    print(user_reviews_list)
    print(all_content)
    
    package_list = Packages.objects.all()
    return render(request, "admin/about_Us_review.html", {'user_reviews_list': all_content,"userdetails":userdetails,"package_list":package_list})

def delete_review(request, id):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee'and role != 'data':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if role == 'data':
        return redirect('about_us_review')
        
    review = UserReviews.objects.get(id=id)
    print("path verification",review.content.get('image_path'))
    if review.content.get('image_path'):
        image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/client_image/', review.content.get('image_path'))
        
        if os.path.exists(image_path):
            os.remove(image_path) 
    
    review.delete()
    return redirect('about_us_review')

#  -------------------------------------------add mteam name ---------------------------
def add_team(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee'and role != 'data':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if request.method == 'POST':
        Team_Name = request.POST.get('TeamName')
        team = TeamName.objects.create(Teamname=Team_Name)
        team.save()
        return redirect('add_view')
    else:
        return redirect('add_view')

def add_view(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    teams = TeamName.objects.all()
    return render(request, 'admin/Add_Team.html', {'form': teams,"userdetails":userdetails})

def edit_team(request, team_id):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    team = TeamName.objects.get(id=team_id)
    if request.method == 'POST':
        new_team_name = request.POST.get('TeamNamemodify')
        team.Teamname = new_team_name
        team.save()
        return redirect('add_view')
    return redirect('add_view')

# ---------------------------------- staff details memebers --------------------------------

   
def aboutUsTeam(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    teams = TeamName.objects.all()
    return render(request, "admin/add_member.html", {'Teams': teams,"userdetails":userdetails})

def aboutUsmemeber(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Role = request.POST.get('Role')
        Contact_Number = request.POST.get('Contact_Number')
        LinkedInid = request.POST.get('LinkedInid')
        team_name = request.POST.get('team-id')
        Ordernumber = request.POST.get('Ordernumber')
        
        # Saving the uploaded image
        imageurl = ''
        if 'MemeberImages' in request.FILES:
            Images = request.FILES['MemeberImages']
            img_path = Images.name
            Imagesimage_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Office_members', Images.name)
            with open(Imagesimage_path, 'wb') as destination:
                for chunk in Images.chunks():
                    destination.write(chunk)
            imageurl = os.path.join('/image/Office_members', Images.name)
        
        currenttime = timezone.now().strftime("%Y-%m-%d %H:%M")
        description = {
            "Name": Name,
            "Role": Role,
            "Contact_Number": Contact_Number,
            "LinkedInid": LinkedInid,
            "image_url": imageurl,
            "image_path": img_path,
            "team_id": team_name,
            "currentdate": currenttime,
            "Ordernumber": Ordernumber
        }
        # Creating and saving the Member object
        member = Member(role=Role, Team_Name=team_name, description=description)
        member.save()
        return redirect('aboutUsStaff')
    # return render(request, "admin/about_us_staff.html",{"userdetails":userdetails})

def aboutUsStaff(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    teams = Member.objects.all()
    all_content = []
    for user_review in teams:
        review_data = {
            'id': user_review.id,
            'content': user_review.description
        }
        all_content.append(review_data)
    print(all_content)
    print(teams)
    return render(request, "admin/about_us_staff.html",{'all_content':all_content,"userdetails":userdetails})
def updateMember(request,team_id):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    member = Member.objects.get(id=team_id)
    if request.method == 'POST':
        member.description['Name'] = request.POST.get('upadtename')
        member.description['Role'] = request.POST.get('upadteRole')
        member.role = request.POST.get('upadteRole')
        member.description['Contact_Number'] = request.POST.get('upadteContact_Number')
        member.description['LinkedInid'] = request.POST.get('upadteLinkedInid')
        member.description['Ordernumber'] = request.POST.get('upadteordernum')
        if 'upadteMemeberImages' in request.FILES:
            old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Office_members/', member.description['image_path'])
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = request.FILES['upadteMemeberImages']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Office_members', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
            member.description['image_url'] = os.path.join('/image/Office_members', img_path)
            member.description['image_path'] = new_image.name

        member.save()
        return redirect('aboutUsStaff')
    
def delete_Member(request, team_id):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if role == 'data':
        return redirect('aboutUsStaff')
    review = Member.objects.get(id=team_id)
    print("path verification",review.description.get('image_path'))
    if review.description.get('image_path'):
        image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Office_members/', review.description.get('image_path'))
        if os.path.exists(image_path):
            os.remove(image_path) 
    
    review.delete()
    return redirect('aboutUsStaff')

# -------------------------------------------destination details function -------------------------------------

def destination(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    all_destinations = Destination.objects.all()
    destinations_list = []
    for destination in all_destinations:
        destination_dict = {
            'id': destination.id,
            'category': destination.category,
            'destination_category': destination.destination_category,
            'destination_name': destination.destination_name,
            'destination_slug': destination.destination_slug,
            'destination_image': destination.destination_image.split("/")[-1],
            'destination_title': destination.destination_title,
            'destination_title_slug': destination.destination_title_slug,
            # 'destination_cost': destination.destination_cost,
            # 'destination_duration': destination.destination_duration,
            # 'destination_season': destination.destination_season,
            # 'destination_live_guide': destination.destination_live_guide,
            # 'destination_max_group': destination.destination_max_group,
            'created_at': destination.created_at,
            'updated_at': destination.updated_at,
            'canonical': destination.canonical,
            'metakeyword': destination.metakeyword,
            'metadestination': destination.metadestination,
            'metatitle': destination.metatitle,
            }
        destinations_list.append(destination_dict)
    print(destinations_list)
    
    search_query = request.GET.get('search_query')

    if search_query:
        filtered_attractions = [destination for destination in destinations_list if search_query.lower() in destination['destination_name'].lower() or search_query.lower() in destination['destination_category'].lower()]
        if not filtered_attractions:
            # Return a JSON response with a message indicating no attractions found
            return JsonResponse({'message': 'No destination found matching the search query'}, status=404)
        
        destinations_list = filtered_attractions
    

    paginator = Paginator(destinations_list,20)  # Show 5 blog entries per page

    page = request.GET.get('page')
    try:
        destinations_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        destinations_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        destinations_list = paginator.page(paginator.num_pages)

    return render(request, 'admin/destination/destinations.html',{'destination':destinations_list,"userdetails":userdetails,})

def des_insertfn(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    username = request.session.get('username')
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if request.method == 'POST':
        Category = request.POST.get('int-domes')
        des_Category = request.POST.get('Category')
        destination_name = request.POST.get('Name')
        destination_NameSlug = request.POST.get('NameSlug')
        destination_title = request.POST.get('Title')
        destination_title_slug = request.POST.get('TitleSlug')
        destination_MetaTitle = request.POST.get('MetaTitle')
        destination_Metadescription = request.POST.get('Metadescription')
        destination_Metakeyword = request.POST.get('Metakeyword')
        canonical = request.POST.get('canonical')
        # destination_cost = request.POST.get('cost')
        # destination_season = request.POST.get('Season')
        # destination_live_guide = request.POST.get('LiveGuide')
        # destination_max_group = request.POST.get('MaxGroup')
        # show_text = request.POST.get('Textonwebsite')

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if 'Baner_Images' in request.FILES:
            Images = request.FILES['Baner_Images']
            img_path = Images.name
            Imagesimage_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_image', Images.name)
            with open(Imagesimage_path, 'wb') as destination:
                for chunk in Images.chunks():
                    destination.write(chunk)
            # imageurl = os.path.join('/static/image/destination_image', Images.name)
        if 'Tab_Images' in request.FILES:
            Images = request.FILES['Tab_Images']
            img_path2 = Images.name
            Imagesimage_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_image', img_path2)
            with open(Imagesimage_path, 'wb') as destination:
                for chunk in Images.chunks():
                    destination.write(chunk)
        if 'Mobile_Images' in request.FILES:
            Images = request.FILES['Mobile_Images']
            img_path3 = Images.name
            Imagesimage_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_image', img_path3)
            with open(Imagesimage_path, 'wb') as destination:
                for chunk in Images.chunks():
                    destination.write(chunk)
        if 'Pathway_Image' in request.FILES:
            Images = request.FILES['Pathway_Image']
            img_path4 = Images.name
            Imagesimage_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_logo', img_path4)
            with open(Imagesimage_path, 'wb') as destination:
                for chunk in Images.chunks():
                    destination.write(chunk)

       
        new_destination = Destination(
            category=Category,
            destination_category=des_Category,
            destination_name=destination_name,
            destination_slug=destination_NameSlug,
            destination_image=img_path,
            destination_title=destination_title,
            destination_title_slug=destination_title_slug,
            metatitle=destination_MetaTitle,
            metadestination=destination_Metadescription,
            metakeyword=destination_Metakeyword,
            canonical=canonical,
            Tab_image=img_path2,
            pathimages=img_path4,
            mobile_image=img_path3,
            updated_name=username,
            created_name=username,
            # destination_duration=destination_duration,
            destination_season='',
            destination_live_guide='',
            destination_max_group='',
            destination_cost='',
            destination_duration='',
            # destination_season=destination_season,
            created_at=current_time,
            updated_at=current_time,
            show_text=0 
        )
        new_destination.save()
        return redirect('destination')
    return render(request, 'admin/destination/des_inset.html',{"userdetails":userdetails})

def destination_edit(request,team_id):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    username = request.session.get('username')
    destination = Destination.objects.get(id=team_id)
    if request.method == 'POST':
       
        update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        if 'up-Baner_Images' in request.FILES:
            if destination.destination_image :
                old_image = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_image/',destination.destination_image.split("/")[-1])
                print(" old image name",old_image)

                if os.path.exists(old_image):
                    os.remove(old_image)

            new_image = request.FILES['up-Baner_Images']
            up_img = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_image', up_img)
            print('new image',image_path)
            with open(image_path, 'wb') as destination_file:
                for chunk in new_image.chunks():
                    destination_file.write(chunk)
            # destination.destination_image['image_url'] = os.path.join('/image/destination/desti_image', up_img)
            destination.destination_image = up_img
        if 'up-Tab_Images' in request.FILES:
            if destination.Tab_image :
                old_image = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_image/',destination.Tab_image.split("/")[-1])
                print(" old image name",old_image)

                if os.path.exists(old_image):
                    os.remove(old_image)

            new_image = request.FILES['up-Tab_Images']
            up_img = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_image', up_img)
            print('new image',image_path)
            with open(image_path, 'wb') as destination_file:
                for chunk in new_image.chunks():
                    destination_file.write(chunk)
            # destination.destination_image['image_url'] = os.path.join('/image/destination/desti_image', up_img)
            destination.Tab_image = up_img
        if 'up-Mobile_Images' in request.FILES:
            if destination.mobile_image :
                old_image = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_image/',destination.mobile_image.split("/")[-1])
                print(" old image name",old_image)

                if os.path.exists(old_image):
                    os.remove(old_image)

            new_image = request.FILES['up-Mobile_Images']
            up_img = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_image', up_img)
            print('new image',image_path)
            with open(image_path, 'wb') as destination_file:
                for chunk in new_image.chunks():
                    destination_file.write(chunk)
            # destination.destination_image['image_url'] = os.path.join('/image/destination/desti_image', up_img)
            destination.mobile_image = up_img
        if 'up-Pathway_Image' in request.FILES:
            if destination.pathimages :
                old_image = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_logo/',destination.pathimages.split("/")[-1])
                print(" old image name",old_image)

                if os.path.exists(old_image):
                    os.remove(old_image)

            new_image = request.FILES['up-Pathway_Image']
            up_img = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_logo', up_img)
            print('new image',image_path)
            with open(image_path, 'wb') as destination_file:
                for chunk in new_image.chunks():
                    destination_file.write(chunk)
            # destination.destination_image['image_url'] = os.path.join('/image/destination/desti_image', up_img)
            destination.pathimages = up_img

        # Update the destination object with new values
        destination.category = request.POST.get('up-in-dom')
        destination.destination_category = request.POST.get('up-destination-Category')
        destination.destination_name = request.POST.get('up-Name')
        destination.destination_slug = request.POST.get('up-NameSlug')
        # destination.destination_image = image_url_new
        destination.destination_title = request.POST.get('up-Title')
        destination.destination_title_slug = request.POST.get('up-TitleSlug')
        destination.metatitle = request.POST.get('up-MetaTitle')
        destination.metadestination = request.POST.get('up-Metadescription')
        destination.metakeyword = request.POST.get('up-Metakeyword')
        # destination.destination_image = up_img
        destination.canonical = request.POST.get('canonical')
        
        # destination.destination_duration = request.POST.get('up-Duraion')
        # destination.destination_season = request.POST.get('up-Season')
        # destination.destination_live_guide = request.POST.get('up-LiveGuide')
        # destination.destination_max_group = request.POST.get('up-MaxGroup')
        destination.updated_at = update_time
        destination.updated_name = username
        # destination.show_text = request.POST.get('up-on-of')

        destination.save()

        return redirect('destination')

    return render(request, 'admin/destination/des_inset.html',{"userdetails":userdetails})

def destination_delete(request,team_id):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if role == 'data':
        return redirect('destination')
    destinations = Destination.objects.get(id=team_id)
    
    if destinations.destination_image:
        image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_image/', destinations.destination_image.split("/")[-1])
        if os.path.exists(image_path):
            os.remove(image_path)
    if destinations.Tab_image:
        image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_image/', destinations.Tab_image.split("/")[-1])
        if os.path.exists(image_path):
            os.remove(image_path)
    if destinations.mobile_image:
        image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_image/', destinations.mobile_image.split("/")[-1])
        if os.path.exists(image_path):
            os.remove(image_path)
    if destinations.pathimages:
        image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/desti_logo/', destinations.pathimages.split("/")[-1])
        if os.path.exists(image_path):
            os.remove(image_path)
    destinations.delete()
    return redirect('destination')


def destination_cities(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    Destnation = Destination.objects.all()

    all_des = []
    for destination in Destnation:
        all_des.append({"id":destination.id,"category":destination.category,"destination_name":destination.destination_name})

    Internation = []
    Domestic = []

    # Iterate over each destination and separate them based on their category
    for destination in all_des:
        if destination['category'] == '0':
            Internation.append(destination)
        elif destination['category'] == '1':
            Domestic.append(destination)
    
    Cities = InternationalCity.objects.all()
    City_list = []
    for City in Cities:
        City_list.append ({
            'id': City.id,
            'international_city_name': City.international_city_name,
            'updated_at': City.updated_at,
            "destination_name":City.destination_id,
            'city_slug':City.international_city_slug,
        })
        
    search_query = request.GET.get('search_query')

    if search_query:
        filtered_attractions = [attraction for attraction in City_list if search_query.lower() in attraction['international_city_name'].lower()]
        if not filtered_attractions:
            # Return a JSON response with a message indicating no attractions found
            return JsonResponse({'message': 'No attractions found matching the search query'}, status=404)
        
        City_list = filtered_attractions
    

    paginator = Paginator(City_list,20)  # Show 5 blog entries per page

    page = request.GET.get('page')
    try:
        City_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        City_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        City_list = paginator.page(paginator.num_pages)
    
    
    return render(request, 'admin/destination/destination_city.html',{'Internation':Internation,'Domestic':Domestic,'City_list':City_list,"userdetails":userdetails})

def add_destination_city(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if request.method == 'POST':
        DestinationName_id = request.POST.get('DestinationName')
        DestinationCityName = request.POST.get('DestinationCityName')
        DestinationCitySlug = request.POST.get('DestinationCitySlug')

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        city = InternationalCity(
            destination_id=DestinationName_id,
            international_city_name = DestinationCityName,
            international_city_slug = DestinationCitySlug,
            created_at=current_time, 
            updated_at=current_time,   
            )
        city.save()
        return redirect('destination_cities')
    return render(request, 'admin/destination/destination_city.html',{"userdetails":userdetails})

def edit_destination_city(request,team_id):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    Sepcific_city = InternationalCity.objects.get(id = team_id)
    if request.method == 'POST':
        update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        Sepcific_city.destination_id = request.POST.get('up-DestinationName')
        Sepcific_city.international_city_name = request.POST.get('up-DestinationCityName')
        Sepcific_city.international_city_slug = request.POST.get('up-DestinationCitySlug')
        Sepcific_city.updated_at = update_time

        Sepcific_city.save()

        return redirect('destination_cities')
    return render(request, 'admin/destination/destination_city.html',{"userdetails":userdetails})

def delete_destination_city(request,team_id):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if role == 'data':
        return redirect('destination_cities')
    del_city = InternationalCity.objects.get(id=team_id)
    del_city.delete()
    return redirect('destination_cities')
  

def destination_attraction(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    Attraction = InternationalAttraction.objects.all()
    list_attraction = []
    for Attraction_list in Attraction:
        list_attraction.append({
            'id': Attraction_list.id,
            "international_city_id":Attraction_list.international_city_id,
            "tour_spot_name":Attraction_list.tour_spot_name,
            "created_at":Attraction_list.created_at,
            "tour_spot_slug":Attraction_list.tour_spot_slug,
            "highlights_content":Attraction_list.highlights_content,
            "highlights_image":Attraction_list.highlights_image.split("/")[-1],
            "includes_content":Attraction_list.includes_content,
            "includes_image":Attraction_list.includes_image.split("/")[-1],

        })

    print(list_attraction)
    search_query = request.GET.get('search_query')

    if search_query:
        filtered_attractions = [attraction for attraction in list_attraction if search_query.lower() in attraction['tour_spot_name'].lower()]
        if not filtered_attractions:
            # Return a JSON response with a message indicating no attractions found
            return JsonResponse({'message': 'No attractions found matching the search query'}, status=404)
        
        list_attraction = filtered_attractions

    paginator = Paginator(list_attraction,55)  # Show 5 blog entries per page

    page = request.GET.get('page')
    try:
        list_attraction = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list_attraction = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list_attraction = paginator.page(paginator.num_pages)
    return render(request, 'admin/destination/des_attraction.html',{"attraction":list_attraction,"userdetails":userdetails})

def destination_attraction_insert(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    Cities = InternationalCity.objects.all()
    City_list = []
    for City in Cities:
        City_list.append ({
            'id': City.id,
            'international_city_name': City.international_city_name,
            
        })
    
    print(City_list)



    return render(request, 'admin/destination/des_attr_insert.html',{'City_list':City_list,"userdetails":userdetails})

def desti_add_deatils (request):

     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')

    if request.method == 'POST':
        TourSpotName = request.POST.get('TourSpotName')
        TourSpotslug = request.POST.get('TourSpotslug')
        City_name = request.POST.get('City_name')
        Highlights_Images = request.POST.get('Highlights_Images')
        Includes_Images = request.POST.get('Includes_Images')
        Highlight_text = request.POST.get('Highlights')
        Includes_test = request.POST.get('Includes')

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if 'Highlights_Images' in request.FILES:
            Images = request.FILES['Highlights_Images']
            img_path = Images.name
            Imagesimage_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/Attraction_image', img_path)
            with open(Imagesimage_path, 'wb') as destination:
                for chunk in Images.chunks():
                    destination.write(chunk)

        if 'Includes_Images' in request.FILES:
            Images = request.FILES['Includes_Images']
            img_path_2 = Images.name
            Imagesimage_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/Attraction_image', img_path_2)
            with open(Imagesimage_path, 'wb') as destination:
                for chunk in Images.chunks():
                    destination.write(chunk)

        

        Attraction = InternationalAttraction(
            international_city_id=City_name,
            tour_spot_name = TourSpotName,
            tour_spot_slug = TourSpotslug,
            highlights_content=Highlight_text,
            highlights_image= img_path,
            includes_content = Includes_test,
            includes_image = img_path_2,
            created_at=current_time, 
            updated_at=current_time,   
            )
        Attraction.save()

        return redirect('destination_attraction')

def  edit_attraction_page(request):

     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    attraction_id = request.GET.get('Cities')
    # all_city = InternationalCity.objects.filter(destination_id=continent)
    specific_attraction = InternationalAttraction.objects.get(id=attraction_id)
        # Format the retrieved attraction into a dictionary
    formatted_attraction = {
        'id': specific_attraction.id,
        'international_city_id': specific_attraction.international_city_id,
        'tour_spot_name': specific_attraction.tour_spot_name,
        'created_at': specific_attraction.created_at,
        'tour_spot_slug': specific_attraction.tour_spot_slug,
        'highlights_content': specific_attraction.highlights_content,
        'highlights_image': specific_attraction.highlights_image.split('/')[-1],
        'includes_content': specific_attraction.includes_content,
        'includes_image': specific_attraction.includes_image.split('/')[-1],
    }
    Cities = InternationalCity.objects.all()
    City_list = []
    for City in Cities:
        City_list.append ({
            'id': City.id,
            'international_city_name': City.international_city_name,
            
        })
    
    print(City_list)

    return render(request, "admin/destination/attraction_edit.html",{'attraction_deatils':formatted_attraction,'City_list':City_list,"userdetails":userdetails})
def attraction_edit(request):

     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')

    if request.method == 'POST':
        attraction_id = request.POST.get('id')
        
        try:
            attraction_id = int(attraction_id)
            attraction_place = InternationalAttraction.objects.get(id=attraction_id)
            
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if 'Highlights_Images' in request.FILES:
                # Process Highlights Image
                old_image = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/Attraction_image/', attraction_place.highlights_image.split('/')[-1])
                if os.path.exists(old_image):
                    os.remove(old_image)
                images = request.FILES['Highlights_Images']
                img_path = images.name
                images_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/Attraction_image', img_path)
                with open(images_image_path, 'wb') as destination:
                    for chunk in images.chunks():
                        destination.write(chunk)
                attraction_place.highlights_image = img_path

            if 'Includes_Images' in request.FILES:
                # Process Includes Image
                old_image = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/Attraction_image/', attraction_place.includes_image.split('/')[-1])
                if os.path.exists(old_image):
                    os.remove(old_image)
                images = request.FILES['Includes_Images']
                img_path_2 = images.name
                images_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/Attraction_image', img_path_2)
                with open(images_image_path, 'wb') as destination:
                    for chunk in images.chunks():
                        destination.write(chunk)
                attraction_place.includes_image = img_path_2

            # Update other fields
            attraction_place.tour_spot_name = request.POST.get('TourSpotName')
            attraction_place.tour_spot_slug = request.POST.get('TourSpotslug')
            attraction_place.international_city_id = request.POST.get('City_name')
            attraction_place.highlights_content = request.POST.get('Highlights')
            attraction_place.includes_content = request.POST.get('Includes')
            attraction_place.updated_at = current_time

            # Save the changes
            attraction_place.save()

        except (ValueError, InternationalAttraction.DoesNotExist):
            # Handle invalid or non-existing attraction ID
            return redirect('destination_attraction')  # or return an error response

    return redirect('destination_attraction')

def delete_attraction(request,team_id):

     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if role == 'data':
        return redirect('destination_attraction')

    destinations = InternationalAttraction.objects.get(id=team_id)
    
    if destinations.highlights_image:
        image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/Attraction_image/', destinations.highlights_image.split('/')[-1])
        if os.path.exists(image_path):
            os.remove(image_path)
    if destinations.includes_image:
        image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/destination/Attraction_image/', destinations.includes_image.split('/')[-1])
        if os.path.exists(image_path):
            os.remove(image_path)

    destinations.delete()

    return redirect('destination_attraction')


       
def dashboard(request):
    # Retrieve username and role from session
    userdetails = adminheader(request)
    print(userdetails)
    username = request.session.get('username')
    role = request.session.get('role')
    password = request.session.get('password')

    if not username or not role:
        # Redirect to login page if session data is not found
        return redirect('adminlogin')

    # Render dashboard with username and role
    return render(request, 'admin/dashboard.html', {"userdetails":userdetails})

def contact_us_admin(request):

    # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Get username from session
    username = request.session.get('username')

    # Check if the user has the appropriate role to access this page (optional)
    role = request.session.get('role')
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')

    # Check if the user's password matches the session data (optional)
    password = request.session.get('password')
    if not password:
        # Redirect to login page if password is not found in session
        return redirect('adminlogin')
    
    # Your existing code for retrieving and formatting data from PagesTable
    userdetails = adminheader(request)
    contact_us_page = PagesTable.objects.filter(pagesname='contact us').first()
    datedata = contact_us_page.description
    created_by = contact_us_page.created_by
    updated_by = contact_us_page.updated_by
    # time = datedata['updated_time']
    # timestamp_format = '%Y-%m-%dT%H:%M:%S.%f%z'
    # timestamp_dt = datetime.strptime(time, timestamp_format)
    # normal_format = timestamp_dt.strftime('%Y-%m-%d')
    
    return render(request, "admin/contact_us.html", {'datedata': datedata,"userdetails":userdetails,"created_by":created_by,"updated_by":updated_by})
    
    

def submit_form_contact(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    username = request.session.get('username')
    role = request.session.get('role')
    contact_us = PagesTable.objects.filter(pagesname='contact us').first()
    contact_us_details = contact_us.description
    update_time = datetime.now().strftime('%Y-%m-%d')
    if request.method == 'POST':
        contact_us_details['meta_title'] = request.POST.get('title')
        contact_us_details['meta_description'] = request.POST.get('description')
        contact_us_details['meta_keyword'] = request.POST.get('keyword')
       
        # contact_us.created_by = update_time
        contact_us.updated_by = update_time
        # contact_us.created_name = username
        contact_us.updated_name = username

        if 'Desktopimage' in request.FILES:
            old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home/', contact_us_details['Desktopimage_path'])
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = request.FILES['Desktopimage']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
            contact_us_details['Desktopimage_url'] = os.path.join('/image/home', img_path)
            contact_us_details['Desktopimage_path'] = img_path
        if 'Tabimage' in request.FILES:
            old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home/', contact_us_details['Tabimage_path'])
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = request.FILES['Tabimage']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
            contact_us_details['Tabimage_url'] = os.path.join('/image/home', img_path)
            contact_us_details['Tabimage_path'] = img_path

        if 'Mobileimage' in request.FILES:
            old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home/', contact_us_details['Mobileimage_path'])
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = request.FILES['Mobileimage']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
            contact_us_details['Mobileimage_url'] = os.path.join('/image/home', img_path)
            contact_us_details['Mobileimage_path'] = img_path

        contact_us.save()
    
        return redirect('contact_us_admin')  # Redirect to a success page

    return render(request, "admin/about_us_update.html")

def adminlogout(request):
    # Clear session data
    request.session.clear()
    
    # Logout the user
    logout(request)
    
    # Redirect to the login page
    return redirect('login')

def blog_us_admin(request):
    # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    userdetails = adminheader(request)
    search_query = request.GET.get('search_query')
    countpopular = request.GET.get('count')
    blog_entries = Blog.objects.all().order_by('-id')
    tags = Tags.objects.all()


    blog_us_page = PagesTable.objects.filter(pagesname='blog_us').first()
    count_false_popular = Blog.objects.filter(popular=False).count()
    datedata = blog_us_page.description
    created_by = blog_us_page.created_by
    updated_by = blog_us_page.updated_by
    all_blog_us_instances = Blog.objects.all()

    # Iterate over each instance and access its hidden attribute
    hidden = Blog.hidden
    popular = Blog.popular

    # Now hidden_values contains the values of the hidden field for all instances
    print(hidden)
    
    

    if search_query:
        blog_entries = blog_entries.filter(description__title__icontains=search_query)

    paginator = Paginator(blog_entries, 5)  # Show 5 blog entries per page
    
    if countpopular:
        blog_entries = Blog.objects.filter(popular=False)
        count_false_popular = Blog.objects.filter(popular=False).count()
        paginator = Paginator(blog_entries, count_false_popular)

    page = request.GET.get('page')
    try:
        blog_entries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blog_entries = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blog_entries = paginator.page(paginator.num_pages)
    return render(request, "admin/blog_us_adminpanel.html" , {"page":page,'tags':tags,'blog_entries': blog_entries,'datedata': datedata,"userdetails":userdetails,"popular":popular,"hidden":hidden,"created_by":created_by,"updated_by":updated_by,"count_false_popular":count_false_popular})

def addblogs(request):
    # Check authentication and role
    # Check authentication and role
    username = request.session.get('username')
    role = request.session.get('role')

    if not username or not role:
        return redirect('login')

    if role != 'admin' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    
    blog_entry_id = None
    description = None

    if request.method == 'POST':
        blog_entry_id = request.POST.get('id','')
        try:
            # Get the BlogUs instance with the provided ID
            blog_entry = Blog.objects.get(id=blog_entry_id)
            description = blog_entry.description
            existing_url = blog_entry.url
            existing_created_by = blog_entry.created_by
            existing_updated_by = blog_entry.updated_by
            print(description)
            if request.method == 'POST':
                # Retrieve existing values
                existing_tags = description.get('tags', '')
                existing_banner_image_url = description.get('banner_image_url', None)
                existing_MobileBanner_Image_url = description.get('MobileBanner_Image_url', None)
                existing_TabBanner_Image_url = description.get('TabBanner_Image_url', None)
                existing_grid_image_url = description.get('grid_image_url', None)
                existing_cover_image_url = description.get('cover_image_url', None)
                existing_banner_image_path = description.get('banner_image_path', None)
                existing_TabBanner_Image_path = description.get('TabBanner_Image_path', None)
                existing_MobileBanner_Image_path = description.get('MobileBanner_Image_path', None)
                existing_grid_image_path = description.get('grid_image_path', None)
                existing_cover_image_path = description.get('cover_image_path', None)
                # existing_tagsid = request.description('tagsid',None)
                existing_banner_image = description.get('banner_image', None)
                existing_TabBanner_Image = description.get('TabBanner_Image', None)
                existing_MobileBanner_Image = description.get('MobileBanner_Image', None)
                existing_cover_image = description.get('cover_image', None)
                existing_grid_image = description.get('grid_image', None)
                
                hint = request.POST.get('hint')
                category = request.POST.get('category')
                new_tags = request.POST.get('tags')
                author = request.POST.get('author')
                new_url = request.POST.get('url')
                Canonical = request.POST.get('Canonical')
                title = request.POST.get('title')
                descriptions = request.POST.get('description')
                content = request.POST.get('content')
                jump_link_titles = request.POST.get('jumpLinkTitles')
                meta_title = request.POST.get('metaTitle')
                meta_description = request.POST.get('metaDescription')
                meta_keywords = request.POST.get('metaKeywords')

                richtextarea1 = request.POST.get('richtextarea1')
                richtextarea2 = request.POST.get('richtextarea2')
                richtextarea3 = request.POST.get('richtextarea3')
                richtextarea4 = request.POST.get('richtextarea4')
                richtextarea5 = request.POST.get('richtextarea5')
                richtextarea6 = request.POST.get('richtextarea6')
                richtextarea7 = request.POST.get('richtextarea7')
                richtextarea8 = request.POST.get('richtextarea8')
                richtextarea9 = request.POST.get('richtextarea9')
                richtextarea10 = request.POST.get('richtextarea10')
                
                tagsid = request.POST.get('tagsid')
                date = datetime.now().strftime('%Y-%m-%d')
                description = {
                    "hint": hint,
                    "category": category,
                    "author": author,
                    "url": new_url,
                    "title": title,
                    "content": content,
                    "description":descriptions,
                    "jump_link_titles": jump_link_titles,
                    "meta_title": meta_title,
                    "meta_description": meta_description,
                    "meta_keywords": meta_keywords,

                    "banner_image_url": existing_banner_image_url,
                    "banner_image_path": existing_banner_image_path,
                    "banner_image":existing_banner_image,

                    "MobileBanner_Image_url": existing_MobileBanner_Image_url,
                    "MobileBanner_Image_path": existing_MobileBanner_Image_path,
                    "MobileBanner_Image":existing_MobileBanner_Image,

                    "TabBanner_Image_url": existing_TabBanner_Image_url,
                    "TabBanner_Image_path": existing_TabBanner_Image_path,
                    "TabBanner_Image":existing_TabBanner_Image,

                    "cover_image_url": existing_cover_image_url,
                    "cover_image_path": existing_cover_image_path,
                    "cover_image":existing_cover_image,
                    "grid_image_url": existing_grid_image_url,
                    "grid_image_path": existing_grid_image_path,
                    "grid_image":existing_grid_image,
                    "tags":existing_tags
                }

                if new_tags:
                    description['tags'] = new_tags

                if new_url:
                    blog_entry.url = new_url
                else:
                    blog_entry.url = existing_url


                blog_entry_folder = str(blog_entry.id)
                banner_image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder)
                TabBanner_Image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder)
                MobileBanner_Image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder)

                cover_image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder)
                grid_image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder)

                if 'Banner_Image' in request.FILES:
                    blog_entry_folder = str(blog_entry.id)
                    if existing_banner_image:
                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder,existing_banner_image)
                        if os.path.exists(old_image_path):
                            os.remove(old_image_path)
                    
                    if not os.path.exists(banner_image_folder):
                        os.makedirs(banner_image_folder)
                    new_image = request.FILES['Banner_Image']
                    img_path = new_image.name
                    image_path = os.path.join(settings.BASE_DIR,'VFpages/static/image/blog_image', blog_entry_folder, img_path)
                    with open(image_path, 'wb') as destination:
                        for chunk in new_image.chunks():
                            destination.write(chunk)
                    banner_image_url_first = os.path.join('/image/blog_image', blog_entry_folder, img_path)
                    banner_image_url_final = banner_image_url_first.replace("\\", "/")
                    description['banner_image_url'] = banner_image_url_final
                    description['banner_image'] = img_path
                if 'TabBanner_Image' in request.FILES:
                    blog_entry_folder = str(blog_entry.id)
                    if existing_TabBanner_Image:
                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder,existing_TabBanner_Image)
                        if os.path.exists(old_image_path):
                            os.remove(old_image_path)
                    
                    if not os.path.exists(TabBanner_Image_folder):
                        os.makedirs(TabBanner_Image_folder)
                    new_image = request.FILES['TabBanner_Image']
                    img_path = new_image.name
                    image_path = os.path.join(settings.BASE_DIR,'VFpages/static/image/blog_image', blog_entry_folder, img_path)
                    with open(image_path, 'wb') as destination:
                        for chunk in new_image.chunks():
                            destination.write(chunk)
                    banner_image_url_first = os.path.join('/image/blog_image', blog_entry_folder, img_path)
                    banner_image_url_final = banner_image_url_first.replace("\\", "/")
                    description['TabBanner_Image_url'] = banner_image_url_final
                    description['TabBanner_Image'] = img_path
                if 'MobileBanner_Image' in request.FILES:
                    blog_entry_folder = str(blog_entry.id)
                    if existing_MobileBanner_Image :
                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder,existing_MobileBanner_Image)
                        if os.path.exists(old_image_path):
                            os.remove(old_image_path)
                    
                    if not os.path.exists(MobileBanner_Image_folder):
                        os.makedirs(MobileBanner_Image_folder)
                    new_image = request.FILES['MobileBanner_Image']
                    img_path = new_image.name
                    image_path = os.path.join(settings.BASE_DIR,'VFpages/static/image/blog_image', blog_entry_folder, img_path)
                    with open(image_path, 'wb') as destination:
                        for chunk in new_image.chunks():
                            destination.write(chunk)
                    banner_image_url_first = os.path.join('/image/blog_image', blog_entry_folder, img_path)
                    banner_image_url_final = banner_image_url_first.replace("\\", "/")
                    description['MobileBanner_Image_url'] = banner_image_url_final
                    description['MobileBanner_Image'] = img_path
                
                if 'Grid_Image' in request.FILES:
                    blog_entry_folder = str(blog_entry.id)
                    if existing_grid_image:
                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder , existing_grid_image)
                        if os.path.exists(old_image_path):
                            os.remove(old_image_path)
                    
                    if not os.path.exists(grid_image_folder):
                        os.makedirs(grid_image_folder)
                    new_image = request.FILES['Grid_Image']
                    img_path = new_image.name
                    image_path = os.path.join(settings.BASE_DIR,'VFpages/static/image/blog_image', blog_entry_folder, img_path)
                    with open(image_path, 'wb') as destination:
                        for chunk in new_image.chunks():
                            destination.write(chunk)
                    description['grid_image_url'] = os.path.join('/image/blog_image', blog_entry_folder, img_path)
                    description['grid_image'] = img_path

                if 'Cover_Image' in request.FILES:
                    blog_entry_folder = str(blog_entry.id)
                    if existing_cover_image:
                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder,existing_cover_image)
                        if os.path.exists(old_image_path):
                            os.remove(old_image_path)
                            
                    if not os.path.exists(cover_image_folder):
                        os.makedirs(cover_image_folder)
                    new_image = request.FILES['Cover_Image']
                    img_path = new_image.name
                    image_path = os.path.join(settings.BASE_DIR,'VFpages/static/image/blog_image', blog_entry_folder, img_path)
                    with open(image_path, 'wb') as destination:
                        for chunk in new_image.chunks():
                            destination.write(chunk)
                    description['cover_image_url'] = os.path.join('/image/blog_image', blog_entry_folder, img_path)
                    description['cover_image'] = img_path

                # ----------------------- blog details -------------
                
                blog_details = BlogDetails.objects.filter(blog_id=blog_entry_folder)

                # Check if there are at least two BlogDetails objects with the same blog_id
                if 10 >=10:
                    for index, blog_detail in enumerate(blog_details):
                        if index == 0:  # Update first row
                            if richtextarea1:
                                blog_entry_folder = str(blog_entry.id)
                                banner_image_folder1 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder)
                                if 'blogImage1' in request.FILES:
                                    if blog_detail.image_path:
                                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, blog_detail.image_path)
                                        if os.path.exists(old_image_path):
                                            os.remove(old_image_path)
    
                                    if not os.path.exists(banner_image_folder1):
                                        os.makedirs(banner_image_folder1)
                                    new_image = request.FILES['blogImage1']
                                    img_path = new_image.name
                                    image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, img_path)
                                    with open(image_path, 'wb') as destination:
                                        for chunk in new_image.chunks():
                                            destination.write(chunk)
                                    blog_detail.image_path = img_path

                                blog_detail.blog_description = richtextarea1
                                blog_detail.title = request.POST.get('title1')
                                blog_detail.updated_by = date
                                blog_detail.updated_name = username
                                blog_detail.save()
                        elif index == 1:  # Update second row
                            if richtextarea2:
                                blog_entry_folder = str(blog_entry.id)
                                banner_image_folder2 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder)
                                if 'blogImage2' in request.FILES:
                                    if blog_detail.image_path:
                                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, blog_detail.image_path)
                                        if os.path.exists(old_image_path):
                                            os.remove(old_image_path)

                                    if not os.path.exists(banner_image_folder2):
                                        os.makedirs(banner_image_folder2)
                                    new_image = request.FILES['blogImage2']
                                    img_path = new_image.name
                                    image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, img_path)
                                    with open(image_path, 'wb') as destination:
                                        for chunk in new_image.chunks():
                                            destination.write(chunk)
                                    blog_detail.image_path = img_path

                                blog_detail.blog_description = richtextarea2
                                blog_detail.title = request.POST.get('title2')
                                blog_detail.updated_by = date
                                blog_detail.updated_name = username
                                blog_detail.save()
                        elif index == 2:  # Update second row
                            if richtextarea3:
                                blog_entry_folder = str(blog_entry.id)
                                banner_image_folder3 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder)
                                if 'blogImage3' in request.FILES:
                                    if blog_detail.image_path:
                                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, blog_detail.image_path)
                                        if os.path.exists(old_image_path):
                                            os.remove(old_image_path)

                                    if not os.path.exists(banner_image_folder3):
                                        os.makedirs(banner_image_folder3)
                                    new_image = request.FILES['blogImage3']
                                    img_path = new_image.name
                                    image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, img_path)
                                    with open(image_path, 'wb') as destination:
                                        for chunk in new_image.chunks():
                                            destination.write(chunk)
                                    blog_detail.image_path = img_path

                                blog_detail.blog_description = richtextarea3
                                blog_detail.title = request.POST.get('title3')
                                blog_detail.updated_by = date
                                blog_detail.updated_name = username
                                blog_detail.save()
                        elif index == 3:  # Update second row
                            if richtextarea4:
                                blog_entry_folder = str(blog_entry.id)
                                banner_image_folder4 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder)
                                if 'blogImage4' in request.FILES:
                                    if blog_detail.image_path:
                                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, blog_detail.image_path)
                                        if os.path.exists(old_image_path):
                                            os.remove(old_image_path)

                                    if not os.path.exists(banner_image_folder4):
                                        os.makedirs(banner_image_folder4)
                                    new_image = request.FILES['blogImage4']
                                    img_path = new_image.name
                                    image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, img_path)
                                    with open(image_path, 'wb') as destination:
                                        for chunk in new_image.chunks():
                                            destination.write(chunk)
                                    blog_detail.image_path = img_path

                                blog_detail.blog_description = richtextarea4
                                blog_detail.title = request.POST.get('title4')
                                blog_detail.updated_by = date
                                blog_detail.updated_name = username
                                blog_detail.save()
                        elif index == 4:  # Update second row
                            if richtextarea5:
                                blog_entry_folder = str(blog_entry.id)
                                banner_image_folder5 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder)
                                if 'blogImage5' in request.FILES:
                                    if blog_detail.image_path:
                                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, blog_detail.image_path)
                                        if os.path.exists(old_image_path):
                                            os.remove(old_image_path)

                                    if not os.path.exists(banner_image_folder5):
                                        os.makedirs(banner_image_folder5)
                                    new_image = request.FILES['blogImage5']
                                    img_path = new_image.name
                                    image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, img_path)
                                    with open(image_path, 'wb') as destination:
                                        for chunk in new_image.chunks():
                                            destination.write(chunk)
                                    blog_detail.image_path = img_path

                                blog_detail.blog_description = richtextarea5
                                blog_detail.title = request.POST.get('title5')
                                blog_detail.updated_by = date
                                blog_detail.updated_name = username
                                blog_detail.save()
                        elif index == 5:  # Update second row
                            if richtextarea6:
                                blog_entry_folder = str(blog_entry.id)
                                banner_image_folder6 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder)
                                if 'blogImage6' in request.FILES:
                                    if blog_detail.image_path:
                                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, blog_detail.image_path)
                                        if os.path.exists(old_image_path):
                                            os.remove(old_image_path)

                                    if not os.path.exists(banner_image_folder6):
                                        os.makedirs(banner_image_folder6)
                                    new_image = request.FILES['blogImage6']
                                    img_path = new_image.name
                                    image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, img_path)
                                    with open(image_path, 'wb') as destination:
                                        for chunk in new_image.chunks():
                                            destination.write(chunk)
                                    blog_detail.image_path = img_path

                                blog_detail.blog_description = richtextarea6
                                blog_detail.title = request.POST.get('title6')
                                blog_detail.updated_by = date
                                blog_detail.updated_name = username
                                blog_detail.save()
                        elif index == 6:  # Update second row
                            if richtextarea7:
                                blog_entry_folder = str(blog_entry.id)
                                banner_image_folder7 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder)
                                if 'blogImage7' in request.FILES:
                                    if blog_detail.image_path:
                                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, blog_detail.image_path)
                                        if os.path.exists(old_image_path):
                                            os.remove(old_image_path)

                                    if not os.path.exists(banner_image_folder7):
                                        os.makedirs(banner_image_folder7)
                                    new_image = request.FILES['blogImage7']
                                    img_path = new_image.name
                                    image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, img_path)
                                    with open(image_path, 'wb') as destination:
                                        for chunk in new_image.chunks():
                                            destination.write(chunk)
                                    blog_detail.image_path = img_path

                                blog_detail.blog_description = richtextarea7
                                blog_detail.title = request.POST.get('title7')
                                blog_detail.updated_by = date
                                blog_detail.updated_name = username
                                blog_detail.save()
                        elif index == 7:  # Update second row
                            if richtextarea8:
                                blog_entry_folder = str(blog_entry.id)
                                banner_image_folder8 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder)
                                if 'blogImage8' in request.FILES:
                                    if blog_detail.image_path:
                                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, blog_detail.image_path)
                                        if os.path.exists(old_image_path):
                                            os.remove(old_image_path)

                                    if not os.path.exists(banner_image_folder8):
                                        os.makedirs(banner_image_folder8)
                                    new_image = request.FILES['blogImage8']
                                    img_path = new_image.name
                                    image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, img_path)
                                    with open(image_path, 'wb') as destination:
                                        for chunk in new_image.chunks():
                                            destination.write(chunk)
                                    blog_detail.image_path = img_path

                                blog_detail.blog_description = richtextarea8
                                blog_detail.title = request.POST.get('title8')
                                blog_detail.updated_by = date
                                blog_detail.updated_name = username
                                blog_detail.save()
                        elif index == 8:  # Update second row
                            if richtextarea9:
                                blog_entry_folder = str(blog_entry.id)
                                banner_image_folder9 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder)
                                if 'blogImage9' in request.FILES:
                                    if blog_detail.image_path:
                                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, blog_detail.image_path)
                                        if os.path.exists(old_image_path):
                                            os.remove(old_image_path)

                                    if not os.path.exists(banner_image_folder9):
                                        os.makedirs(banner_image_folder9)
                                    new_image = request.FILES['blogImage9']
                                    img_path = new_image.name
                                    image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, img_path)
                                    with open(image_path, 'wb') as destination:
                                        for chunk in new_image.chunks():
                                            destination.write(chunk)
                                    blog_detail.image_path = img_path
                                    
                                blog_detail.blog_description = richtextarea9
                                blog_detail.title = request.POST.get('title9')
                                blog_detail.updated_by = date
                                blog_detail.updated_name = username
                                blog_detail.save()
                        elif index == 9:  # Update second row
                            if richtextarea10:
                                blog_entry_folder = str(blog_entry.id)
                                banner_image_folder10 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder)
                                if 'blogImage10' in request.FILES:
                                    if blog_detail.image_path:
                                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, blog_detail.image_path)
                                        if os.path.exists(old_image_path):
                                            os.remove(old_image_path)

                                    if not os.path.exists(banner_image_folder10):
                                        os.makedirs(banner_image_folder10)
                                    new_image = request.FILES['blogImage10']
                                    img_path = new_image.name
                                    image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder, img_path)
                                    with open(image_path, 'wb') as destination:
                                        for chunk in new_image.chunks():
                                            destination.write(chunk)
                                    blog_detail.image_path = img_path
                                    
                                blog_detail.blog_description = richtextarea10
                                blog_detail.title = request.POST.get('title10')
                                blog_detail.updated_by = date
                                blog_detail.updated_name = username
                                blog_detail.save()
                                
                # Update 'updated_by' key
                username = request.session.get('username')
                current_time = timezone.now().strftime("%d-%m-%Y")
               


                # Update BlogUs instance with the modified description
                # blog_entry.created_by = f"{username} {current_time}"
                blog_entry.updated_by =  date
                blog_entry.updated_name = username
                blog_entry.tags = tagsid
                blog_entry.canonical = Canonical
                blog_entry.description = description
                print(blog_entry.description )
                blog_entry.save()
                return redirect('blog_us_admin') 
        except Blog.DoesNotExist:
            return HttpResponse('Blog entry with the provided ID does not exist') # Redirect to success page
        
    userdetails = adminheader(request)

    return render(request, "admin/updateblogentry.html", {'blog_entry_id': blog_entry_id, 'description': description,"userdetails":userdetails})

def createblogs(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.session.get('username')
        hint = request.POST.get('hint')
        category = request.POST.get('category')
        tags = request.POST.get('tags')
        author = request.POST.get('author')
        url = request.POST.get('url')
        title = request.POST.get('title')
        descriptions = request.POST.get('description')
        content = request.POST.get('content')
        jump_link_titles = request.POST.get('jumpLinkTitles')
        meta_title = request.POST.get('metaTitle')
        meta_description = request.POST.get('metaDescription')
        meta_keywords = request.POST.get('metaKeywords')
        tagsid = request.POST.get('tagsid')
        Canonical = request.POST.get('Canonical')

        richtextarea1 = request.POST.get('richtextarea1')
        richtextarea2 = request.POST.get('richtextarea2')
        richtextarea3 = request.POST.get('richtextarea3')
        richtextarea4 = request.POST.get('richtextarea4')
        richtextarea5 = request.POST.get('richtextarea5')
        richtextarea6 = request.POST.get('richtextarea6')
        richtextarea7 = request.POST.get('richtextarea7')
        richtextarea8 = request.POST.get('richtextarea8')
        richtextarea9 = request.POST.get('richtextarea9')
        richtextarea10 = request.POST.get('richtextarea10')
        
        # Create an instance of BlogUs model
        blog_entry = Blog.objects.create()
        # Blog_Details = BlogDetails.objects.create()
        blog_entry_folder = str(blog_entry.id)
        date = datetime.now().strftime('%Y-%m-%d')
        
        # Generate folder names based on the ID of the created blog entry
        
        banner_image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder )
        TabBanner_Image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder)
        MobileBanner_Image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder)

        cover_image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder)
        grid_image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder)

        if 'Banner_Image' in request.FILES:
            banner_image_file = request.FILES['Banner_Image']
            banner_image = banner_image_file.name
            if not os.path.exists(banner_image_folder):
                os.makedirs(banner_image_folder)
            banner_image_path = os.path.join(banner_image_folder, banner_image_file.name)
            with open(banner_image_path, 'wb') as destination:
                for chunk in banner_image_file.chunks():
                    destination.write(chunk)
            banner_image_url_first = os.path.join('/image/blog_image', blog_entry_folder, banner_image_file.name)
            banner_image_url_second = banner_image_url_first.replace("\\", "/")
            banner_image_url = banner_image_url_second 

        else:
            banner_image_url = None
            banner_image_path = None
            banner_image = None

        if 'TabBanner_Image' in request.FILES:
            TabBanner_Image_file = request.FILES['TabBanner_Image']
            TabBanner_Image = TabBanner_Image_file.name
            if not os.path.exists(TabBanner_Image_folder):
                os.makedirs(TabBanner_Image_folder)
            TabBanner_Image_path = os.path.join(TabBanner_Image_folder, TabBanner_Image_file.name)
            with open(TabBanner_Image_path, 'wb') as destination:
                for chunk in TabBanner_Image_file.chunks():
                    destination.write(chunk)
            TabBanner_Image_url_first = os.path.join('/image/blog_image', blog_entry_folder, TabBanner_Image_file.name)
            TabBanner_Image_url_second = TabBanner_Image_url_first.replace("\\", "/")
            TabBanner_Image_url = TabBanner_Image_url_second 

        else:
            TabBanner_Image_url = None
            TabBanner_Image_path = None
            TabBanner_Image = None

        if 'MobileBanner_Image' in request.FILES:
            MobileBanner_Image_file = request.FILES['MobileBanner_Image']
            MobileBanner_Image = MobileBanner_Image_file.name
            if not os.path.exists(MobileBanner_Image_folder):
                os.makedirs(MobileBanner_Image_folder)
            MobileBanner_Image_path = os.path.join(MobileBanner_Image_folder, MobileBanner_Image_file.name)
            with open(MobileBanner_Image_path, 'wb') as destination:
                for chunk in MobileBanner_Image_file.chunks():
                    destination.write(chunk)
            MobileBanner_Image_url_first = os.path.join('/image/blog_image', blog_entry_folder, MobileBanner_Image_file.name)
            MobileBanner_Image_url_second = MobileBanner_Image_url_first.replace("\\", "/")
            MobileBanner_Image_url = MobileBanner_Image_url_second 

        else:
            MobileBanner_Image_url = None
            MobileBanner_Image_path = None
            MobileBanner_Image = None

        if 'Cover_Image' in request.FILES:
            cover_image_file = request.FILES['Cover_Image']
            cover_image = cover_image_file.name
            if not os.path.exists(cover_image_folder):
                os.makedirs(cover_image_folder)
            cover_image_path = os.path.join(cover_image_folder, cover_image_file.name)
            with open(cover_image_path, 'wb') as destination:
                for chunk in cover_image_file.chunks():
                    destination.write(chunk)
            cover_image_url = os.path.join('/image/blog_image', blog_entry_folder, cover_image_file.name)
        else:
            cover_image_url = None
            cover_image_path = None
            cover_image = None
        
        if 'Grid_Image' in request.FILES:
            grid_image_file = request.FILES['Grid_Image']
            grid_image = grid_image_file.name
            if not os.path.exists(grid_image_folder):
                os.makedirs(grid_image_folder)
            grid_image_path = os.path.join(grid_image_folder, grid_image_file.name)
            with open(grid_image_path, 'wb') as destination:
                for chunk in grid_image_file.chunks():
                    destination.write(chunk)
            grid_image_url = os.path.join('/image/blog_image', blog_entry_folder, grid_image_file.name)
        else:
            grid_image_url = None
            grid_image_path = None
            grid_image = None

        # --------------------- blog details ------------------------
        
        banner_image_folder1 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder )
        banner_image_folder2 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder )
        banner_image_folder3 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder )
        banner_image_folder4 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder )
        banner_image_folder5 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder )
        banner_image_folder6 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder )
        banner_image_folder7 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder )
        banner_image_folder8 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder )
        banner_image_folder9 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder )
        banner_image_folder10 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder )

        if richtextarea1:
            if 'blogImage1' in request.FILES:
                blogImage1_file = request.FILES['blogImage1']
                blogImage1 = blogImage1_file.name
                if not os.path.exists(banner_image_folder1):
                    os.makedirs(banner_image_folder1)
                blogImage1_path = os.path.join(banner_image_folder1, blogImage1_file.name)
                with open(blogImage1_path, 'wb') as destination:
                    for chunk in blogImage1_file.chunks():
                        destination.write(chunk)
            else:
                blogImage1 = None
            
                # Assuming Blog_Details has fields to store image details
            blog_detail_obj = BlogDetails(
                blog_description=richtextarea1,  # Assuming you have retrieved richtextarea earlier
                blog_id=blog_entry.id,
                image_path=blogImage1,
                created_by = date,
                updated_by = date,
                created_name = username,
                updated_name =username,
                title = request.POST.get('title1'),
            )
            blog_detail_obj.save()
        if richtextarea2:
            if 'blogImage2' in request.FILES:
                blogImage2_file = request.FILES['blogImage2']
                blogImage2 = blogImage2_file.name
                if not os.path.exists(banner_image_folder2):
                    os.makedirs(banner_image_folder2)
                blogImage2_path = os.path.join(banner_image_folder2, blogImage2_file.name)
                with open(blogImage2_path, 'wb') as destination:
                    for chunk in blogImage2_file.chunks():
                        destination.write(chunk)
            else:
                blogImage2 = None
            
            blog_detail_obj = BlogDetails(
                blog_description=richtextarea2,  # Assuming you have retrieved richtextarea earlier
                blog_id=blog_entry_folder,
                image_path=blogImage2,
                created_by = date,
                updated_by = date,
                created_name = username,
                updated_name =username,
                title = request.POST.get('title2'),
            )
            blog_detail_obj.save()
        if richtextarea3:
            if 'blogImage3' in request.FILES:
                blogImage3_file = request.FILES['blogImage3']
                blogImage3 = blogImage3_file.name
                if not os.path.exists(banner_image_folder3):
                    os.makedirs(banner_image_folder3)
                blogImage3_path = os.path.join(banner_image_folder3, blogImage3_file.name)
                with open(blogImage3_path, 'wb') as destination:
                    for chunk in blogImage3_file.chunks():
                        destination.write(chunk)
            else:
                blogImage3 = None 
            
            blog_detail_obj = BlogDetails(
                blog_description=richtextarea3,  # Assuming you have retrieved richtextarea earlier
                blog_id=blog_entry_folder,
                image_path=blogImage3,
                created_by = date,
                updated_by = date,
                created_name = username,
                updated_name =username,
                title = request.POST.get('title3'),
            )
            blog_detail_obj.save()
        if richtextarea4:
            if 'blogImage4' in request.FILES:
                blogImage4_file = request.FILES['blogImage4']
                blogImage4 = blogImage4_file.name
                if not os.path.exists(banner_image_folder4):
                    os.makedirs(banner_image_folder4)
                blogImage4_path = os.path.join(banner_image_folder4, blogImage4_file.name)
                with open(blogImage4_path, 'wb') as destination:
                    for chunk in blogImage4_file.chunks():
                        destination.write(chunk)
            else:
                blogImage4 = None
            
            blog_detail_obj = BlogDetails(
                blog_description=richtextarea4,  # Assuming you have retrieved richtextarea earlier
                blog_id=blog_entry_folder,
                image_path=blogImage4,
                created_by = date,
                updated_by = date,
                created_name = username,
                updated_name =username,
                title = request.POST.get('title4'),
            )
            blog_detail_obj.save()
        if richtextarea5:
            if 'blogImage5' in request.FILES:
                blogImage5_file = request.FILES['blogImage5']
                blogImage5 = blogImage5_file.name
                if not os.path.exists(banner_image_folder5):
                    os.makedirs(banner_image_folder5)
                blogImage5_path = os.path.join(banner_image_folder5, blogImage5_file.name)
                with open(blogImage5_path, 'wb') as destination:
                    for chunk in blogImage5_file.chunks():
                        destination.write(chunk)
            else:
                blogImage5 = None
            
            blog_detail_obj = BlogDetails(
                blog_description=richtextarea5,  # Assuming you have retrieved richtextarea earlier
                blog_id=blog_entry_folder,
                image_path=blogImage5,
                created_by = date,
                updated_by = date,
                created_name = username,
                updated_name =username,
                title = request.POST.get('title5'),
            )
            blog_detail_obj.save()
        if richtextarea6:
            if 'blogImage6' in request.FILES:
                blogImage6_file = request.FILES['blogImage6']
                blogImage6 = blogImage6_file.name
                if not os.path.exists(banner_image_folder6):
                    os.makedirs(banner_image_folder6)
                blogImage6_path = os.path.join(banner_image_folder6, blogImage6_file.name)
                with open(blogImage6_path, 'wb') as destination:
                    for chunk in blogImage6_file.chunks():
                        destination.write(chunk)
            else:
                blogImage6 = None
            
            blog_detail_obj = BlogDetails(
                blog_description=richtextarea6,  # Assuming you have retrieved richtextarea earlier
                blog_id=blog_entry_folder,
                image_path=blogImage6,
                created_by = date,
                updated_by = date,
                created_name = username,
                updated_name =username,
                title = request.POST.get('title6'),
            )
            blog_detail_obj.save()
        if richtextarea7:
            if 'blogImage7' in request.FILES:
                blogImage7_file = request.FILES['blogImage7']
                blogImage7 = blogImage7_file.name
                if not os.path.exists(banner_image_folder7):
                    os.makedirs(banner_image_folder7)
                blogImage7_path = os.path.join(banner_image_folder7, blogImage7_file.name)
                with open(blogImage7_path, 'wb') as destination:
                    for chunk in blogImage7_file.chunks():
                        destination.write(chunk)
            else:
                blogImage7 = None
            
            blog_detail_obj = BlogDetails(
                blog_description=richtextarea7,  # Assuming you have retrieved richtextarea earlier
                blog_id=blog_entry_folder,
                image_path=blogImage7,
                created_by = date,
                updated_by = date,
                created_name = username,
                updated_name =username,
                title = request.POST.get('title7'),
            )
            blog_detail_obj.save()
        if richtextarea8:
            if 'blogImage8' in request.FILES:
                blogImage8_file = request.FILES['blogImage8']
                blogImage8 = blogImage8_file.name
                if not os.path.exists(banner_image_folder8):
                    os.makedirs(banner_image_folder8)
                blogImage8_path = os.path.join(banner_image_folder8, blogImage8_file.name)
                with open(blogImage8_path, 'wb') as destination:
                    for chunk in blogImage8_file.chunks():
                        destination.write(chunk)
            else:
                blogImage8 = None
            
            blog_detail_obj = BlogDetails(
                blog_description=richtextarea8,  # Assuming you have retrieved richtextarea earlier
                blog_id=blog_entry_folder,
                image_path=blogImage8,
                created_by = date,
                updated_by = date,
                created_name = username,
                updated_name =username,
                title = request.POST.get('title8'),
            )
            blog_detail_obj.save()
        if richtextarea9:
            if 'blogImage9' in request.FILES:
                blogImage9_file = request.FILES['blogImage9']
                blogImage9 = blogImage9_file.name
                if not os.path.exists(banner_image_folder9):
                    os.makedirs(banner_image_folder9)
                blogImage9_path = os.path.join(banner_image_folder9, blogImage9_file.name)
                with open(blogImage9_path, 'wb') as destination:
                    for chunk in blogImage9_file.chunks():
                        destination.write(chunk)
            else:
                blogImage9 = None
            
            blog_detail_obj = BlogDetails(
                blog_description=richtextarea9,  # Assuming you have retrieved richtextarea earlier
                blog_id=blog_entry_folder,
                image_path=blogImage9,
                created_by = date,
                updated_by = date,
                created_name = username,
                updated_name =username,
                title = request.POST.get('title9'),
            )
            blog_detail_obj.save()   
        if richtextarea10:
            if 'blogImage10' in request.FILES:
                blogImage10_file = request.FILES['blogImage10']
                blogImage10 = blogImage10_file.name
                if not os.path.exists(banner_image_folder10):
                    os.makedirs(banner_image_folder10)
                blogImage10_path = os.path.join(banner_image_folder10, blogImage10_file.name)
                with open(blogImage10_path, 'wb') as destination:
                    for chunk in blogImage10_file.chunks():
                        destination.write(chunk)
            else:
                blogImage10 = None
            
            blog_detail_obj = BlogDetails(
                blog_description=richtextarea10,  # Assuming you have retrieved richtextarea earlier
                blog_id=blog_entry_folder,
                image_path=blogImage10,
                created_by = date,
                updated_by = date,
                created_name = username,
                updated_name =username,
                title = request.POST.get('title10'),
            )
            blog_detail_obj.save()
        
        current_time = timezone.now()
        current_time_str = current_time.strftime("%b %d, %Y")

        current_date_str = timezone.now().strftime("%d-%m-%Y")
        

        description = {
                "hint": hint,
                "category": category,
                "author": author,
                "url": url,
                "title": title,
                "content": content,
                "description":descriptions,
                "jump_link_titles": jump_link_titles,
                "meta_title": meta_title,
                "meta_description": meta_description,
                "meta_keywords": meta_keywords,

                "banner_image_url": banner_image_url,
                "banner_image_path": banner_image_path,
                "banner_image":banner_image,

                "TabBanner_Image_url": TabBanner_Image_url,
                "TabBanner_Image_path": TabBanner_Image_path,
                "TabBanner_Image":TabBanner_Image,

                "MobileBanner_Image_url": MobileBanner_Image_url,
                "MobileBanner_Image_path": MobileBanner_Image_path,
                "MobileBanner_Image":MobileBanner_Image,

                "cover_image_url": cover_image_url,
                "cover_image_path": cover_image_path,
                "cover_image":cover_image,
                "grid_image_url": grid_image_url,
                "grid_image_path": grid_image_path,
                "grid_image":grid_image,
                "tags":tags
            }
        
        # Update the BlogUs model instance with the created description
        blog_entry.description = description
        blog_entry.tags = tagsid
        blog_entry.url = url
        blog_entry.canonical = Canonical
        blog_entry.created_by = date
        blog_entry.updated_by = date
        blog_entry.created_name = username
        blog_entry.updated_name = username
        blog_entry.save()

        print(description)

        return redirect('blog_us_admin')  # Redirect to a success page
    
    userdetails = adminheader(request)

    return render(request, "admin/addblogs.html",{"userdetails":userdetails})

def updateblogs(request):
    # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')

    if 'id' in request.GET:
        blog_entry_id = request.GET['id']
        page = request.GET['page']
        try:
            # Get the BlogUs instance with the provided ID
            userdetails = adminheader(request)
            blog_entry = Blog.objects.get(id=blog_entry_id)
            ids = blog_entry.id
            tagsid = blog_entry.tags
            canonical = blog_entry.canonical
            description = blog_entry.description
            blogContent = []
            Blog_Details = BlogDetails.objects.filter(blog_id=ids)
            for blog_detail in Blog_Details:
                blogContent.append({'blog_id':blog_detail.blog_id,'id':blog_detail.id,'blog_description':blog_detail.blog_description,"image_path":blog_detail.image_path,"title":blog_detail.title})
            print(blogContent  )
            # Now you have access to all the details of the blog entry through 'description'
            return render(request, "admin/updateblogentry.html", {'page':page,'blog_entry_id':blog_entry_id,'description': description,'tagsid':tagsid,"userdetails":userdetails,"blogContent":blogContent,"canonical":canonical})
        except Blog.DoesNotExist:
            return HttpResponse('Blog entry with the provided ID does not exist')
    else:
        return HttpResponse('No ID provided for update')
    return render(request, "admin/addblogs.html")

def tags_list(request):
    tags = Tags.objects.all().values('id', 'tag_name')
    return JsonResponse(list(tags), safe=False)

def blogtag(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return HttpResponse("You do not have access to this page.")
    
    if request.method == "POST":
        # Assuming the word to be inserted into the Tags model is sent via POST request
        word = request.POST.get('word', None)
        if word:
            # Insert the word into the Tags model
            tag = Tags.objects.create(tag_name=word)
            tag.save()
            # Optionally, you can add a success message or redirect the user to another page
            return redirect('createblogs')

    return render(request, "admin/blogtag.html")
    
def blogupdatetags(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    username = request.session.get('username')
    role = request.session.get('role')
    userdetails = adminheader(request)
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M")
    # current_time_str = current_time.strftime("%b %d, %Y")
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')

    if request.method == 'POST':
        id = request.POST.get('id', '')
        tags = request.POST.get('tags', '')
       

        footer = Tags.objects.get(id=id)
       
        footer.tag_name = tags

        footer.save()

        return redirect('blog_us_admin')
    
    return redirect('blog_us_admin')

def deleteblogtitle(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    username = request.session.get('username')
    role = request.session.get('role')
    userdetails = adminheader(request)
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M")
    # current_time_str = current_time.strftime("%b %d, %Y")
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if role == 'data':
        return redirect('blog_us_admin')

    if request.method == 'GET':
        ids = request.GET.get('id', '')

        # Retrieve the FooterHeader object based on the id
        footer_header_object = Tags.objects.get(id=ids)
        
        # Delete the object
        footer_header_object.delete()
        return redirect('blog_us_admin')
    
    return redirect('blog_us_admin')

def blogtagadd(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return HttpResponse("You do not have access to this page.")
    
    if request.method == "POST":
        # Assuming the word to be inserted into the Tags model is sent via POST request
        word = request.POST.get('word', None)
        if word:
            # Insert the word into the Tags model
            tag = Tags.objects.create(tag_name=word)
            tag.save()
            # Optionally, you can add a success message or redirect the user to another page
            return redirect(blog_us_admin)

    return render(request, "admin/blogtag.html")

def update_blog_popular_state(request):

     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        new_state = request.POST.get('new_state') == 'on'

        blog = Blog.objects.get(id=blog_id)
        blog.popular = int(not new_state)  # Convert new_state to int (0 or 1)
        blog.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def update_blog_hidden_state(request):

     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        new_state = request.POST.get('new_state') == 'on'

        blog = Blog.objects.get(id=blog_id)
        blog.hidden = int(not new_state)  # Convert new_state to int (0 or 1)
        blog.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def deleteblogs(request):
    username = request.session.get('username')
    role = request.session.get('role')

    if not username or not role:
        return redirect('login')

    if role != 'admin' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    if role == 'data':
        return redirect('blog_us_admin')

    if request.method == 'GET':
        blog_entry_id = request.GET.get('id','')
        print("blog_entry_id")
        blog_entry_folder = str(blog_entry_id)
        review = Blog.objects.get(id=blog_entry_id)
        blog_details = BlogDetails.objects.filter(blog_id=blog_entry_id)
        image_path =  os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image', blog_entry_folder)
        image_path_main =  os.path.join(settings.BASE_DIR, 'VFpages/static/image/blog_image/blog_main', blog_entry_folder)
        print(image_path)
        if os.path.exists(image_path):
            shutil.rmtree(image_path)
        if os.path.exists(image_path_main):
            shutil.rmtree(image_path_main)
        
        
        for blog in blog_details:
            blog.delete()
        review.delete()
        return redirect('blog_us_admin')

def submit_form_blogus(request):

     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.session.get('username')
        role = request.session.get('role')
        title = request.POST.get('title')
        description = request.POST.get('description')
        keyword = request.POST.get('keyword')

        page = PagesTable.objects.get(pagesname='blog_us')
        
        current_date_str = datetime.now().strftime('%Y-%m-%d')

        # Update the description field with JSON data including updated time and person's name
        # created_by = page.created_by
        # updated_by = f"{username} {current_date_str}"
        page_description = {
            'updated_time': timezone.now().isoformat(),  # Store updated time in ISO 8601 format
            'updated_person_name': username,
            'created_time':timezone.now().isoformat(), 
            'created_person_name':username,
            'meta_title': title,
            'meta_description':description,
            'meta_keyword':keyword
        }

        # Save the changes to the database

        # Check if the about page already exists in the database
        blog_us = PagesTable.objects.filter(pagesname='blog_us').first()
        if blog_us:
            # If it exists, update the description
            blog_us.description = page_description
            # blog_us.created_by = current_date_str
            blog_us.updated_by = current_date_str
            # blog_us.created_name = username
            blog_us.updated_name = username
            blog_us.save()
        else:
            # If it doesn't exist, create a new entry
            PagesTable.objects.create(pagesname='contact us', description=description)
        
        return redirect('blog_us_admin')  # Redirect to a success page

    return render(request, "admin/blog_us_adminpanel.html")

def packagesadmin(request):

     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    Package_list = Packages.objects.all()
    destination_category = Category.objects.all()
    # datedata = Package_list.description
    search_query = request.GET.get('search_query')
    counthome = request.GET.get('count')
    countcategories = request.GET.get('categories')
    
    
    count_false_popular = Packages.objects.filter(homepage=False).count()
    
    

    if search_query:
        Package_list = Package_list.filter(description__cities__icontains=search_query)
    
    categeory_slugs = Category.objects.values_list('categeory_slug', flat=True).distinct()

    # Create a dictionary to store counts for each categeory_slug
    counts_by_slug = {}

    # Loop through each categeory_slug value
    for slug in categeory_slugs:
        # Count the number of Packages for the current categeory_slug where category_button is 0
        count = Packages.objects.filter(destination_category=slug, category_button=0).count()
        # count = Packages.objects.filter(destination_category=slug).count()
        # print(count)
        
        # Store the count in the dictionary
        counts_by_slug[slug] = count

    paginator = Paginator(Package_list, 5)  # Show 5 blog entries per page
    
    if counthome:
        Package_list = Packages.objects.filter(homepage=False)
        count_false_popular =  Packages.objects.filter(homepage=False).count()
        paginator = Paginator(Package_list, count_false_popular)
        
    if countcategories:
        Package_list = Packages.objects.filter(destination_category=countcategories,category_button=False)
        false_popular =  Packages.objects.filter(destination_category=countcategories,category_button=False).count()
        if countcategories == "Not-selected":
            paginator = Paginator(Package_list, 1)
        else:
            paginator = Paginator(Package_list, false_popular)

    page = request.GET.get('page')
    try:
        Package_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        Package_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        Package_list = paginator.page(paginator.num_pages)
    
    return render(request, "admin/packages.html",{"page":page,'Destination': Package_list,"userdetails":userdetails,"destination_category":destination_category,"counts_by_slug":counts_by_slug,"count_false_popular":count_false_popular})

def update_destination_category(request):
    if request.method == 'POST':
        destination_id = request.POST.get('destination_id', None)
        selected_category = request.POST.get('selected_category', None)
        if destination_id is not None and selected_category is not None:
            try:
                # Assuming destination_id is the primary key of the Destination model
                package = Packages.objects.get(id=destination_id)
                package.destination_category = selected_category
                package.save()
                return JsonResponse({'success': True})
            except Packages.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Package with provided ID does not exist.'})
    return JsonResponse({'success': False, 'error': 'Invalid request or method.'})


def packagesmainadmin(request):

     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    Destnation = Destination.objects.all()

    userdetails = adminheader(request)
    

    all_des = []


    for destination in Destnation:
        all_des.append({"id":destination.id,"category":destination.category,"destination_name":destination.destination_name})
    
    print(all_des)

    Internation = []
    Domestic = []

    # Iterate over each destination and separate them based on their category
    for destination in all_des:
        print(destination)
        if destination['category'] == '0':
            Internation.append(destination)
            
        elif destination['category'] == '1':
            Domestic.append(destination)
    print(Domestic)
    
    Lead_details =  Lead.objects.using('second_database').all()
    
    return render(request, "admin/packagesmainadmin.html",{'Internation':Internation,'Domestic':Domestic,"userdetails":userdetails,"Lead_details":Lead_details})

def createpackages(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.session.get('username')
        Noofdays = request.POST.get('Noofdays')
        # rating = request.POST.get('rating')
        price = request.POST.get('price')
        person = request.POST.get('person')
        place1 = request.POST.get('place1')
        place2 = request.POST.get('place2')
        descriptions = request.POST.get('description')
        content = request.POST.get('content')
        leadName = request.POST.get('leadName')
        destination_package_id = request.POST.get('destination_package_id')
        destination_package_name = request.POST.get('destination_package_name')
        meta_title = request.POST.get('metaTitle')
        meta_description = request.POST.get('metaDescription')
        meta_keywords = request.POST.get('metaKeywords')
        canonical = request.POST.get('canonical')
        destinationtype = request.POST.get('destinationtype')

        itinerayid = request.POST.get('itinerayid')
        Url_lead = request.POST.get('Url_lead')
        pakageHeading = request.POST.get('pakageHeading')
        Days = request.POST.get('Days')
        Transfers = request.POST.get('TRANSFERS')
        Hotel = request.POST.get('HOTEL')
        Breakfast = request.POST.get('BREAKFAST')
        Sightseeing = request.POST.get('SIGHTSEEING')
        Category = request.POST.get('CATEGORY')

        # Create an instance of BlogUs model
        Package = Packages.objects.create()

        # Generate folder names based on the ID of the created blog entry
        Packages_folder = str(Package.id)
        cover_image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/packages', Packages_folder)
        cover_image_folder1 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/packages', Packages_folder)
        cover_image_folder2 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/packages', Packages_folder)
        grid_image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/packages', Packages_folder)

        if 'Cover_Image' in request.FILES:
            cover_image_file = request.FILES['Cover_Image']
            cover_image = cover_image_file.name
            if not os.path.exists(cover_image_folder):
                os.makedirs(cover_image_folder)
            cover_image_path = os.path.join(cover_image_folder, cover_image_file.name)
            with open(cover_image_path, 'wb') as destination:
                for chunk in cover_image_file.chunks():
                    destination.write(chunk)
            cover_image_url_first = os.path.join('/image/packages', Packages_folder, cover_image_file.name)
            cover_image_url = cover_image_url_first.replace("\\", "/")
        else:
            cover_image_url = None
            cover_image_path = None
            cover_image = None
        if 'TabCover' in request.FILES:
            cover_image_file1 = request.FILES['TabCover']
            cover_image1 = cover_image_file1.name
            if not os.path.exists(cover_image_folder1):
                os.makedirs(cover_image_folder1)
            cover_image_path1 = os.path.join(cover_image_folder, cover_image_file1.name)
            with open(cover_image_path1, 'wb') as destination:
                for chunk in cover_image_file1.chunks():
                    destination.write(chunk)
            cover_image_url_first1 = os.path.join('/image/packages', Packages_folder, cover_image_file1.name)
            cover_image_url1 = cover_image_url_first1.replace("\\", "/")
        else:
            cover_image_url1 = None
            cover_image_path1 = None
            cover_image1 = None
            
        if 'MobileCover' in request.FILES:
            cover_image_file2 = request.FILES['MobileCover']
            cover_image2 = cover_image_file2.name
            if not os.path.exists(cover_image_folder2):
                os.makedirs(cover_image_folder2)
            cover_image_path2 = os.path.join(cover_image_folder2, cover_image_file2.name)
            with open(cover_image_path2, 'wb') as destination:
                for chunk in cover_image_file2.chunks():
                    destination.write(chunk)
            cover_image_url_first2 = os.path.join('/image/packages', Packages_folder, cover_image_file2.name)
            cover_image_url2 = cover_image_url_first2.replace("\\", "/")
        else:
            cover_image_url2 = None
            cover_image_path2 = None
            cover_image2 = None
            
        if 'Grid_Image' in request.FILES:
            grid_image_file = request.FILES['Grid_Image']
            grid_image = grid_image_file.name
            if not os.path.exists(grid_image_folder):
                os.makedirs(grid_image_folder)
            grid_image_path = os.path.join(grid_image_folder, grid_image_file.name)
            with open(grid_image_path, 'wb') as destination:
                for chunk in grid_image_file.chunks():
                    destination.write(chunk)
            grid_image_url = os.path.join('/image/packages', Packages_folder, grid_image_file.name)
        else:
            grid_image_url = None
            grid_image_path = None
            grid_image = None

        current_time = timezone.now()
        current_time_str = current_time.strftime("%b %d, %Y")

        current_date_str = datetime.now().strftime("%d/%m/%Y")
        current_d = datetime.now().strftime('%Y-%m-%d')

        # filtered_cities = InternationalCities.objects.filter(destination_id=destination_package_id)
        # print(filtered_cities)
        # cities = filtered_cities.international_city_name

        description = {
                "Noofdays": Noofdays,
                # "rating": rating,
                "price": price,
                "person": person,
                "leadName": leadName,
                "place1": place1,
                "place2":place2,
                "content": content,
                "descriptions":descriptions,
                "meta_title": meta_title,
                "meta_description": meta_description,
                "meta_keywords": meta_keywords,
                # "richtextarea": richtextarea,
                "cover_image_url": cover_image_url,
                "cover_image_path": cover_image_path,
                "cover_image":cover_image,
                
                "cover_image_url1": cover_image_url1,
                "cover_image_path1": cover_image_path1,
                "cover_image1":cover_image1,

                "cover_image_url2": cover_image_url2,
                "cover_image_path2": cover_image_path2,
                "cover_image2":cover_image2,
                
                "grid_image_url": grid_image_url,
                "grid_image_path": grid_image_path,
                "grid_image":grid_image,
                "updated_by": f"{username} {current_date_str}",   # Assuming you have authentication and can access the current user
                "updated_on": current_time_str,
                "created_by": f"{username} {current_date_str}",   # Assuming you have authentication and can access the current user
                "created_on": current_time_str,
                "cities":destination_package_name,
                "destinationtype":destinationtype,
                "canonical":canonical,

                "Url_in_lead":Url_lead,
                "leadDays_nights":Days,
                "leadTransfers":Transfers,
                "leadHotel":Hotel,
                "leadBreakfast":Breakfast,
                "leadSightseeing":Sightseeing,
                "leadCategory":Category,
                "leadpakageHeading":pakageHeading
            }


        
        # Update the BlogUs model instance with the created description
        Package.description = description
        Package.packages_id = destination_package_id
        Package.updated_by = username
        Package.created_by = username
        Package.created_date = current_d
        Package.updated_date = current_d
        Package.itinaries_id = itinerayid
        Package.destination_category = "Not-selected"
        Package.save()

        print(description)

        return redirect('packagesadmin')  # Redirect to a success page

    return render(request, "admin/packagesadmin.html")

def deletepackages(request):
    username = request.session.get('username')
    role = request.session.get('role')

    if not username or not role:
        return redirect('login')

    if role != 'admin' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    if role == 'data':
        return redirect('packagesadmin')

    if request.method == 'GET':
        blog_entry_id = request.GET.get('id','')
        print("blog_entry_id")
        blog_entry_folder = str(blog_entry_id)
        review = Packages.objects.get(id=blog_entry_id)
        image_path =  os.path.join(settings.BASE_DIR, 'VFpages/static/image/packages', blog_entry_folder)
        print(image_path)
        if os.path.exists(image_path):
            shutil.rmtree(image_path)
        
        review.delete()
        return redirect('packagesadmin')
    
def updatepackages(request):
    # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')

    if 'id' in request.GET:
        blog_entry_id = request.GET['id']
        page = request.GET['page']
        try:
            Destnation = Destination.objects.all()
            all_des = []


            for destination in Destnation:
                all_des.append({"id":destination.id,"category":destination.category,"destination_name":destination.destination_name})
            
            print(all_des)

            Internation = []
            Domestic = []

            # Iterate over each destination and separate them based on their category
            for destination in all_des:
                print(destination)
                if destination['category'] == '0':
                    Internation.append(destination)
                    
                elif destination['category'] == '1':
                    Domestic.append(destination)
            print(Domestic)
            userdetails = adminheader(request)
            # Get the BlogUs instance with the provided ID
            describtion_list = Packages.objects.get(id=blog_entry_id)
            description = describtion_list.description
            destination_package_id = describtion_list.packages_id
            lead_id = describtion_list.itinaries_id
            
            Lead_details =  Lead.objects.using('second_database').all()
            
            # Now you have access to all the details of the blog entry through 'description'
            return render(request, "admin/packageupdate.html", {"page":page,'blog_entry_id':blog_entry_id,'description': description,'destination_package_id':destination_package_id,'Internation':Internation,'Domestic':Domestic,"userdetails":userdetails,"Lead_details":Lead_details,"lead_id":lead_id})
        except Blog.DoesNotExist:
            return HttpResponse('Blog entry with the provided ID does not exist')
    else:
        return HttpResponse('No ID provided for update')
    return render(request, "admin/addblogs.html")

def addpackages(request):
    # Check authentication and role
    # Check authentication and role
    username = request.session.get('username')
    role = request.session.get('role')

    if not username or not role:
        return redirect('login')

    if role != 'admin' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    
    blog_entry_id = None
    description = None

    if request.method == 'POST':
        blog_entry_id = request.POST.get('id','')
        try:
            # Get the BlogUs instance with the provided ID
            userdetails = adminheader(request)
            Package_list = Packages.objects.get(id=blog_entry_id)
            description = Package_list.description
            print(description)
            if request.method == 'POST':
                # Retrieve existing values
                existing_grid_image_url = description.get('grid_image_url', None)
                existing_cover_image_url = description.get('cover_image_url', None)
                existing_cover_image_url1 = description.get('cover_image_url1', None)
                existing_cover_image_url2 = description.get('cover_image_url2', None)
                
                existing_grid_image_path = description.get('grid_image_path', None)
                existing_cover_image_path = description.get('cover_image_path', None)
                existing_cover_image_path1 = description.get('cover_image_path1', None)
                existing_cover_image_path2 = description.get('cover_image_path2', None)
               
                existing_cover_image = description.get('cover_image', None)
                existing_cover_image1 = description.get('cover_image1', None)
                existing_cover_image2 = description.get('cover_image2', None)
                existing_grid_image = description.get('grid_image', None)
                created_by = description.get('created_by', None)
                created_on = description.get('created_on', None)
                updated_on = description.get('updated_on', None)
                updated_by = description.get('updated_by', None)
                Noofdays = request.POST.get('Noofdays')
                # rating = request.POST.get('rating')
                tags = request.POST.get('tags')
                price = request.POST.get('price')
                person = request.POST.get('person')
                place1 = request.POST.get('place1')
                place2 = request.POST.get('place2')
                content = request.POST.get('content')
                descriptions = request.POST.get('description')
                leadName = request.POST.get('leadName')
                meta_title = request.POST.get('metaTitle')
                destination_package_id = request.POST.get('destination_package_id')
                destination_package_name = request.POST.get('destination_package_name')
                destinationtype = request.POST.get('destinationtype')
                meta_description = request.POST.get('metaDescription')
                meta_keywords = request.POST.get('metaKeywords')
                canonical = request.POST.get('canonical')
                
                itinerayid = request.POST.get('itinerayid')
                Url_lead = request.POST.get('Url_lead')
                pakageHeading = request.POST.get('pakageHeading')
                Days = request.POST.get('Days')
                Transfers = request.POST.get('TRANSFERS')
                Hotel = request.POST.get('HOTEL')
                Breakfast = request.POST.get('BREAKFAST')
                Sightseeing = request.POST.get('SIGHTSEEING')
                Category = request.POST.get('CATEGORY')
                
                description = {
                    "Noofdays": Noofdays,
                    # "rating": rating,
                    "tags": tags,
                    "price": price,
                    "person": person,
                    "place1":place1,
                    "place2": place2,
                    "content":content,
                    "leadName": leadName,
                    "meta_title": meta_title,
                    "meta_description": meta_description,
                    "meta_keywords": meta_keywords,
                    "canonical": canonical,
                    "destination_package_id":destination_package_id,
                    "created_by":created_by,
                    "cover_image_url": existing_cover_image_url,
                    "cover_image_path": existing_cover_image_path,
                    "cover_image":existing_cover_image,
                    
                    "cover_image_url1": existing_cover_image_url1,
                    "cover_image_path1": existing_cover_image_path1,
                    "cover_image1":existing_cover_image1,

                    "cover_image_url2": existing_cover_image_url2,
                    "cover_image_path2": existing_cover_image_path2,
                    "cover_image2":existing_cover_image2,
                    
                    "grid_image_url": existing_grid_image_url,
                    "grid_image_path": existing_grid_image_path,
                    "grid_image":existing_grid_image,
                    "updated_by": updated_by,   # Assuming you have authentication and can access the current user
                    "updated_on": updated_on,
                    "created_by": created_by,   # Assuming you have authentication and can access the current user
                    "created_on": created_on,
                    "cities":destination_package_name,
                    "descriptions":descriptions,
                    "destinationtype":destinationtype,

                    "Url_in_lead":Url_lead,
                    "leadDays_nights":Days,
                    "leadTransfers":Transfers,
                    "leadHotel":Hotel,
                    "leadBreakfast":Breakfast,
                    "leadSightseeing":Sightseeing,
                    "leadCategory":Category,
                    "leadpakageHeading":pakageHeading,
                }


                # Generate folder names based on the ID of the created blog entry
                Packages_folder = str(Package_list.id)
                cover_image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/packages', Packages_folder)
                cover_image_folder1 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/packages', Packages_folder)
                cover_image_folder2 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/packages', Packages_folder)
                grid_image_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/image/packages', Packages_folder)
                if 'Grid_Image' in request.FILES:
                    blog_entry_folder = str(Package_list.id)
                    if existing_grid_image:
                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/packages', blog_entry_folder , existing_grid_image)
                        if os.path.exists(old_image_path):
                            os.remove(old_image_path)
                    if not os.path.exists(grid_image_folder):
                        os.makedirs(grid_image_folder)
                    new_image = request.FILES['Grid_Image']
                    img_path = new_image.name
                    image_path = os.path.join(settings.BASE_DIR,'VFpages/static/image/packages', blog_entry_folder, img_path)
                    with open(image_path, 'wb') as destination:
                        for chunk in new_image.chunks():
                            destination.write(chunk)
                    description['grid_image_url'] = os.path.join('/image/packages', blog_entry_folder, img_path)
                    description['grid_image'] = img_path

                if 'Cover_Image' in request.FILES:
                    blog_entry_folder = str(Package_list.id)
                    if existing_cover_image:
                        old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/packages', blog_entry_folder,existing_cover_image)
                        if os.path.exists(old_image_path):
                            os.remove(old_image_path)
                    if not os.path.exists(cover_image_folder):
                        os.makedirs(cover_image_folder)
                    new_image = request.FILES['Cover_Image']
                    img_path = new_image.name
                    image_path = os.path.join(settings.BASE_DIR,'VFpages/static/image/packages', blog_entry_folder, img_path)
                    with open(image_path, 'wb') as destination:
                        for chunk in new_image.chunks():
                            destination.write(chunk)
                    cover_image_url_first = os.path.join('/image/packages', blog_entry_folder, img_path)
                    cover_image_url = cover_image_url_first.replace("\\", "/")
                    description['cover_image_url'] = cover_image_url
                    description['cover_image'] = img_path
                if 'TabCover' in request.FILES:
                    blog_entry_folder = str(Package_list.id)
                    if existing_cover_image1:
                        old_image_path1 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/packages', blog_entry_folder,existing_cover_image1)
                        if os.path.exists(old_image_path1):
                            os.remove(old_image_path1)
                    if not os.path.exists(cover_image_folder1):
                        os.makedirs(cover_image_folder1)
                    new_image1 = request.FILES['TabCover']
                    img_path1 = new_image1.name
                    image_path1 = os.path.join(settings.BASE_DIR,'VFpages/static/image/packages', blog_entry_folder, img_path1)
                    with open(image_path1, 'wb') as destination:
                        for chunk in new_image1.chunks():
                            destination.write(chunk)
                    cover_image_url_first1 = os.path.join('/image/packages', blog_entry_folder, img_path1)
                    cover_image_url1= cover_image_url_first1.replace("\\", "/")
                    description['cover_image_url1'] = cover_image_url1
                    description['cover_image1'] = img_path1
                if 'MobileCover' in request.FILES:
                    blog_entry_folder = str(Package_list.id)
                    if existing_cover_image2:
                        old_image_path2 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/packages', blog_entry_folder,existing_cover_image2)
                        if os.path.exists(old_image_path2):
                            os.remove(old_image_path2)
                    if not os.path.exists(cover_image_folder2):
                        os.makedirs(cover_image_folder2)
                    new_image2 = request.FILES['MobileCover']
                    img_path2 = new_image2.name
                    image_path2 = os.path.join(settings.BASE_DIR,'VFpages/static/image/packages', blog_entry_folder, img_path2)
                    with open(image_path2, 'wb') as destination:
                        for chunk in new_image2.chunks():
                            destination.write(chunk)
                    cover_image_url_first2 = os.path.join('/image/packages', blog_entry_folder, img_path2)
                    cover_image_url2 = cover_image_url_first2.replace("\\", "/")
                    description['cover_image_url2'] = cover_image_url2
                    description['cover_image2'] = img_path2
                
                # Update 'updated_by' key
                username = request.session.get('username')
                current_time = timezone.now().strftime("%Y-%m-%d %H:%M")
                current_date_str = datetime.now().strftime("%d/%m/%Y")
                current_d = datetime.now().strftime('%Y-%m-%d')
                description['updated_by'] = f"{username} {current_date_str}"

                # Update BlogUs instance with the modified description
                Package_list.description = description
                Package_list.packages_id = destination_package_id
                Package_list.itinaries_id = itinerayid
                
                Package_list.updated_by = username
                Package_list.updated_date = current_d
                print(Package_list.description )
                Package_list.save()
                return redirect('packagesadmin') 
        except Blog.DoesNotExist:
            return HttpResponse('Blog entry with the provided ID does not exist') # Redirect to success page

    return render(request, "admin/updateblogentry.html", {'blog_entry_id': blog_entry_id, 'description': description,"userdetails":userdetails})

def update_packages_hidden_state(request):

     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        new_state = request.POST.get('new_state') == 'on'

        blog = Packages.objects.get(id=blog_id)
        blog.hidden = int(not new_state)  # Convert new_state to int (0 or 1)
        blog.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def update_packages_home_state(request):

     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        new_state = request.POST.get('new_state') == 'on'

        blog = Packages.objects.get(id=blog_id)
        blog.homepage = int(not new_state)  # Convert new_state to int (0 or 1)
        blog.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


# def Destination_meta(request):

#      # Check if user is authenticated
#     if not request.session.get('username') or not request.session.get('role'):
#         # Redirect to login page if session data is not found
#         return redirect('login')

#     # Check if the user has the appropriate role to access this page
#     role = request.session.get('role')
#     userdetails = adminheader(request)
#     if role != 'admin' and role != 'superadmin' and role != 'employee':
#         # Redirect to appropriate page if the role is not admin
#         return redirect('dashboard')
    
#     return render(request, 'admin/destination/destination_meta.html')

# ===================================  home page slider =========================

def Homepage_slider(request):

     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    Destnation = Destination.objects.all()

    all_des = []
    for destination in Destnation:
        all_des.append({"id":destination.id,"category":destination.category,"destination_name":destination.destination_name,"destination_slug":destination.destination_slug})

    Internation = []
    Domestic = []

    # Iterate over each destination and separate them based on their category
    for destination in all_des:
        if destination['category'] == '0':
            Internation.append(destination)
        elif destination['category'] == '1':
            Domestic.append(destination)

    Homeslider = HomepageSlider.objects.all()
    print('home page slider',Homeslider)
    package = Packages.objects.all()

    return render(request, 'admin/homepage/Slider_homepage.html',{"package":package,'Internation':Internation,'Domestic':Domestic,"Homeslider":Homeslider,"userdetails":userdetails})

def Homepage_slider_add(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')

    if request.method == 'POST':
        HomeDestinationName = request.POST.get('HomeDestinationName')
        SliderTitle = request.POST.get('package')
        SliderContent = request.POST.get('SliderContent')
        Select_In_do = request.POST.get('SelectIn_do')
        # SliderImage = request.POST.get('SliderImage')
     # Check if user is authenticated
   

    # if request.method == 'POST':

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if 'SliderImage' in request.FILES:
            Images = request.FILES['SliderImage']
            img_path = Images.name
            Imagesimage_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image', img_path)
            with open(Imagesimage_path, 'wb') as destination:
                for chunk in Images.chunks():
                    destination.write(chunk)
        if 'tabImage' in request.FILES:
            Images = request.FILES['tabImage']
            img_path2 = Images.name
            Imagesimage_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image', img_path2)
            with open(Imagesimage_path, 'wb') as destination:
                for chunk in Images.chunks():
                    destination.write(chunk)
        if 'mobileImage' in request.FILES:
            Images = request.FILES['mobileImage']
            img_path3 = Images.name
            Imagesimage_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image', img_path3)
            with open(Imagesimage_path, 'wb') as destination:
                for chunk in Images.chunks():
                    destination.write(chunk)

        description_data = {
            "HomeDestinationName": HomeDestinationName,
            "SliderTitle": SliderTitle,
            "SliderContent": SliderContent,
            "Select_In_do": Select_In_do,
            "SliderImage": img_path,
            "tabImage": img_path2,
            "mobileImage": img_path3,
            "crete_date": current_time,
            "update_date": current_time

        }
        
        # Convert the dictionary to JSON string
        # description_json = json.dumps(description_data)

        # Insert data into the Homepage model
        homepage_instance = HomepageSlider(description=description_data,create_us=current_time,update_us=current_time)
        homepage_instance.save()

        return redirect('Homepage_slider')  # You can render a success page or redirect as needed
    else:
        return render(request, 'admin/homepage/Homepage_slider.html',{"userdetails":userdetails})

def Homepage_slider_Edit(request,team_id):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    slideredit = HomepageSlider.objects.get(id=team_id)
    if request.method == 'POST':
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        slideredit.description['HomeDestinationName'] = request.POST.get('HomeDestinationName')
        slideredit.description['SliderTitle'] = request.POST.get('SliderTitle')
        slideredit.description['SliderContent']= request.POST.get('SliderContent')
        slideredit.description['update_date'] = current_time
        slideredit.description['Select_In_do']= request.POST.get('up-Select_In_do')
        slideredit.update_us= current_time
      
        if 'SliderImage' in request.FILES:
            old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image/', slideredit.description['SliderImage'])
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = request.FILES['SliderImage']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            slideredit.description['SliderImage'] = img_path

        if 'tabImage' in request.FILES:
            if slideredit.description.get('tabImage'):
                old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image/', slideredit.description.get('tabImage', ''))
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)

            new_image = request.FILES['tabImage']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            slideredit.description['tabImage'] = img_path

        if 'mobileImage' in request.FILES:
            if slideredit.description.get('mobileImage'):
                old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image/', slideredit.description.get('mobileImage', ''))
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)

            new_image = request.FILES['mobileImage']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            slideredit.description['mobileImage'] = img_path

        slideredit.save()
        return redirect('Homepage_slider')
    
   
    return render(request, 'admin/homepage/Slider_homepage.html',{"userdetails":userdetails})

def Homepage_slider_delete(request,team_id):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if role == 'data':
        return redirect('Homepage_slider')
    
    sliderdelete = HomepageSlider.objects.get(id=team_id)
    if sliderdelete.description.get('SliderImage'):
        image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image/', sliderdelete.description.get('SliderImage'))
        if os.path.exists(image_path):
            os.remove(image_path)
    if sliderdelete.description.get('tabImage', ''):
        image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image/', sliderdelete.description.get('tabImage', ''))
        if os.path.exists(image_path):
            os.remove(image_path)
    if sliderdelete.description.get('mobileImage', ''):
        image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image/', sliderdelete.description.get('mobileImage', ''))
        if os.path.exists(image_path):
            os.remove(image_path) 
    
    sliderdelete.delete()
    return redirect('Homepage_slider')

# ================================================ international top destination ==============
def Homepage_topdestination(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
        
    Destnation = Destination.objects.all()
    userdetails = adminheader(request)

    all_des = []
    for destination in Destnation:
        all_des.append({"id":destination.id,"category":destination.category,"destination_name":destination.destination_name,"destination_slug":destination.destination_slug})

    Internation = []
    Domestic = []

    # Iterate over each destination and separate them based on their category
    for destination in all_des:
        if destination['category'] == '0':
            Internation.append(destination)
        elif destination['category'] == '1':
            Domestic.append(destination)

    topdestination = PagesTable.objects.filter(pagesname='international_top_destination').first()
    about_us_details = topdestination.description
    print(about_us_details)

    do_city_list = []
    for j in Internation:
        Cities = InternationalCity.objects.filter(destination_id=j['id'])
        for City in Cities:
            do_city_list.append ({
                'id': City.id,
                'international_city_name': City.international_city_name,
             })
    
  
    package = Packages.objects.all()

    return render(request, 'admin/homepage/top_destination.html',{"package":package,'Internation':Internation,'Domestic':Domestic,"topdestination":about_us_details,"City_list":do_city_list,"userdetails":userdetails})



def Homepage_topdestination_Edit(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    userdetails = adminheader(request)
    username = request.session.get('username')
 
    topdestination_all = PagesTable.objects.filter(pagesname='international_top_destination').first()
    topdestination = topdestination_all.description
    if request.method == 'POST':
        current_time = datetime.now().strftime('%Y-%m-%d')
        topdestination['destination_1Continent'] = request.POST.get('destination_1Continent')
        topdestination['destination_2Continent'] = request.POST.get('destination_2Continent')
        topdestination['destination_3Continent'] = request.POST.get('destination_3Continent')
        topdestination['destination_4Continent'] = request.POST.get('destination_4Continent')
        topdestination['destination_1Name'] = request.POST.get('destination_1Name')
        topdestination['destination_2Name'] = request.POST.get('destination_2Name')
        topdestination['destination_3Name'] = request.POST.get('destination_3Name')
        topdestination['destination_4Name'] = request.POST.get('destination_4Name')
        topdestination['destination_1Cities'] = request.POST.get('destination_1Cities')
        topdestination['destination_2Cities'] = request.POST.get('destination_2Cities')
        topdestination['destination_3Cities'] = request.POST.get('destination_3Cities')
        topdestination['destination_4Cities'] = request.POST.get('destination_4Cities')
        topdestination['destination_1Price'] = request.POST.get('destination_1Price')
        topdestination['destination_2price'] = request.POST.get('destination_2price')
        topdestination['destination_3price'] = request.POST.get('destination_3price')
        topdestination['destination_4price'] = request.POST.get('destination_4price')
       
        topdestination_all.updated_by = current_time
        topdestination_all.updated_name = username
        # slideredit.description['LinkedInid'] = request.POST.get('upadteLinkedInid')
      
        if 'destination_1image' in request.FILES:
            old_image_path1 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination/', topdestination['destination_1image'])
            if os.path.exists(old_image_path1):
                os.remove(old_image_path1)

            new_image = request.FILES['destination_1image']
            img_path1 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination', img_path1)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_1image'] = img_path1

        if 'destination_2image' in request.FILES:
            old_image_path2 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination/', topdestination['destination_2image'])
            if os.path.exists(old_image_path2):
                os.remove(old_image_path2)

            new_image = request.FILES['destination_2image']
            img_path2 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination', img_path2)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_2image'] = img_path2

        if 'destination_3image' in request.FILES:
            old_image_path3 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination/', topdestination['destination_3image'])
            if os.path.exists(old_image_path3):
                os.remove(old_image_path3)

            new_image= request.FILES['destination_3image']
            img_path3 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination', img_path3)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_3image'] = img_path3

        if 'destination_4image' in request.FILES:
            old_image_path4 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination/', topdestination['destination_4image'])
            if os.path.exists(old_image_path4):
                os.remove(old_image_path4)

            new_image= request.FILES['destination_4image']
            img_path4 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination', img_path4)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_4image'] = img_path4

        topdestination_all.save()
        return redirect('Homepage_topdestination')
    
   
    return render(request, 'admin/homepage/Slider_homepage.html',{"userdetails":userdetails})

# ================================================ Domestic top destination ==============
def Homepage_domestic_topdestination(request):
    
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    userdetails = adminheader(request)
    Destnation = Destination.objects.all()

    all_des = []
    for destination in Destnation:
        all_des.append({"id":destination.id,"category":destination.category,"destination_name":destination.destination_name,"destination_slug":destination.destination_slug})

    Internation = []
    Domestic = []

    # Iterate over each destination and separate them based on their category
    for destination in all_des:
        if destination['category'] == '0':
            Internation.append(destination)
        elif destination['category'] == '1':
            Domestic.append(destination)

    topdestination = PagesTable.objects.filter(pagesname='domestic_top_destination').first()
    about_us_details = topdestination.description
    print(about_us_details)

    do_city_list = []
    for j in Domestic:
        Cities = InternationalCity.objects.filter(destination_id=j['id'])
        for City in Cities:
            do_city_list.append ({
                'id': City.id,
                'international_city_name': City.international_city_name,
             })
        
    
  
   
    package = Packages.objects.all()
    return render(request, 'admin/homepage/domestic_Topdestination.html',{"package":package,'Internation':Internation,'Domestic':Domestic,"topdestination":about_us_details,"City_list":do_city_list,"userdetails":userdetails})



def Homepage_domestic_topdestination_Edit(request):
    
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    userdetails = adminheader(request)
    username = request.session.get('username')
 
    topdestination_all = PagesTable.objects.filter(pagesname='domestic_top_destination').first()
    topdestination = topdestination_all.description
    if request.method == 'POST':
        current_time = datetime.now().strftime('%Y-%m-%d')
        topdestination['destination_1Continent'] = request.POST.get('destination_1Continent')
        topdestination['destination_2Continent'] = request.POST.get('destination_2Continent')
        topdestination['destination_3Continent'] = request.POST.get('destination_3Continent')
        topdestination['destination_4Continent'] = request.POST.get('destination_4Continent')
        topdestination['destination_1Name'] = request.POST.get('destination_1Name')
        topdestination['destination_2Name'] = request.POST.get('destination_2Name')
        topdestination['destination_3Name'] = request.POST.get('destination_3Name')
        topdestination['destination_4Name'] = request.POST.get('destination_4Name')
        topdestination['destination_1Cities'] = request.POST.get('destination_1Cities')
        topdestination['destination_2Cities'] = request.POST.get('destination_2Cities')
        topdestination['destination_3Cities'] = request.POST.get('destination_3Cities')
        topdestination['destination_4Cities'] = request.POST.get('destination_4Cities')
        topdestination['destination_1Price'] = request.POST.get('destination_1Price')
        topdestination['destination_2price'] = request.POST.get('destination_2price')
        topdestination['destination_3price'] = request.POST.get('destination_3price')
        topdestination['destination_4price'] = request.POST.get('destination_4price')
       
        topdestination_all.updated_by = current_time
        topdestination_all.updated_name = username
        # slideredit.description['LinkedInid'] = request.POST.get('upadteLinkedInid')
      
        if 'destination_1image' in request.FILES:
            old_image_path1 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination/', topdestination['destination_1image'])
            if os.path.exists(old_image_path1):
                os.remove(old_image_path1)

            new_image = request.FILES['destination_1image']
            img_path1 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination', img_path1)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_1image'] = img_path1

        if 'destination_2image' in request.FILES:
            old_image_path2 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination/', topdestination['destination_2image'])
            if os.path.exists(old_image_path2):
                os.remove(old_image_path2)

            new_image = request.FILES['destination_2image']
            img_path2 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination', img_path2)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_2image'] = img_path2

        if 'destination_3image' in request.FILES:
            old_image_path3 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination/', topdestination['destination_3image'])
            if os.path.exists(old_image_path3):
                os.remove(old_image_path3)

            new_image= request.FILES['destination_3image']
            img_path3 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination', img_path3)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_3image'] = img_path3

        if 'destination_4image' in request.FILES:
            old_image_path4 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination/', topdestination['destination_4image'])
            if os.path.exists(old_image_path4):
                os.remove(old_image_path4)

            new_image= request.FILES['destination_4image']
            img_path4 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/Top_destination', img_path4)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_4image'] = img_path4

        topdestination_all.save()
        return redirect('Homepage_domestic_topdestination')
    
   
    return render(request, 'admin/homepage/Slider_homepage.html',{"userdetails":userdetails})

# ======================================== destination categories ===========================

def add_categories(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if request.method == 'POST':
        Team_Name = request.POST.get('TeamName')
        Categories_Url = request.POST.get('Categories-Url')
        
        if 'CategoriesImages' in request.FILES:
            Images = request.FILES['CategoriesImages']
            img_path = Images.name
            Imagesimage_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image', img_path)
            with open(Imagesimage_path, 'wb') as destination:
                for chunk in Images.chunks():
                    destination.write(chunk)
        
     
        team = Category.objects.create(categoriesname=Team_Name,updatedate=current_time ,createdate=current_time,categeory_slug=Categories_Url,categoriesimage=img_path)
        team.save()
        return redirect('categories_view')
    else:
        return redirect('categories_view')

def categories_view(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    teams = Category.objects.all()
    return render(request, 'admin/homepage/Top Categories.html', {'form': teams,"userdetails":userdetails})

def edit_categories(request, team_id):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    team = Category.objects.get(id=team_id)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if request.method == 'POST':
        new_team_name = request.POST.get('TeamNamemodify')
        new_upCategories = request.POST.get('upCategories-Url')
        team.categoriesname = new_team_name
        team.categeory_slug = new_upCategories
        team.updatedate = current_time
        if 'upCategoriesImages' in request.FILES:
            # old_image_path4 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image/', team.categoriesimage)
            # if os.path.exists(old_image_path4):
            #     os.remove(old_image_path4)

            new_image= request.FILES['upCategoriesImages']
            img_path4 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/homepageslider_image', img_path4)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            team.categoriesimage = img_path4
        team.save()
        return redirect('categories_view')
    return redirect('categories_view')


# ======================================== categries based list the detination name ==================
# for key, value in cities_name.items():
    #     print("Key:", key)
    #     print("Value:", value)

def categories_cities(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    Destnation = Destination.objects.all()

    all_des = []
    for destination in Destnation:
        all_des.append({"id":destination.id,"category":destination.category,"destination_name":destination.destination_name})

    Internation = []
    Domestic = []

    # Iterate over each destination and separate them based on their category
    for destination in all_des:
        if destination['category'] == '0':
            Internation.append(destination)
        elif destination['category'] == '1':
            Domestic.append(destination)
    
    categories =  Category.objects.all()
    userdetails = adminheader(request)
    results = []
    categories_destination = CategoriesDestination.objects.all()

    for destination in categories_destination:
        id=destination.id
        city = destination.category
        cities_name = destination.city_id
        if destination.all_description is not None:
            metakeyword = destination.all_description.get("Metakeyword", "")
            metatitle = destination.all_description.get("MetaTitle", "")
            metadescription = destination.all_description.get("Metadescription", "")
            canonical = destination.all_description.get("canonical", "")
        else:
        # Assign default values if all_description is None
            metakeyword = ""
            metatitle = ""
            metadescription = ""
            canonical = ""

        # city_ = json.dumps(cities_name)

        # Constructing the new structure for each destination
        result = {
            "id": id,  # Assuming there's an ID field in the CategoriesDestination model
            "city": city,
            "description":json.dumps(cities_name),
            "metakeyword":metakeyword,
            "metatitle":metatitle,
            "metadescription":metadescription,
            "canonical":canonical,
            "categeory_slug":destination.categeory_slug,
                
        }
        results.append(result)
    print(results)
    # keys_array = []

    # for key in cities_name.keys():
    #     keys_array.append(key)

    # print("Keys Array:", keys_array)

    return render(request, 'admin/homepage/home_bucketlist.html',{'Internation':Internation,'Domestic':Domestic,"categories":categories,"results":results,"userdetails":userdetails})

def add_categories_cities(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    username = request.session.get('username')
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    current_time = datetime.now().strftime('%Y-%m-%d')
    if request.method == 'POST':
        Category_name = request.POST.get('CategoriesType')
        MetaTitle = request.POST.get('MetaTitle')
        Metadescription = request.POST.get('Metadescription')
        Metakeyword = request.POST.get('Metakeyword')
        canonical = request.POST.get('canonical')
        
        Category_cities = request.POST.get('selectedCities')
        Category_slug = request.POST.get('CategoriesTypeslug')

        if 'CategoriesImages' in request.FILES:
            new_image = request.FILES['CategoriesImages']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/CategoriesImages', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
        if 'TabImages' in request.FILES:
            new_image = request.FILES['TabImages']
            img_path2 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/CategoriesImages', img_path2)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
        if 'MobileImages' in request.FILES:
            new_image = request.FILES['MobileImages']
            img_path3 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/CategoriesImages', img_path3)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
        
        all_json = {
            "MetaTitle":MetaTitle,
            "Metadescription":Metadescription,
            "Metakeyword":Metakeyword,
            "canonical":canonical,
            "img_path":img_path,
            "tab_path" :img_path2,
            "Mobile_path" :img_path3,
        }


        parsed_data = json.loads(Category_cities)
       
        destination = CategoriesDestination(category=Category_name, city_id=parsed_data,create_date=current_time,update_date=current_time,categeory_slug=Category_slug,all_description=all_json,updated_name=username,created_name=username)
        destination.save()
        return redirect('categories_cities')
    else:
        return redirect('categories_cities')

   

def edit_categories_cities(request,team_id):
      # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    Ccity= CategoriesDestination.objects.get(id=team_id)
    current_time = datetime.now().strftime('%Y-%m-%d')
    username = request.session.get('username')
    if request.method == 'POST':
    
        Ccity.category = request.POST.get('up-CategoriesType')
        Ccity.categeory_slug = request.POST.get('up-CategoriesTypeslug')
        Ccity.city_id = json.loads(request.POST.get('uptwo-selectedCities'))
        Ccity.all_description["Metakeyword"] = request.POST.get('up-Metakeywork')
        Ccity.all_description["MetaTitle"]= request.POST.get('up-MetaTitle')
        Ccity.all_description["Metadescription"] = request.POST.get('up-Metadescription')
        Ccity.all_description["canonical"] = request.POST.get('canonical')
        Ccity.update_date = current_time
        Ccity.updated_name = username

        if 'up-CategoriesImages' in request.FILES:
            old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/CategoriesImages/', Ccity.all_description['img_path'])
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = request.FILES['up-CategoriesImages']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/CategoriesImages', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            Ccity.all_description['img_path'] = img_path
        if 'up-TabImages' in request.FILES:
            old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/CategoriesImages/', Ccity.all_description['tab_path'])
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = request.FILES['up-TabImages']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/CategoriesImages', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
            Ccity.all_description['tab_path'] = img_path
        if 'up-MobileImages' in request.FILES:
            
            old_image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/CategoriesImages/', Ccity.all_description['Mobile_path'])
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = request.FILES['up-MobileImages']
            img_path = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/CategoriesImages', img_path)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)

            Ccity.all_description['Mobile_path'] = img_path
        Ccity.save()
        return redirect('categories_cities')
    return redirect('categories_cities')


def delete_categories_cities(request,team_id):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if role == 'data':
        return redirect('categories_cities')
    
    Catagriescitydelete = CategoriesDestination.objects.get(id=team_id)
    if Catagriescitydelete.all_description.get('img_path'):
        image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/CategoriesImages/', Catagriescitydelete.all_description.get('img_path'))
        if os.path.exists(image_path):
            os.remove(image_path) 
    
    Catagriescitydelete.delete()

    return redirect('categories_cities')
# Footer 
def footer(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    footer_headers = FooterHeader.objects.all()
    footer_title = FooterTitle.objects.all()
    search_query = request.GET.get('search_query')

    if search_query:
            footer_title = footer_title.filter(description__Header__icontains=search_query)

    paginator = Paginator(footer_title, 10)  # Show 5 blog entries per page

    page = request.GET.get('page')
    try:
        footer_title = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        footer_title = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        footer_title = paginator.page(paginator.num_pages)

    
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    return render(request, 'admin/footer.html',{"footer_headers":footer_headers,"footer_title":footer_title,"userdetails":userdetails})

def addheaderfooter(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    username = request.session.get('username')
    role = request.session.get('role')
    userdetails = adminheader(request)
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M")
    # current_time_str = current_time.strftime("%b %d, %Y")

    current_date_str = datetime.now().strftime("%d/%m/%Y")
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')

    if request.method == 'POST':
        Header = request.POST.get('Header', '')
        URL = request.POST.get('URL', '')

        footer_main = FooterHeader.objects.create()
        updated_by =  f"{username} {current_date_str}"   # Assuming you have authentication and can access the current user
        created_by =  f"{username} {current_date_str}"

        description = {"Header":Header,
                       "URL":URL,  # Assuming you have authentication and can access the current user
                "updated_on": current_date_str,   # Assuming you have authentication and can access the current user
                "created_on": current_date_str,}
        


        footer_main.header = description
        footer_main.created_by = created_by
        footer_main.updated_by = updated_by

        footer_main.save()

        return redirect('footer')
    
    return redirect('footer')

def updateheader(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    username = request.session.get('username')
    role = request.session.get('role')
    userdetails = adminheader(request)
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M")
    # current_time_str = current_time.strftime("%b %d, %Y")

    current_date_str = datetime.now().strftime("%d/%m/%Y")
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')

    if request.method == 'POST':
        id = request.POST.get('id', '')
        Header = request.POST.get('Header', '')
        URL = request.POST.get('URL', '')

        footer = FooterHeader.objects.get(id=id)
        description = footer.header
        created_by = description.get('created_by', None)
        created_on = description.get('created_on', None)

        description = {"Header":Header,
                       "URL":URL,  # Assuming you have authentication and can access the current user
                "updated_on": current_date_str,   # Assuming you have authentication and can access the current user
                "created_on": created_on}
        
        footer.updated_by =  f"{username} {current_date_str}"
        
        footer.header = description

        footer.save()

        return redirect('footer')
    
    return redirect('footer')

def deletefooterheader(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    username = request.session.get('username')
    role = request.session.get('role')
    userdetails = adminheader(request)
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M")
    # current_time_str = current_time.strftime("%b %d, %Y")

    current_date_str = datetime.now().strftime("%d/%m/%Y")
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if role == 'data':
        return redirect('footer')

    if request.method == 'GET':
        ids = request.GET.get('id', '')

        # Retrieve the FooterHeader object based on the id
        footer_header_object = FooterHeader.objects.get(id=ids)
        
        # Delete the object
        footer_header_object.delete()
        return redirect('footer')
    
    return redirect('footer')
    

def addtitlefooter (request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    username = request.session.get('username')
    role = request.session.get('role')
    userdetails = adminheader(request)
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M")
    # current_time_str = current_time.strftime("%b %d, %Y")

    current_date_str = datetime.now().strftime("%d/%m/%Y")
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')

    if request.method == 'POST':
        title = request.POST.get('title', '')
        URL = request.POST.get('URL', '')
        header = request.POST.get('selectedHeader', '')
        header_id = request.POST.get('selectedHeaderId', '')

        

        footer_main = FooterTitle.objects.create()

        description = {"title":title,
                    "Header":header,
                       "URL":URL,   # Assuming you have authentication and can access the current user
                "updated_on": current_date_str,   # Assuming you have authentication and can access the current user
                "created_on": current_date_str,}
        
        footer_main.description = description
        footer_main.header_id = header_id
        footer_main.created_by = f"{username} {current_date_str}"
        footer_main.updated_by =  f"{username} {current_date_str}"
        footer_main.save()

        return redirect('footer')
    
    return redirect('footer')

def updatetitlefooter (request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    username = request.session.get('username')
    role = request.session.get('role')
    userdetails = adminheader(request)
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M")
    # current_time_str = current_time.strftime("%b %d, %Y")

    current_date_str = datetime.now().strftime("%d/%m/%Y")
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')

    if request.method == 'POST':
        ids = request.POST.get('id', '')
        title = request.POST.get('title', '')
        URL = request.POST.get('URL', '')
        header = request.POST.get('selectedHeader', '')
        header_id = request.POST.get('selectedHeaderId', '')

        footer_title = FooterTitle.objects.get(id=ids)
        description = footer_title.description
        created_by = description.get('created_by', None)
        created_on = description.get('created_on', None)

        description = {
            "title":title,
                "Header":header,
                "URL":URL,   # Assuming you have authentication and can access the current user
                "updated_on": current_date_str,  # Assuming you have authentication and can access the current user
                "created_on": created_on
                }
        
        footer_title.description = description
        footer_title.header_id = header_id
        footer_title.updated_by =  f"{username} {current_date_str}"
        footer_title.save()

        return redirect('footer')
    
    return redirect('footer')
    
def deletefootertitle(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    username = request.session.get('username')
    role = request.session.get('role')
    userdetails = adminheader(request)
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M")
    # current_time_str = current_time.strftime("%b %d, %Y")

    current_date_str = datetime.now().strftime("%d/%m/%Y")
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if role == 'data':
        return redirect('footer')

    if request.method == 'GET':
        ids = request.GET.get('id', '')

        # Retrieve the FooterHeader object based on the id
        footer_header_object = FooterTitle.objects.get(id=ids)
        
        # Delete the object
        footer_header_object.delete()
        return redirect('footer')
    
    return redirect('footer')
    
    
def Continent_Metas(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    Contient_page = ContinentMetas.objects.all()
    
    return render(request, 'admin/destination/continent_meta.html',{"Contient_page":Contient_page,"userdetails":userdetails})
    
def Continent_Metas_edit(request,team_id):
    # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    Contient = ContinentMetas.objects.get(id=team_id)
    current_date_time = timezone.now()

    # Format the current date and time to the required format
    # formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        Contient.description_son['meta_title'] = request.POST.get('meta_title')
        Contient.description_son['meta_keyword'] = request.POST.get('meta_keyword')
        Contient.description_son['meta_description'] = request.POST.get('meta_description')
        Contient.description_son['canonical'] = request.POST.get('canonical')
        Contient.Update_at = current_date_time

    Contient.save()
    return redirect('Continent_Metas')
    
def destination_Metas(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    Meta_page = DestinationMeta.objects.all()
    
    return render(request, 'admin/destination/destination_meta.html',{"Meta_page":Meta_page,'userdetails':userdetails})

def destination_Metas_edit(request,team_id):
    # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    Contient = DestinationMeta.objects.get(id=team_id)
    current_date_time = timezone.now()


    if request.method == 'POST':
        Contient.meta_details['meta_title'] = request.POST.get('MetaTitle')
        Contient.meta_details['meta_keyword'] = request.POST.get('MetaKeyword')
        Contient.meta_details['meta_description'] = request.POST.get('Metadescription')
        Contient.meta_details['canonical'] = request.POST.get('canonical')
        Contient.update_at = current_date_time

    Contient.save()
    return redirect('destination_Metas')
    
def update_packages_category_state(request):
    # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        new_state = request.POST.get('new_state') == 'on'

        blog = Packages.objects.get(id=blog_id)
        blog.category_button = int(not new_state)  # Convert new_state to int (0 or 1)
        blog.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

# ADD USER
def adduser (request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    username = request.session.get('username')
    role = request.session.get('role')
    userdetails = adminheader(request)
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M")
    # current_time_str = current_time.strftime("%b %d, %Y")

    if role != 'superadmin':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    teams = UserTable.objects.all()

    return render(request, 'admin/adduser.html',{"teams":teams,'userdetails':userdetails})
    

def add_user(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    username = request.session.get('username')
    role = request.session.get('role')
    userdetails = adminheader(request)
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M")
    # current_time_str = current_time.strftime("%b %d, %Y")

    if role != 'superadmin':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    if request.method == 'POST':
        team_name = request.POST.get('TeamName')
        department = request.POST.get('Department')
        role = request.POST.get('Role')
        password = request.POST.get('password')

        # Create and save UserTable instance
        user = UserTable(username=team_name, department=department, role=role, password=password)
        user.save()

        # Redirect to a success page or return a success message
        return redirect('adduser')
    else:
        return redirect('adduser')
    
def edit_user(request, team_id):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'superadmin':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    team = UserTable.objects.get(id=team_id)
    if request.method == 'POST':
        new_team_name = request.POST.get('TeamName')
        Role = request.POST.get('Role')
        Password = request.POST.get('password')
        department = request.POST.get('Department')
        team.username = new_team_name
        team.department = department
        team.role = Role
        team.password = Password
        team.save()
        return redirect('adduser')
    return redirect('adduser')


def deleteuser(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'superadmin':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    if role == 'data':
        return redirect('adduser')
    ids = request.GET.get('id', '')
    review = UserTable.objects.get(id=ids)
    review.delete()
    return redirect('adduser')

from VFpages.models import HomepageTheme;

def Homepage2_international(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
        
    Destnation = Destination.objects.all()
    userdetails = adminheader(request)

    all_des = []
    for destination in Destnation:
        all_des.append({"id":destination.id,"category":destination.category,"destination_name":destination.destination_name,"destination_slug":destination.destination_slug})

    Internation = []
    Domestic = []

    # Iterate over each destination and separate them based on their category
    for destination in all_des:
        if destination['category'] == '0':
            Internation.append(destination)
        elif destination['category'] == '1':
            Domestic.append(destination)

    topdestination = PagesTable.objects.filter(pagesname='international_top_destination_2').first()
    about_us_details = topdestination.description
    print(about_us_details)

    do_city_list = []
    for j in Internation:
        Cities = InternationalCity.objects.filter(destination_id=j['id'])
        for City in Cities:
            do_city_list.append ({
                'id': City.id,
                'international_city_name': City.international_city_name,
             })
    package = Packages.objects.all()
  
   

    return render(request, 'admin/homepage2/international_destination2.html',{'Internation':Internation,'Domestic':Domestic,"topdestination":about_us_details,"City_list":do_city_list,"userdetails":userdetails,"package":package})

def Homepage2_domestic(request):
    
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    userdetails = adminheader(request)
    Destnation = Destination.objects.all()

    all_des = []
    for destination in Destnation:
        all_des.append({"id":destination.id,"category":destination.category,"destination_name":destination.destination_name,"destination_slug":destination.destination_slug})

    Internation = []
    Domestic = []

    # Iterate over each destination and separate them based on their category
    for destination in all_des:
        if destination['category'] == '0':
            Internation.append(destination)
        elif destination['category'] == '1':
            Domestic.append(destination)

    topdestination = PagesTable.objects.filter(pagesname='domestic_top_destination_2').first()
    about_us_details = topdestination.description
    print(about_us_details)

    do_city_list = []
    for j in Domestic:
        Cities = InternationalCity.objects.filter(destination_id=j['id'])
        for City in Cities:
            do_city_list.append ({
                'id': City.id,
                'international_city_name': City.international_city_name,
             })
        
    package = Packages.objects.all()
  
   

    return render(request, 'admin/homepage2/domestic_Topdestination2.html',{'Internation':Internation,'Domestic':Domestic,"topdestination":about_us_details,"City_list":do_city_list,"userdetails":userdetails,"package":package})




def home_page_details(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    userdetails = adminheader(request)
    home1_details = PagesTable.objects.filter(pagesname='home_page_2').first()
    home2_inter = PagesTable.objects.filter(pagesname='international_top_destination_2').first()
    home2_domes = PagesTable.objects.filter(pagesname='domestic_top_destination_2').first()
    
    Destnation = Destination.objects.all()

    all_des = []
    for destination in Destnation:
        all_des.append({"id":destination.id,"category":destination.category,"destination_name":destination.destination_name,"destination_slug":destination.destination_slug})

    Internation = []
    Domestic = []

    # Iterate over each destination and separate them based on their category
    for destination in all_des:
        if destination['category'] == '0':
            Internation.append(destination)
        elif destination['category'] == '1':
            Domestic.append(destination)
    

    return render(request,'admin/homepage2/home_details.html',{"home1_details":home1_details,"home2_inter":home2_inter,"home2_domes":home2_domes,"userdetails":userdetails,"Internation":Internation,"Domestic":Domestic})


def home_page2_Edit(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    userdetails = adminheader(request)
    username =request.session.get('username')
 
    homepage_detrails = PagesTable.objects.filter(pagesname='home_page_2').first()
    topdestination = homepage_detrails.description
    if request.method == 'POST':
        current_time = datetime.now().strftime('%Y-%m-%d')
        topdestination['banner_title'] = request.POST.get('banner_title')
        topdestination['big_v_title'] = request.POST.get('big_v_title')
        topdestination['big_v_heading'] = request.POST.get('big_v_heading')
        topdestination['small_v_heading'] = request.POST.get('small_v_heading')
        topdestination['small_v_title'] = request.POST.get('small_v_title')
        topdestination['small_v_para'] = request.POST.get('small_v_para')
        topdestination['big_v_destination'] = request.POST.get('big_v_destination')
        topdestination['small_v_destination'] = request.POST.get('small_v_destination')
        
        homepage_detrails.updated_by = current_time
        homepage_detrails.updated_name = username 

      
        if 'banner_image' in request.FILES:
            old_image_path1 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/main_details/', topdestination['banner_image'])
            if os.path.exists(old_image_path1):
                os.remove(old_image_path1)

            new_image = request.FILES['banner_image']
            img_path1 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/main_details', img_path1)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['banner_image'] = img_path1
            
        if 'tab_image' in request.FILES:
            old_image_path1 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/main_details/', topdestination['tab_image'])
            if os.path.exists(old_image_path1):
                os.remove(old_image_path1)

            new_image = request.FILES['tab_image']
            img_path1 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/main_details', img_path1)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['tab_image'] = img_path1
        if 'Mobile_image' in request.FILES:
            old_image_path1 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/main_details/', topdestination['Mobile_image'])
            if os.path.exists(old_image_path1):
                os.remove(old_image_path1)

            new_image = request.FILES['Mobile_image']
            img_path1 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/main_details', img_path1)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['Mobile_image'] = img_path1

        if 'review_banner_image' in request.FILES:
            old_image_path4 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/main_details/', topdestination['review_banner_image'])
            if os.path.exists(old_image_path4):
                os.remove(old_image_path4)

            new_image = request.FILES['review_banner_image']
            img_path4 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/main_details', img_path4)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['review_banner_image'] = img_path4

        if 'big_video' in request.FILES:
            old_image_path2 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/main_details/', topdestination['big_video'])
            if os.path.exists(old_image_path2):
                os.remove(old_image_path2)

            new_image = request.FILES['big_video']
            img_path2 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/main_details', img_path2)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['big_video'] = img_path2

        if 'small_video' in request.FILES:
            old_image_path3 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/main_details/', topdestination['small_video'])
            if os.path.exists(old_image_path3):
                os.remove(old_image_path3)

            new_image= request.FILES['small_video']
            img_path3 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/main_details', img_path3)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['small_video'] = img_path3

        

        homepage_detrails.save()

        return redirect('home_page_details')
    
   
    return render(request,'admin/homepage2/home_details.html',{"userdetails":userdetails})

def Homepage2_international_Edit(request):
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    userdetails = adminheader(request)
    username = request.session.get('username')
 
    topdestination_all = PagesTable.objects.filter(pagesname='international_top_destination_2').first()
    topdestination = topdestination_all.description
    if request.method == 'POST':
        current_time = datetime.now().strftime('%Y-%m-%d')
        topdestination['destination_1Continent'] = request.POST.get('destination_1Continent')
        topdestination['destination_2Continent'] = request.POST.get('destination_2Continent')
        topdestination['destination_3Continent'] = request.POST.get('destination_3Continent')
        topdestination['destination_4Continent'] = request.POST.get('destination_4Continent')
        topdestination['destination_4Continent'] = request.POST.get('destination_4Continent')
        topdestination['destination_5Continent'] = request.POST.get('destination_5Continent')
        topdestination['destination_1Name'] = request.POST.get('destination_1Name')
        topdestination['destination_2Name'] = request.POST.get('destination_2Name')
        topdestination['destination_3Name'] = request.POST.get('destination_3Name')
        topdestination['destination_4Name'] = request.POST.get('destination_4Name')
        topdestination['destination_5Name'] = request.POST.get('destination_5Name')
        topdestination['destination_1Cities'] = request.POST.get('destination_1Cities')
        topdestination['destination_2Cities'] = request.POST.get('destination_2Cities')
        topdestination['destination_3Cities'] = request.POST.get('destination_3Cities')
        topdestination['destination_4Cities'] = request.POST.get('destination_4Cities')
        topdestination['destination_5Cities'] = request.POST.get('destination_5Cities')
        topdestination['destination_1Price'] = request.POST.get('destination_1Price')
        topdestination['destination_2price'] = request.POST.get('destination_2price')
        topdestination['destination_3price'] = request.POST.get('destination_3price')
        topdestination['destination_4price'] = request.POST.get('destination_4price')
        topdestination['destination_5price'] = request.POST.get('destination_5price')
       
        topdestination_all.updated_by = current_time
        topdestination_all.updated_name = username
        # slideredit.description['LinkedInid'] = request.POST.get('upadteLinkedInid')
      
        if 'destination_1image' in request.FILES:
            old_image_path1 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations/', topdestination['destination_1image'])
            if os.path.exists(old_image_path1):
                os.remove(old_image_path1)

            new_image = request.FILES['destination_1image']
            img_path1 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations', img_path1)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_1image'] = img_path1

        if 'destination_2image' in request.FILES:
            old_image_path2 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations/', topdestination['destination_2image'])
            if os.path.exists(old_image_path2):
                os.remove(old_image_path2)

            new_image = request.FILES['destination_2image']
            img_path2 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations', img_path2)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_2image'] = img_path2

        if 'destination_3image' in request.FILES:
            old_image_path3 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations/', topdestination['destination_3image'])
            if os.path.exists(old_image_path3):
                os.remove(old_image_path3)

            new_image= request.FILES['destination_3image']
            img_path3 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations', img_path3)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_3image'] = img_path3

        if 'destination_4image' in request.FILES:
            old_image_path4 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations/', topdestination['destination_4image'])
            if os.path.exists(old_image_path4):
                os.remove(old_image_path4)

            new_image= request.FILES['destination_4image']
            img_path4 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations', img_path4)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_4image'] = img_path4

        if 'destination_5image' in request.FILES:
            old_image_path5 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations/', topdestination['destination_5image'])
            if os.path.exists(old_image_path5):
                os.remove(old_image_path5)

            new_image= request.FILES['destination_5image']
            img_path5 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations', img_path5)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_5image'] = img_path5

        topdestination_all.save()

        return redirect('home_page_details')
    
   
    return render(request,'admin/homepage2/international_destination2.html',{"userdetails":userdetails})


def Homepage2_topdomestic_Edit(request):
    
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    
    if role != 'admin' and role != 'superadmin' and role != 'employee':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    userdetails = adminheader(request)
    username = request.session.get('username')
 
    topdestination_all = PagesTable.objects.filter(pagesname='domestic_top_destination_2').first()
    topdestination = topdestination_all.description
    if request.method == 'POST':
        current_time = datetime.now().strftime('%Y-%m-%d')
        topdestination['destination_1Continent'] = request.POST.get('destination_1Continent')
        topdestination['destination_2Continent'] = request.POST.get('destination_2Continent')
        topdestination['destination_3Continent'] = request.POST.get('destination_3Continent')
        topdestination['destination_4Continent'] = request.POST.get('destination_4Continent')
        topdestination['destination_5Continent'] = request.POST.get('destination_5Continent')
        topdestination['destination_1Name'] = request.POST.get('destination_1Name')
        topdestination['destination_2Name'] = request.POST.get('destination_2Name')
        topdestination['destination_3Name'] = request.POST.get('destination_3Name')
        topdestination['destination_4Name'] = request.POST.get('destination_4Name')
        topdestination['destination_5Name'] = request.POST.get('destination_5Name')
        topdestination['destination_1Cities'] = request.POST.get('destination_1Cities')
        topdestination['destination_2Cities'] = request.POST.get('destination_2Cities')
        topdestination['destination_3Cities'] = request.POST.get('destination_3Cities')
        topdestination['destination_4Cities'] = request.POST.get('destination_4Cities')
        topdestination['destination_5Cities'] = request.POST.get('destination_5Cities')
        topdestination['destination_1Price'] = request.POST.get('destination_1Price')
        topdestination['destination_2price'] = request.POST.get('destination_2price')
        topdestination['destination_3price'] = request.POST.get('destination_3price')
        topdestination['destination_4price'] = request.POST.get('destination_4price')
        topdestination['destination_5price'] = request.POST.get('destination_5price')
       
        topdestination_all.updated_by =current_time
        topdestination_all.updated_name =username
        # slideredit.description['LinkedInid'] = request.POST.get('upadteLinkedInid')
      
        if 'destination_1image' in request.FILES:
            old_image_path1 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations/', topdestination['destination_1image'])
            if os.path.exists(old_image_path1):
                os.remove(old_image_path1)

            new_image = request.FILES['destination_1image']
            img_path1 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations', img_path1)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_1image'] = img_path1

        if 'destination_2image' in request.FILES:
            old_image_path2 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations/', topdestination['destination_2image'])
            if os.path.exists(old_image_path2):
                os.remove(old_image_path2)

            new_image = request.FILES['destination_2image']
            img_path2 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations', img_path2)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_2image'] = img_path2

        if 'destination_3image' in request.FILES:
            old_image_path3 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations/', topdestination['destination_3image'])
            if os.path.exists(old_image_path3):
                os.remove(old_image_path3)

            new_image= request.FILES['destination_3image']
            img_path3 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations', img_path3)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_3image'] = img_path3

        if 'destination_4image' in request.FILES:
            old_image_path4 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations/', topdestination['destination_4image'])
            if os.path.exists(old_image_path4):
                os.remove(old_image_path4)

            new_image= request.FILES['destination_4image']
            img_path4 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations', img_path4)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_4image'] = img_path4

        if 'destination_5image' in request.FILES:
            old_image_path5 = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations/', topdestination['destination_5image'])
            if os.path.exists(old_image_path5):
                os.remove(old_image_path5)

            new_image= request.FILES['destination_5image']
            img_path5 = new_image.name
            image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/image/home_2/topDestinations', img_path5)
            with open(image_path, 'wb') as destination:
                for chunk in new_image.chunks():
                    destination.write(chunk)
           
            topdestination['destination_5image'] = img_path5

        topdestination_all.save()
        return redirect('home_page_details')
    
   
    return render(request, 'admin/homepage/Slider_homepage.html',{"userdetails":userdetails})
    
def defalut_home_page(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    themes = HomepageTheme.objects.filter(themename='Selected theme').first()
    theme = themes.themevalue
    return render(request,'admin/homepage2/select_page.html',{"theme":theme})

def update_homepage_theme(request):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'admin' and role != 'superadmin':
        # Redirect to appropriate page if the role is not admin
        return redirect('dashboard')
    
    if request.method == 'POST':
        selectedTheme = request.POST.get('selectedTheme')
        themes = HomepageTheme.objects.filter(themename='Selected theme').first()
        themes.themevalue = selectedTheme  
        themes.save()

        return redirect('defalut_home_page')
        
from VFpages.models import Uploadhotel;


def addhotel(request,search_query):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'Sales' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    
    if request.method == 'POST':
        # Get form data
        phone_number = request.POST.get('Phonenumber')
        hotel_name = request.POST.get('Hotel')
        confirmation_number = request.POST.get('Confirmation')  # Assuming you have a field for this in your form
        check_in = request.POST.get('checkin')
        check_out = request.POST.get('checkout')
        no_of_nights = request.POST.get('Noofnights')
        room_type = request.POST.get('Room')
        # attachment = request.FILES.get('attachmentfiles')  # Assuming you have a file field in your form
        print(request.FILES)

        uploadhotel_ = Uploadhotel.objects.all()


        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/hotelvoucher', current_date)
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            uploadhotel_= os.path.join(current_date, uploaded_file.name)
        else:
            uploadhotel_=None

        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
            

        # Create and save instance
        uploadhotel_instance = Uploadhotel(
            phone_number=phone_number,
            hotel_name=hotel_name,
            confirmation_number=confirmation_number,
            check_in=check_in,
            check_out=check_out,
            no_of_nights=no_of_nights,
            room_type=room_type,
            created_by = date_object,
            updated_by = date_object,
            uplotername = username,
            editername = username,
            attachment = uploadhotel_,
        )
        uploadhotel_instance.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query)  # Replace '/success-url/' with your actual success URL

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'your_template.html')

def edithotel(request,id,search_query):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'Sales' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    

    hotel_ = Uploadhotel.objects.filter(id=id)
    print(hotel_)
    return render(request, 'admin/UserCMS/hoteledit.html',{"userdetails":userdetails,"hotel_d":hotel_,"search_query":search_query})

def editmainhotel(request,id,search_query):
    if request.method == 'POST':
        phone_number = request.POST.get('Phonenumber')
        hotel_name = request.POST.get('Hotel')
        confirmation_number = request.POST.get('Confirmation')
        check_in = request.POST.get('checkin')
        check_out = request.POST.get('checkout')
        no_of_nights = request.POST.get('Noofnights')
        room_type = request.POST.get('Room')
        hotel = Uploadhotel.objects.filter(id=id).first()

        # Check if a new file is uploaded
        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Delete the previously uploaded file if it exists
            if hotel.attachment:
                file_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/hotelvoucher', hotel.attachment)
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            parts = hotel.attachment.split('\\')
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/hotelvoucher', parts[0])
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            # Set the attachment field to the relative file path including the current date
            hotel.attachment = os.path.join(current_date, uploaded_file.name)

        # Update other fields
        hotel.phone_number = phone_number
        hotel.hotel_name = hotel_name
        hotel.confirmation_number = confirmation_number
        hotel.check_in = check_in
        hotel.check_out = check_out
        hotel.no_of_nights = no_of_nights
        hotel.room_type = room_type
        
        # Update the updated_by field
        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
        hotel.updated_by = date_object
        hotel.editername = username
        # Save the updated instance
        hotel.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query)
  # Replace 'hoteladmin' with your actual success URL name

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'hotel.html', {'hotel': hotel})

from VFpages.models import UploadFlight ,UploadTransfers, UploadUserdetails;


def addflight(request,search_query):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'Sales' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    
    if request.method == 'POST':
        # Get form data
        phone_number = request.POST.get('Phonenumber')
        # hotel_name = request.POST.get('Hotel')
        pnr_number = request.POST.get('Confirmation')  # Assuming you have a field for this in your form
        travel_date = request.POST.get('checkin')
        return_date = request.POST.get('checkout')
        baggage = request.POST.get('Noofnights')
        sector = request.POST.get('Room')
        flight_name = request.POST.get('FlightName')
        # attachment = request.FILES.get('attachmentfiles')  # Assuming you have a file field in your form
        print(request.FILES)

        uploadhotel_ = UploadFlight.objects.all()


        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/flightvoucher', current_date)
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            uploadhotel_= os.path.join(current_date, uploaded_file.name)

        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
            

        # Create and save instance
        uploadhotel_instance = UploadFlight(
            phone_number=phone_number,
            baggage=baggage,
            pnr_number=pnr_number,
            traveldate=travel_date,
            returendate=return_date,
            # no_of_nights=no_of_nights,
            sector=sector,
            created_by = date_object,
            updated_by = date_object,
            uplodername = username,
            editername = username,
            ticketattachment = uploadhotel_,
            flight_name = flight_name,
        )
        uploadhotel_instance.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query)  # Replace '/success-url/' with your actual success URL

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'your_template.html')

def editflight(request,id,search_query):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'Sales' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    

    hotel_ = UploadFlight.objects.filter(id=id)
    print(hotel_)
    return render(request, 'admin/UserCMS/flightedit.html',{"userdetails":userdetails,"hotel_d":hotel_,"search_query":search_query})

def editmainflight(request,id,search_query):
    if request.method == 'POST':
        phone_number = request.POST.get('Phonenumber')
        # hotel_name = request.POST.get('Hotel')
        pnr_number = request.POST.get('Confirmation')
        travel_date = request.POST.get('checkin')
        return_date = request.POST.get('checkout')
        baggage = request.POST.get('Noofnights')
        sector = request.POST.get('Room')
        flight_name = request.POST.get('FlightName')
        
        hotel = UploadFlight.objects.filter(id=id).first()
       
        # Check if a new file is uploaded
        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Delete the previously uploaded file if it exists
            if hotel.ticketattachment:
                file_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/flightvoucher', hotel.ticketattachment)
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            parts = hotel.ticketattachment.split('\\')
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/flightvoucher', parts[0])
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            # Set the attachment field to the relative file path including the current date
            hotel.ticketattachment = os.path.join(current_date, uploaded_file.name)

        # Update other fields
        hotel.phone_number = phone_number
        # hotel.hotel_name = hotel_name
        hotel.pnr_number = pnr_number
        hotel.traveldate = travel_date
        hotel.returendate = return_date
        hotel.baggage = baggage
        hotel.sector = sector
        hotel.flight_name = flight_name
        
        # Update the updated_by field
        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
        hotel.updated_by = date_object
        hotel.editername = username
        
        # Save the updated instance
        hotel.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query)

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'flight.html', {'hotel': hotel})



def addtrans(request,search_query):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'Sales' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    
    if request.method == 'POST':
        # Get form data
        phone_number = request.POST.get('Phonenumber')
        # hotel_name = request.POST.get('Hotel')
        From = request.POST.get('From')  # Assuming you have a field for this in your form
        TO = request.POST.get('TO')
        traveldate = request.POST.get('checkin')
        xxxxxx = request.POST.get('Noofnights')
        yyyyyyy = request.POST.get('Room')
        # attachment = request.FILES.get('attachmentfiles')  # Assuming you have a file field in your form
        print(request.FILES)

        uploadhotel_ = UploadTransfers.objects.all()


        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/transfers', current_date)
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            uploadhotel_= os.path.join(current_date, uploaded_file.name)

        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
            

        # Create and save instance
        uploadhotel_instance = UploadTransfers(
            phone_number=phone_number,
            traveldate=traveldate,
            datas={"From":From,"TO":TO,"data1":xxxxxx,"data2":yyyyyyy,"attachment":uploadhotel_},
            created_by = date_object,
            updated_by = date_object,
            uplodername = username,
            editername = username
          
        )
        uploadhotel_instance.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query)  # Replace '/success-url/' with your actual success URL

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'your_template.html')

def editmaintransfer(request,id,search_query):
    if request.method == 'POST':
        phone_number = request.POST.get('Phonenumber')
        # hotel_name = request.POST.get('Hotel')
        From = request.POST.get('From')  # Assuming you have a field for this in your form
        TO = request.POST.get('TO')
        traveldate = request.POST.get('checkin')
        xxxxxx = request.POST.get('Noofnights')
        yyyyyyy = request.POST.get('Room')
        hotel = UploadTransfers.objects.filter(id=id).first()

        # Check if a new file is uploaded
        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Delete the previously uploaded file if it exists
            if hotel.datas['attachment']:
                file_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/transfers', hotel.datas['attachment'])
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            parts = hotel.datas['attachment'].split('\\')
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/transfers', parts[0])
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            # Set the attachment field to the relative file path including the current date
            hotel.datas['attachment'] = os.path.join(current_date, uploaded_file.name)

        # Update other fields
        hotel.phone_number = phone_number
        hotel.traveldate = traveldate
        hotel.datas['From']=From
        hotel.datas['TO']=TO
        hotel.datas['data1']=xxxxxx
        hotel.datas['data2']=yyyyyyy

        # Update the updated_by field
        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
        hotel.updated_by = date_object
        hotel.editername = username
        
        # Save the updated instance
        hotel.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query)  # Replace 'hoteladmin' with your actual success URL name

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'transfers.html', {'hotel': hotel})



def addticket(request,search_query):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'Sales' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    
    if request.method == 'POST':
        # Get form data
        phone_number = request.POST.get('Phonenumber')
        filed1 = request.POST.get('From')
        traveldate = request.POST.get('checkin')
        enddate = request.POST.get('checkout')
        filed2 = request.POST.get('Noofnights')
        print(request.FILES)

        uploadhotel_ = UploadUserdetails.objects.all()


        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/tickets', current_date)
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            uploadhotel_= os.path.join(current_date, uploaded_file.name)
        else:
            uploadhotel_=None


        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
            

        # Create and save instance
        uploadhotel_instance = UploadUserdetails(
            phone_number=phone_number,
            tickets={"filed1":filed1,"filed2":filed2,"traveldate":traveldate,"enddate":enddate,"attachment":uploadhotel_},
            created_by = date_object,
            updated_by = date_object,
            uplodername = username,
            editername = username,
          
        )
        uploadhotel_instance.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query) # Replace '/success-url/' with your actual success URL

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'your_template.html')

def editmainticket(request,id,search_query):
    if request.method == 'POST':
        phone_number = request.POST.get('Phonenumber')
        filed1 = request.POST.get('From')
        traveldate = request.POST.get('checkin')
        enddate = request.POST.get('checkout')
        filed2 = request.POST.get('Noofnights')
        hotel = UploadUserdetails.objects.filter(id=id).first()

        # Check if a new file is uploaded
        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Delete the previously uploaded file if it exists
            if hotel.tickets['attachment']:
                file_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/tickets', hotel.tickets['attachment'])
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            parts = hotel.tickets['attachment'].split('\\')
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/tickets', parts[0])
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            # Set the attachment field to the relative file path including the current date
            hotel.tickets['attachment'] = os.path.join(current_date, uploaded_file.name)

        # Update other fields
        hotel.phone_number = phone_number
        hotel.tickets['traveldate'] = traveldate
        hotel.tickets['enddate'] = enddate
        hotel.tickets['filed1']=filed1
        hotel.tickets['filed2']=filed2


        # Update the updated_by field
        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
        hotel.updated_by = date_object
        hotel.editername = username
        
        # Save the updated instance
        hotel.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query)  # Replace 'hoteladmin' with your actual success URL name

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'transfers.html', {'hotel': hotel})



def addvisa(request,search_query):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'Sales' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    
    if request.method == 'POST':
        # Get form data
        phone_number = request.POST.get('Phonenumber')
        filed1 = request.POST.get('From')
        filed2 = request.POST.get('TO')
        filed3 = request.POST.get('Noofnights')
        checkout = request.POST.get('checkout')
        print(request.FILES)

        uploadhotel_ = UploadUserdetails.objects.all()


        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/visa', current_date)
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            uploadhotel_= os.path.join(current_date, uploaded_file.name)
        else:
            uploadhotel_=None

        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
            

        # Create and save instance
        uploadhotel_instance = UploadUserdetails(
            phone_number=phone_number,
            visa={"filed1":filed1,"filed2":filed2,"filed3":filed3,"attachment":uploadhotel_,"checkout":checkout},
            created_by = date_object,
            updated_by = date_object,
            uplodername = username,
            editername = username,
          
        )
        uploadhotel_instance.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query)  # Replace '/success-url/' with your actual success URL

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'your_template.html')

def editmainvisa(request,id,search_query):
    if request.method == 'POST':
        phone_number = request.POST.get('Phonenumber')
        filed1 = request.POST.get('From')
        filed2 = request.POST.get('TO')
        filed3 = request.POST.get('Noofnights')
        checkout = request.POST.get('checkout')
        hotel = UploadUserdetails.objects.filter(id=id).first()

        # Check if a new file is uploaded
        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Delete the previously uploaded file if it exists
            if hotel.visa['attachment']:
                file_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/visa', hotel.visa['attachment'])
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            parts = hotel.visa['attachment'].split('\\')
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/visa', parts[0])
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            # Set the attachment field to the relative file path including the current date
            hotel.visa['attachment'] = os.path.join(current_date, uploaded_file.name)

        # Update other fields
        hotel.phone_number = phone_number
        hotel.visa['filed3'] = filed3
        hotel.visa['filed1']=filed1
        hotel.visa['filed2']=filed2
        hotel.visa['checkout'] = checkout


        # Update the updated_by field
        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
        hotel.updated_by = date_object
        hotel.editername = username
        
        # Save the updated instance
        hotel.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query)  # Replace 'hoteladmin' with your actual success URL name

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'visa.html', {'hotel': hotel})


def addinsurence(request,search_query):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'Sales' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    
    if request.method == 'POST':
        # Get form data
        phone_number = request.POST.get('Phonenumber')
        filed1 = request.POST.get('From')
        filed2 = request.POST.get('checkin')
        filed3 = request.POST.get('checkout')
        # filed1 = request.POST.get('Noofnights')
        print(request.FILES)

        uploadhotel_ = UploadUserdetails.objects.all()


        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/insurense', current_date)
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            uploadhotel_= os.path.join(current_date, uploaded_file.name)
        else:
            uploadhotel_=None

        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
            

        # Create and save instance
        uploadhotel_instance = UploadUserdetails(
            phone_number=phone_number,
            insurense={"filed1":filed1,"filed2":filed2,"filed3":filed3,"attachment":uploadhotel_},
            created_by = date_object,
            updated_by = date_object,
            uplodername = username,
            editername = username,
          
        )
        uploadhotel_instance.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query)  # Replace '/success-url/' with your actual success URL

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'your_template.html')

def editmaininsurence(request,id,search_query):
    if request.method == 'POST':
        phone_number = request.POST.get('Phonenumber')
        filed1 = request.POST.get('From')
        filed2 = request.POST.get('checkin')
        filed3 = request.POST.get('checkout')
        hotel = UploadUserdetails.objects.filter(id=id).first()

        # Check if a new file is uploaded
        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Delete the previously uploaded file if it exists
            if hotel.insurense['attachment']:
                file_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/insurense', hotel.insurense['attachment'])
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            parts = hotel.insurense['attachment'].split('\\')
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/insurense', parts[0])
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            # Set the attachment field to the relative file path including the current date
            hotel.insurense['attachment'] = os.path.join(current_date, uploaded_file.name)

        # Update other fields
        hotel.phone_number = phone_number
        hotel.insurense['filed3'] = filed3
        hotel.insurense['filed1']=filed1
        hotel.insurense['filed2']=filed2


        # Update the updated_by field
        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
        hotel.updated_by = date_object
        hotel.editername = username
        
        # Save the updated instance
        hotel.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query)  # Replace 'hoteladmin' with your actual success URL name

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'insurense.html', {'hotel': hotel})


def addpassport(request,search_query):
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'Sales' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    
    if request.method == 'POST':
        # Get form data
        phone_number = request.POST.get('Phonenumber')
        clientname = request.POST.get('From')

        uploadhotel_ = UploadUserdetails.objects.all()
        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/Passport', current_date)
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            uploadhotel_= os.path.join(current_date, uploaded_file.name)
        else:
            uploadhotel_=None

        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
            

        # Create and save instance
        uploadhotel_instance = UploadUserdetails(
            phone_number=phone_number,
            Passport={"clientname":clientname,"attachment":uploadhotel_},
            created_by = date_object,
            updated_by = date_object,
            uplodername = username,
            editername = username,
          
        )
        uploadhotel_instance.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query)  # Replace '/success-url/' with your actual success URL

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'your_template.html')

def editmainpassport(request,id,search_query):
    if request.method == 'POST':
        phone_number = request.POST.get('Phonenumber')
        clientnmae = request.POST.get('From')
        # filed2 = request.POST.get('TO')
        # filed3 = request.POST.get('Noofnights')
        hotel = UploadUserdetails.objects.filter(id=id).first()

        # Check if a new file is uploaded
        if 'attachmentfiles' in request.FILES:
            uploaded_file = request.FILES['attachmentfiles']
            
            # Delete the previously uploaded file if it exists
            if hotel.Passport['attachment']:
                file_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/Passport', hotel.insurense['attachment'])
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            # Get the current date
            current_date = datetime.now().strftime('%d-%m-%Y')
            parts = hotel.Passport['attachment'].split('\\')
            # Construct the folder path
            pdf_folder = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/Passport', parts[0])
            
            # Check if the folder for the current date exists, if not, create it
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            
            # Save the PDF file inside the folder
            pdf_file_path = os.path.join(pdf_folder, uploaded_file.name)
            with open(pdf_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            # Set the attachment field to the relative file path including the current date
            hotel.Passport['attachment'] = os.path.join(current_date, uploaded_file.name)

        # Update other fields
        hotel.phone_number = phone_number
        hotel.Passport['clientname']=clientnmae

        


        # Update the updated_by field
        username = request.session.get('username')
        current_time = timezone.now().strftime("%d-%m-%Y")
        date_object = datetime.strptime(current_time, "%d-%m-%Y")
        hotel.updated_by = date_object
        hotel.editername = username
        
        # Save the updated instance
        hotel.save()

        # Redirect after successful submission
        return redirect(reverse('useradminpage') + '?search_query=' + search_query)  # Replace 'hoteladmin' with your actual success URL name

    # If request method is not POST or form is not submitted yet, render the form page
    return render(request, 'insurense.html', {'hotel': hotel})


def delete_userpanel(request):
  
    if request.method == 'GET':
        id = request.GET.get('id', '')
        search_query = request.GET.get('search_query', '')
        type = request.GET.get('type', '')

        if type == 'hotel':
            hotel = Uploadhotel.objects.filter(id=id).first()

            if hotel.attachment:
                image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/hotelvoucher/', hotel.attachment)
                if os.path.exists(image_path):
                    os.remove(image_path)
            hotel.delete() 

            return redirect(reverse('useradminpage') + '?search_query=' + search_query)

        if type == 'flight':
            hotel = UploadFlight.objects.filter(id=id).first()

            if hotel.ticketattachment:
                image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/flightvoucher/', hotel.ticketattachment)
                if os.path.exists(image_path):
                    os.remove(image_path)
            hotel.delete() 
        
            return redirect(reverse('useradminpage') + '?search_query=' + search_query)
        
            
        if type == 'transfers':
            hotel = UploadTransfers.objects.filter(id=id).first()

            if hotel.datas['attachment']:
                image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/transfers/', hotel.datas['attachment'])
                if os.path.exists(image_path):
                    os.remove(image_path)
            hotel.delete() 
        
            return redirect(reverse('useradminpage') + '?search_query=' + search_query) 
        if type == 'tickets':
            hotel = UploadUserdetails.objects.filter(id=id).first()

            if hotel.tickets['attachment']:
                image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/tickets/', hotel.tickets['attachment'])
                if os.path.exists(image_path):
                    os.remove(image_path)
            hotel.delete() 
        
            return redirect(reverse('useradminpage') + '?search_query=' + search_query) 
        if type == 'visa':
            hotel = UploadUserdetails.objects.filter(id=id).first()

            if hotel.visa['attachment']:
                image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/visa/', hotel.visa['attachment'])
                if os.path.exists(image_path):
                    os.remove(image_path)
            hotel.delete() 
        
            return redirect(reverse('useradminpage') + '?search_query=' + search_query) 
        if type == 'insurance':
            hotel = UploadUserdetails.objects.filter(id=id).first()

            if hotel.insurense['attachment']:
                image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/insurense/', hotel.insurense['attachment'])
                if os.path.exists(image_path):
                    os.remove(image_path)
            hotel.delete() 
        
            return redirect(reverse('useradminpage') + '?search_query=' + search_query)
        if type == 'Passport':
            hotel = UploadUserdetails.objects.filter(id=id).first()

            if hotel.Passport['attachment']:
                image_path = os.path.join(settings.BASE_DIR, 'VFpages/static/pdf/Passport/', hotel.Passport['attachment'])
                if os.path.exists(image_path):
                    os.remove(image_path)
            hotel.delete() 
        
            return redirect(reverse('useradminpage') + '?search_query=' + search_query) 

import mimetypes
from django.http import FileResponse, HttpResponse

def useradminpage(request): 
     # Check if user is authenticated
    if not request.session.get('username') or not request.session.get('role'):
        # Redirect to login page if session data is not found
        return redirect('login')

    # Check if the user has the appropriate role to access this page
    role = request.session.get('role')
    userdetails = adminheader(request)
    if role != 'Sales' and role != 'superadmin' and role != 'employee':
        return redirect('dashboard')
    # my_value1 = request.session.get('my_value1')
    hotel_data = UploadFlight.objects.all()
    hotel_data2 = Uploadhotel.objects.all()
    hotel_data3 = UploadTransfers.objects.all()
    hotel_data4 = UploadUserdetails.objects.all()
    # hotel_data5 = UploadUserdetails.objects.all()
    search_query = request.GET.get('search_query')
    user_name = None
    if search_query:
        filtered_hotels = hotel_data.filter(phone_number=search_query)
        filtered_hotels2 = hotel_data2.filter(phone_number=search_query)
        filtered_hotels3 = hotel_data3.filter(phone_number=search_query)
        filtered_hotels4 = hotel_data4.filter(phone_number=search_query)
        # filtered_hotels5 = hotel_data4.filter(phone_number=search_query)
        
        # if not filtered_hotels:
        #     # Return a JSON response with a message indicating no hotels found
        #     return JsonResponse({'message': 'No hotels found matching the search query'}, status=404)
        # if not filtered_hotels2:
        #     # Return a JSON response with a message indicating no hotels found
        #     return JsonResponse({'message': 'No hotels found matching the search query'}, status=404)
        # if not filtered_hotels3:
        #     # Return a JSON response with a message indicating no hotels found
        #     return JsonResponse({'message': 'No hotels found matching the search query'}, status=404)
        # if not filtered_hotels4:
        #     # Return a JSON response with a message indicating no hotels found
        #     return JsonResponse({'message': 'No hotels found matching the search query'}, status=404)
        

        
        hotel_data = filtered_hotels
        hotel_data2 = filtered_hotels2
        hotel_data3 = filtered_hotels3
        hotel_data4 = filtered_hotels4
        try:
            user_name = Userdetails.objects.get(phone_number=search_query)
        except:
            user_name = "User not found"   

    
    return render(request,'admin/UserCMS/customerportel.html',{"userdetails":userdetails,"hotel_data":hotel_data,"hotel_data2":hotel_data2,"hotel_data3":hotel_data3,"hotel_data4":hotel_data4,"search_query":search_query,"user_name":user_name})







