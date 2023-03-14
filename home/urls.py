from django.contrib import admin
from django.urls import path,re_path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('codeeditor/',views.editor,name='editor'),
    re_path(r'^home/run$',views.runcode),
    path('home/submit ',views.OnCLICKSUBMIT,name='Submit for review'),


]
admin.site.site_header  =  "QQGC ADMIN"
admin.site.site_title  =  "Admin Panel"
admin.site.index_title  =  "Welcome Admin"