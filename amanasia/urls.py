"""amanasia URL Configuration

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
from accounts import views

urlpatterns = [
    path('', views.home_redirect, name='redirect'),
    path('home', views.EntryListView.as_view(), name='home'),
    path('<int:pk>', views.EntryDetailView.as_view(), name='Entries_detail'),
    path('create', views.EntryCreateView.as_view(), name='Entries_create'),
    path('update/<int:pk>', views.EntryUpdateView.as_view(), name='Entries_update'),
    path('delete/<int:pk>', views.EntryDeleteView.as_view(), name='Entries_delete'),
    path('excel/', views.data_to_excel, name='excel'),
    path('admin', admin.site.urls),
]
