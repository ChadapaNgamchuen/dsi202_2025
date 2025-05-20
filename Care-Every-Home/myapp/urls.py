from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home, ProductListView, ProductDetailView, RentProductView, 
    ProductListCreateAPIView, ProductRetrieveUpdateAPIView, 
    dashboard, toggle_favorite, FavoriteListView, toggle_cart, 
    CartListView, user_profile, mark_payment, post_review, toggle_review_like, submit_review,
    browse_requests, donation_offer, my_requests,checkout
)

urlpatterns = [
    path('', home, name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/rent/', RentProductView.as_view(), name='rent_product'),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/products/', ProductListCreateAPIView.as_view(), name='product_api_list_create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateAPIView.as_view(), name='product_api_retrieve_update'),
    path('favorite/toggle/<int:product_id>/', toggle_favorite, name='toggle_favorite'),
    path('favorites/', FavoriteListView.as_view(), name='favorite_list'),
    path('cart/toggle/<int:product_id>/', toggle_cart, name='toggle_cart'),
    path('cart/', CartListView.as_view(), name='cart_list'),
    path('profile/', user_profile, name='user_profile'),
    path('rental/<int:rental_id>/pay/', mark_payment, name='mark_payment'),
    path('products/<int:product_id>/review/', post_review, name='post_review'),
    path('review/<int:review_id>/like/', toggle_review_like, name='toggle_review_like'),
    path('rental/<int:rental_id>/review/', submit_review, name='submit_review'),

    # คำร้องขอของบริจาค
    path('requests/', browse_requests, name='browse_requests'),
    path('requests/<int:request_id>/offer/', donation_offer, name='donation_offer'),
    path('my-requests/', my_requests, name='my_requests'),
    path('checkout/', checkout, name='checkout')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    