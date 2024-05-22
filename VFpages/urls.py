from django.urls import path
from .import views

urlpatterns= [
    path('',views.home_page,name="home_page"),
    path('contact-us', views.contact_us, name='contact_us'),
    path('insert_customer_details',views.insert_customer_details,name='insert_customer_details'),
    path('about-us', views.about_us, name='about-us'),
    path('header_fn', views.header_fn, name='header_fn'),
    path('footer', views.footer, name='footer'),
    
    
    
    path('international-tour', views.main_Destination, name='international-tour'),
    path('international-tour-package/<str:continent_name>', views.main_DestinationCity, name='international-tour-package'),
    path('domestic-package/<str:continent_name>', views.main_DestinationCity, name='domestic-package'),
    path('international-tour-packages/<str:city_name>', views.main_DestinationAttraction, name='international-tour-packages'),
    path('domestic-packages/<str:city_name>', views.main_DestinationAttraction, name='domestic-packages'),
    path('domestic-tour', views.domestic_city, name='domestic-tour'),
    
    path('travel-category/<str:city_name>', views.catagories_city, name='travel-category'),
    
    
    path('blogs-travelblogs', views.gridblogus, name='gridblogus'),
    # path('bloglist/', views.bloglist, name='bloglist'),
    path('blogs/<str:blog_url>', views.blogsdetails, name='blogsdetails'),
    # path('download_images/', views.download_images, name='download_images'),
    
    path('tour-packages/<str:lead>', views.lead_itinerary, name='tour-packages'),
    
    # Login
    path('send_otp',views.send_otp,name='send_otp'),
    path('verify-otp', views.verify_otp, name='verify_otp'),
    path('signups', views.signups, name='signups'),
    path('login_views',views.login_views,name='login_views'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('send_otp_forgot',views.send_otp_forgot,name='send_otp_forgot'),
    path('change_password', views.change_password, name='change_password'),

    
    
    path('terms-and-conditions',views.terms,name='terms-and-conditions'),
    path('privacy-policy',views.privacy,name='privacy-policy'),
    path('sales-policy',views.cancel,name='sales-policy'),
    
    
    #portal
    path('portalhome',views.portalhome,name='portalhome'),
    path('upcominghotel',views.upcominghotel,name='upcominghotel'),
    path('upcomingflight',views.upcomingflight,name='upcomingflight'),
    path('transfersuser',views.transfersuser,name='transfersuser'),
    path('ticketsuser',views.ticketsuser,name='ticketsuser'),
    path('visauser',views.visauser,name='visauser'),
    path('insuranceuser',views.insuranceuser,name='insuranceuser'),
    path('passportuser',views.passportuser,name='passportuser'),
    
    path('download_attachment/<int:id>/<str:type>',views.download_attachment,name='download_attachment'),
    
    path('send_pdf_link',views.send_pdf_link,name='send_pdf_link'),
    path('send_whatsapp_message_2/',views.send_whatsapp_message_2,name='send_whatsapp_message_2'),
    path('download_pdf/', views.download_pdf, name='download_pdf'),
    
    path('hotelcompleted',views.hotelcompleted,name='hotelcompleted'),
    path('flightcompleted',views.flightcompleted,name='flightcompleted'),
    path('send_captcha',views.send_captcha,name='send_captcha'),
    path('send_captcha2',views.send_captcha2,name='send_captcha2'),

    

]

