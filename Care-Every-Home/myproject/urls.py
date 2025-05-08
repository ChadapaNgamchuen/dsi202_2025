from django.contrib import admin
from django.urls import path
from myapp.views import home, EquipmentListView, EquipmentDetailView,BookingCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('equipments/', EquipmentListView.as_view(), name='equipment_list'),
    path('equipments/<int:pk>/', EquipmentDetailView.as_view(), name='equipment_detail'),
    path('search/', EquipmentListView.as_view(), name='equipment_search'),
    path('bookings/create/<int:equipment_id>/', BookingCreateView.as_view(), name='booking_create')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
