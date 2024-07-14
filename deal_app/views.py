from django.shortcuts import render

# Create your views here.
def deal_register(request):
    return render(request, 'deal_register.html')