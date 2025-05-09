# myapp/views.py
from django.shortcuts import render
from .models import Equipment
from django.db.models import Q  # For complex queries
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import CreateView
from .models import Donation
from .forms import DonationForm
from django.urls import reverse_lazy



def home(request):
    return render(request, 'myapp/home.html')

class EquipmentListView(ListView):
    model = Equipment
    template_name = 'myappp/equipment_list.html'  # Specify your template name
    context_object_name = 'equipments'  # Name of the variable to be used in the template

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(description__icontains=search_query)
            )
        return queryset
class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'myapp/equipment_detail.html'  # Specify your template name
    context_object_name = 'equipment'  # Name of the variable to be used in the template

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        return obj
    
class EquipmentSearchView(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            equipments = Equipment.objects.filter(
                Q(name__icontains=search_query) | Q(description__icontains=search_query)
            )
        else:
            equipments = Equipment.objects.all()
        return render(request, 'myapp/equipment_list.html', {'equipments': equipments})

class  BookingCreateView(View):
    def get(self, request, equipment_id):
        equipment = get_object_or_404(Equipment, id=equipment_id)
        return render(request, 'myapp/booking_create.html', {'equipment': equipment})

    def post(self, request, equipment_id):
        # Handle booking creation logic here
        pass

class DonationCreateView(CreateView):
    model = Donation
    form_class = DonationForm
    template_name = 'donate.html'
    success_url = reverse_lazy('donate_success')