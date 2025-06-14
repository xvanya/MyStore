from django.shortcuts import render, redirect
from .utils import optimize_image
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import CustomUser

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.email = form.cleaned_data['email']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                if 'image' in request.FILES:
                    # optimized_image, new_name = optimize_image(request.FILES['image'], max_size=(300, 300))
                    # user.image_small.save(new_name, optimized_image, save=False)
                    # optimized_image, new_name = optimize_image(request.FILES['image'], max_size=(600, 600))
                    # user.image_medium.save(new_name, optimized_image, save=False)
                    optimized_image, new_name = optimize_image(request.FILES['image'], max_size=(1200, 1200))
                    user.image.save(new_name, optimized_image, save=False)
                user.save()
                return redirect('users:index')
            except Exception as e:
                messages.error(request, f'Помилка при реєстрації: {str(e)}')
        else:
            messages.success(request, 'Виправте помилки в формі')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def index(request):
    users = CustomUser.objects.all()
    return render(request, 'users.html', {'users': users})