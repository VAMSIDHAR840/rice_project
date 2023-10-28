"""vlt_prod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examp
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
from django.urls import path, include
from warehouse import urls as warehouse_urls
from suppliers import urls as suppliers_urls
from customers import urls as customers_urls
from drivers import urls as drivers_urls
from manager import urls as manager_urls
from owner import urls as owner_urls
from employee import urls as employee_urls
from backend import urls as backend_urls
from backend.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('warehouse/', include(warehouse_urls)),
    path('suppliers/', include(suppliers_urls)),
    path('customers/', include(customers_urls)),
    path('drivers/', include(drivers_urls)),
    path('manager/', include(manager_urls)),
    path('owner/', include(owner_urls)),
    path('employee/', include(employee_urls)),
    path('backend/', include(backend_urls)),
    path('', login.as_view(), name="login_page"),
]
