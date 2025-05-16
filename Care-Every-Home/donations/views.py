from django.http import HttpResponse
# import json
# from django.views.decorators.csrf import csrf_exempt
from .models import DonationRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import DonationRequestForm, DonationOfferForm




def home(request):
    return HttpResponse("Hello from donations!")

def browse_requests(request):
    requests = DonationRequest.objects.all()
    return render(request, 'donations/browse_requests.html', {'donation_requests': requests})

@login_required
def my_requests(request):
    requests = DonationRequest.objects.filter(requester=request.user)
    return render(request, 'donations/my_requests.html', {'requests': requests})


@login_required
def donation_offer(request, request_id):
    donation_request = get_object_or_404(DonationRequest, pk=request_id)

    if request.method == 'POST':
        form = DonationOfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.request = donation_request
            offer.donater = request.user
            offer.save()
            return redirect('browse_requests')
    else:
        form = DonationOfferForm()

    return render(request, 'donations/donation_offer.html', {
        'donation_request': donation_request,
        'form': form
    })

@login_required
def create_donation_request(request):
    if request.method == 'POST':
        print("POST DATA:", request.POST)  # ✅ เพิ่มบรรทัดนี้
        form = DonationRequestForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # ✅ debug ตรงนี้ด้วย
            donation_request = form.save(commit=False)
            donation_request.requester = request.user
            donation_request.save()
            print("Saved successfully")  # ✅ confirm การ save
            return redirect('my_requests')
        else:
            print("Form errors:", form.errors)  
    else:
        form = DonationRequestForm()
    return render(request, 'donations/create_request.html', {'form': form})
