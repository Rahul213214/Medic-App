from django.shortcuts import render

# Create your views here.
def appointmentForm(request):
    return render(request, 'appointment/appointform.html')