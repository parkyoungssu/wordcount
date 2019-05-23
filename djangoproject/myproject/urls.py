from django.contrib import admin
from django.urls import path
import myapp.views

import ysapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name='home'),
    path('ys/',ysapp.views.index, name='index')
]
