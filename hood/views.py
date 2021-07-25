from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import SignupForm, BusinessForm,UpdateProfileForm, NeighbourHoodForm, PostForm
from .models import NeighbourHood, Profile, Business, Post
from django.contrib.auth.decorators import login_required

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

        # create neighbourhood
@login_required(login_url='login')
def create_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighbourHoodForm()
    return render(request, 'hood/newhood.html', {'form': form})

    # single hood details
def single_hood(request,id):
    hood = NeighbourHood.objects.get(id=id)
    business = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = hood
            b_form.user = request.user.profile
            b_form.save()
            print(hood)
            print(business)
            print(posts)
            return redirect('hood/single-hood', hood.id)
            
    else:
        form = BusinessForm()
    params = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'hood/single_hood.html', params)