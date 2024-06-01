"""kareliamulparlour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from kap.views import index, dairy_products, ice_cream, contact, delivery, search_list, thanks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index', index),
    path('dairy_products', dairy_products),
    path('ice_cream', ice_cream),
    path('contact', contact),
    path('delivery', delivery),
    path('Amul_1_Ltr_Ice_Cream_Tubs', ice_cream),
    path('Amul_2_Ltr_Ice_Cream_Bricks', ice_cream),
    path('Amul_750ml_Ice_Cream_Bricks', ice_cream),
    path('search_list', search_list),
    path('thanks', thanks)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
