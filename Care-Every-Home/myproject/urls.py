from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Import views ที่จำเป็นเท่านั้น
from myapp.views import (
    home,
    EquipmentListView,
    EquipmentDetailView,
    BookingCreateView,
    DonationCreateView,
)

# Import views ที่จำเป็นเท่านั้น
from myapp.views import (
    home,
    EquipmentListView,
    EquipmentDetailView,
    BookingCreateView,
    DonationCreateView,
)


from myapp.views import (
    home,
    EquipmentListView,
    EquipmentDetailView,
    BookingCreateView,
    DonationCreateView,  # ✅ ตรงนี้ถูกต้อง
)


from myapp.views import (
    home,
    EquipmentListView,
    EquipmentDetailView,
    BookingCreateView,
    DonationCreateView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('equipments/', EquipmentListView.as_view(), name='equipment_list'),
    path('equipments/<int:pk>/', EquipmentDetailView.as_view(), name='equipment_detail'),
    path('search/', EquipmentListView.as_view(), name='equipment_search'),
    path('bookings/create/<int:equipment_id>/', BookingCreateView.as_view(), name='booking_create'),
    path('donate/', DonationCreateView.as_view(), name='donate'),
    path('donate/success/', TemplateView.as_view(template_name='donate_success.html'), name='donate_success'),
]

# สำหรับไฟล์ media (รูป ฯลฯ)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
