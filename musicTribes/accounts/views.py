from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from django.shortcuts import get_object_or_404, redirect, render

from django.urls import reverse_lazy
from django.views import generic

from app.forms import NewUserForm, UserUpdateForm, ProfileUpdateForm
from app.models import User, Profile

class SignUpView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('app:index')
    template_name = 'registration/signup.html'
    
@login_required
def profile(request, user_id):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('app:index') 

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile.html', context)

