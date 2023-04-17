from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('user/', views.user,name="index"),
    path('user/paid/<int:cno>', views.paid,name="inde"),
    path('user/challan/<int:cno>', views.challan,name="paidlist"),
    path('user/invoice/<int:cno>', views.invoice,name="paidlist"),





]
