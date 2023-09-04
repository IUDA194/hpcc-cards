from table.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getalldata/', get_all_data),
    path('adminn/', adminn)
]
