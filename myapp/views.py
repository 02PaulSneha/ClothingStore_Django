from django.shortcuts import render
from .models import DressVerity,Store
from django.shortcuts import get_object_or_404
from .forms import DressVerityForm

# Create your views here.

def all_myapp(request):
    dresses = DressVerity.objects.all()
    return render(request, 'myapp/all_myapp.html',{'dresses':dresses})

def dress_detail(request,dress_id):
    dress = get_object_or_404(DressVerity, pk= dress_id)
    return render(request,'myapp/dress_detail.html', {'dress':dress})

def dress_store_view(request):
    stores = None
    if request.method == 'POST':
        form  = DressVerityForm(request.POST)
        if form.is_valid():
            Dress_verity = form.cleaned_data['dress_verity']
            stores=Store.objects.filter(dress_varieties=Dress_verity)
    else:
        form = DressVerityForm()
    return render(request, 'myapp/dress_store.html', {"stores":stores , "form": form})