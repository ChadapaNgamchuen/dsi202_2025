from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from donations!")

def browse_requests(request):
    return HttpResponse("This is browse_requests page.")
