from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    user = request.user
    if user.groups.filter(name='Sellers').exists():
        role = 'seller'
    else:
        role = 'buyer'
    return render(request, 'home.html', {'role': role})
