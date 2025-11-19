from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from properties.models import Property
from .form import BookingForm
from django.contrib.auth.decorators import login_required

@login_required
def booking_list(request):
    # Show only bookings made by the logged-in user (buyer)
    bookings = Booking.objects.filter(buyer=request.user)
    return render(request, "bookings/booking_list.html", {"bookings": bookings})

@login_required
def booking_edit(request, id):
    # Only allow editing bookings belonging to the logged-in user
    booking = get_object_or_404(Booking, id=id, buyer=request.user)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, "bookings/booking_edit.html", {"form": form})

@login_required
def booking_create(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        booking = Booking.objects.create(
            property=property,
            buyer=request.user,  # link booking to logged-in user
            buyer_name=request.POST["buyer_name"],
            email=request.POST["email"],
            booking_date=request.POST["booking_date"],
            message=request.POST["message"]
        )
        return redirect('payment_create', booking_id=booking.id)

    return render(request, 'bookings/booking_create.html', {"property": property})
