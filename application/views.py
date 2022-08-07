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

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
def post(request):
    return render(request,'post.html')
def client(request):
    return render(request,'client.html')
def contact(request):
    return render(request,'contact.html')

def authentication (request):
    
    return render(request, 'registration/authentication.html')

