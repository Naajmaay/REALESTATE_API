from django.shortcuts import render, redirect
from .models import Property
from .form import PropertyForm
from django.contrib.auth.decorators import login_required

def property_list(request):
    properties = Property.objects.all()
    return render(request, "properties/property_list.html", {"properties": properties})

def property_detail(request, id):
    prop = Property.objects.filter(id=id).first()
    if not prop:
        return render(request, "property_not_found.html")  # create this template
    return render(request, "properties/property_detail.html", {"prop": prop})

@login_required
def property_create(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            prop = form.save(commit=False)
            prop.agent = request.user
            prop.save()
            return redirect('property_detail', id=prop.id)
    else:
        form = PropertyForm()
    return render(request, "properties/property_create.html", {"form": form})

@login_required
def property_edit(request, id):
    prop = Property.objects.filter(id=id).first()
    if not prop:
        return render(request, "property_not_found.html")  # optional custom template

    if prop.agent != request.user:
        return render(request, "access_denied.html")  # create this template

    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES, instance=prop)
        if form.is_valid():
            form.save()
            return redirect('property_detail', id=prop.id)
    else:
        form = PropertyForm(instance=prop)

    return render(request, "properties/property_edit.html", {"form": form})
