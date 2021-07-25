from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from .models import NeighbourHood, Profile, Business, Post

# Create your views here.
def index(request):
    return render(request, 'hood/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('hood')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

# hood section
def hoods(request):
    all_hoods = NeighbourHood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    print(all_hoods)
    return render(request, 'hood/all_hoods.html', params)
