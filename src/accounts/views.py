from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Register User
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check user name
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is already taken.")
                return redirect('register')
            else:
                # Check email exists
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is being used.")
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    ## Login after registration
                    # auth.login(request, user)
                    # messages.success(request, "You are now logged in.")
                    # return redirect('index')

                    ## Manually user should log in
                    user.save()
                    messages.success(request, "You are now registered and can log in.")
                    return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:
        template_name = "accounts/register.html"
        context = {}
        return render(request, template_name, context)

def login(request):
    if request.method == 'POST':
        # Register User
        # Login User
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    else:
        template_name = "accounts/login.html"
        context = {}
        return render(request, template_name, context)

def logout(request):
    return redirect('index')

def dashboard(request):

    template_name = "accounts/dashboard.html"
    context = {}
    return render(request, template_name, context)
