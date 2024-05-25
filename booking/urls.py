from django.urls import path
from . import views

urlpatterns= [
   path('',views.home,name="home"),
   path('hotel', views.hotel, name='hotel'),
   path('hotelreview/',views.hotelreview,name="hotelreview"),
   path('roomdetails/<str:hotelCode>/<str:traceId>/<str:resultIndex>/<str:tokenId>/',views.roomdetails,name="roomdetails"),
   path('search_destinations', views.search_destinations, name='search_destinations'),
   path('hotellist', views.process_form, name='hotellist'),
   path('get_room_details/', views.get_room_details, name='get_room_details'),
   path('your_view', views.your_view, name='your_view'),
   path('previewpage/', views.previewpage, name='previewpage'),
   path('hotelbooked/', views.hotelbooked, name='hotelbooked'),
   path('pdf/<str:pk>',views.generatePDf,name='pdf'),
   path('pdfs/',views.pdf,name='pdfs'),
   path('testpdf/',views.testpdf,name='testpdf'),
   path('mail/',views.mail,name='mail'),
   path('mailsucess/',views.sendemail,name='mailsucess'),
   path('signups/', views.signups, name='signups'),
   path('login_views/',views.login_views,name='login_views'),
   path('logout_view/',views.logout_view,name='logout_view'),
   path('download_pdfview/', views.download_pdfview, name='download_pdfview'),
   path('change_password/', views.change_password, name='change_password'),

   # TEST
    path('listofhotelx/', views.listofhotelx, name='listofhotelx'),
    path('hotel_home', views.hotel_homex, name='hotel_home'),
   # path('navbar/',views.navbar,name='navbar')
   # path('review', views.review, name='review'),
]