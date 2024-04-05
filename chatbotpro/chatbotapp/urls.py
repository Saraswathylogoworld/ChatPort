from django.urls import path
from . import views
from . models import *

urlpatterns = [
    path('indexC',views.indexC,name='indexC'),
    path('logC',views.logC,name='logC'),
    path('logintheC',views.logintheC,name='logintheC'),
    path('regC',views.regC,name='regC'),
    path('registertheC',views.registertheC,name='registertheC'),
    path('thelogoutC',views.thelogoutC,name='thelogoutC'),
    path('about_the',views.about_the,name='about_the'),
    path('contact_the',views.contact_the,name='contact_the'),
    path('therapist_the',views.therapist_the,name='therapist_the'),
    path('doctor_the',views.doctor_the,name='doctor_the'),
    path('concellr_the',views.concellr_the,name='concellr_the'),
    path('indexUser1',views.indexUser1,name='indexUser1'),
    path('contact_user',views.contact_user,name='contact_user'),
    path('',views.reg_user,name='reg_user'),
    path('RegUser',views.RegUser,name='RegUser'),
    path('registertheC',views.registertheC,name='registertheC'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('reg_doctor',views.reg_doctor,name='reg_doctor'),
    path('RegDoc',views.RegDoc,name='RegDoc'),
    path('registerdoc',views.registerdoc,name='registerdoc'),
    path('doclogout',views.doclogout,name='doclogout'),
    path('add_lab',views.add_lab,name='add_lab'),
    path('labtable',views.labtable,name='labtable'),
    path('labdelete/<int:labdid>/',views.labdelete,name='labdelete'),
    path('lablist',views.lablist,name='lablist'),
    path('reg_doctor',views.reg_doctor,name='reg_doctor')
]