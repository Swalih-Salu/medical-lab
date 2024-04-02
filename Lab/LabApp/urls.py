from . import views
from django.urls import path

app_name='Main'
urlpatterns = [
    path('',views.Home,name='home'),
    path('tele-radiology/',views.Teleradio,name='teleradio'),
    path('health-checkup-packages/',views.Hcp,name='hcp'),
    path('doctor-consultitions/',views.Doc,name='doc'),
    path('gallery/',views.Gallery,name='gallery'),
    path('partner-with-us/',views.Pws,name='pws'),
    path('contact-us/',views.Contact,name='contact'),
    path('Haematology/',views.Haematology,name='Haematology'),
    path('Biochemistry/',views.Biochemistry,name='Biochemistry'),
    path('Immunology/',views.Immunology,name='Immunology'),
]
