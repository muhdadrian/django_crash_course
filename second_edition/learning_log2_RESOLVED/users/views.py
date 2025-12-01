from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm() #1
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST) #2

        if form.is_valid(): #3
            new_user = form.save() #4
            # Log the user in and then redirect to home page.
            login(request, new_user) #5
            return redirect('learning_logs:index') #6

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


