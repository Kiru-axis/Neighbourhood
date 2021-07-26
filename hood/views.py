from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import SignupForm, BusinessForm,UpdateProfileForm, NeighbourHoodForm, PostForm
from .models import NeighbourHood, Profile, Business, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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
            return redirect('single-hood', hood.id)
            
    else:
        form = BusinessForm()
    params = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'hood/single_hood.html', params)


        # join or leave your hoods

@login_required(login_url='login')
def join_hood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')


def leave_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')


# profile section
def profile(request, username):
    return render(request, 'hood/profile.html')

    # edit profile
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'hood/editprofile.html', {'form': form})


# posts section
def create_post(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('single-hood', hood.id)
    else:
        form = PostForm()
    return render(request, 'hood/post.html', {'form': form})

# Businesses section
def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Business.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'hood/results.html', params)
    else:
        message = "You haven't searched for any business category"
    return render(request, "hood/results.html")
