from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from .forms import PaymentForm
from bookings.models import Booking

def payment_create(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Prevent duplicate payment
    if hasattr(booking, 'payment'):
        return redirect('payment_success', payment_id=booking.payment.id)

    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking
            payment.save()
            return redirect('payment_success', payment.id)
    else:
        form = PaymentForm(initial={'amount': 1000})  # Default value

    return render(request, 'payments/payment_form.html', {
        'form': form,
        'booking': booking
    })


def payment_success(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    return render(request, 'payments/payment_success.html', {'payment': payment})
