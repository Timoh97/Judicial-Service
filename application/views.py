from django.shortcuts import render

# Create your views here.
def index(request):
    
    
    return render(request, 'index.html')

def profile(request):
        
    return render(request, 'profile.html')
def posts(request):
        
    return render(request, 'post.html')
def update_profile(request):
    return render(request,'update_profile.html')
def create_post(request):
    return render(request,'profile.html')

def authentication (request):
    
    return render(request, 'registration/authentication.html')

