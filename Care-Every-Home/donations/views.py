from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DonationRequestForm, DonationOfferForm
from .models import DonationRequest, DonationOffer
from django.contrib.auth.models import User


def home(request):
    return HttpResponse("Hello from donations!")


def browse_requests(request):
    donation_requests = DonationRequest.objects.filter(fulfilled=False).order_by('-created_at')
    return render(request, 'donations/browse_requests.html', {'donation_requests': donation_requests})


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

            donation_request.fulfilled = True
            donation_request.save()
            print("✅ fulfilled set to True for request ID:", donation_request.id)

            messages.success(request, "คุณได้บริจาคเรียบร้อยแล้ว")
            return redirect('my_donations')
        else:
            print("❌ Form Errors:", form.errors)
            messages.error(request, "มีบางอย่างผิดพลาดในการส่งฟอร์ม")
    else:
        form = DonationOfferForm()

    return render(request, 'donations/donation_offer.html', {
        'donation_request': donation_request,
        'form': form
    })


@login_required
def create_donation_request(request):
    if request.method == 'POST':
        print("POST DATA:", request.POST)
        form = DonationRequestForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            donation_request = form.save(commit=False)
            donation_request.requester = request.user
            donation_request.save()
            print("Saved successfully")
            return redirect('my_requests')
        else:
            print("Form errors:", form.errors)
    else:
        form = DonationRequestForm()
    return render(request, 'donations/create_request.html', {'form': form})


@login_required
def my_donations(request):
    offers = DonationOffer.objects.filter(donater=request.user).select_related('request').order_by('-created_at')
    return render(request, 'donations/my_donations.html', {'offers': offers})