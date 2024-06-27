from django.urls import path
from . import views

urlpatterns= [
   # path('',views.home,name="home"),
   path('hotel', views.hotel, name='hotel'),
   path('hotelreview/',views.hotelreview,name="hotelreview"),
   # path('roomdetails/<str:hotelCode>/<str:traceId>/<str:resultIndex>/<str:tokenId>/',views.roomdetails,name="roomdetails"),
   path('search_destinations', views.search_destinations, name='search_destinations'),
   path('hotellist', views.process_form, name='hotellist'),
   # path('get_room_details/', views.get_room_details, name='get_room_details'),
   path('your_view/', views.your_view, name='your_view'),
   path('previewpage/', views.previewpage, name='previewpage'),
   path('hotelbooked/', views.hotelbooked, name='hotelbooked'),
   path('pdf/<str:pk>',views.generatePDf,name='pdf'),
   path('pdfs/',views.pdf,name='pdfs'),
   path('testpdf/',views.testpdf,name='testpdf'),
   path('mail/',views.mail,name='mail'),
   path('mailsucess/',views.sendemail,name='mailsucess'),
   path('download_pdfview/', views.download_pdfview, name='download_pdfview'),
   path('verify_pan/', views.verify_pan, name='verify_pan'),
]