# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from .forms import UserRegisterForm, EditProfileView
from .models import UserProfile
from django.contrib.auth import update_session_auth_hash
# Create your views here.

User = get_user_model()

def edit_profile(request):

    if request.method == 'POST':
        form = EditProfileView(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect("profiles:detail", username=username)

    else:
        form = EditProfileView(instance=request.user)

        return render(request, 'accounts/edit_profile.html', {'form': form})

def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect("/")


    else:
        form = PasswordChangeForm(user=request.user)

        return render(request, 'accounts/change_password.html', {'form': form})


class UserRegisterView(FormView):
  template_name = 'accounts/user_register_form.html'
  form_class = UserRegisterForm
  success_url = '/login'

  def form_valid(self,form):
    #form.send_email()
    username = form.cleaned_data.get("username")
    email = form.cleaned_data.get("email")
    password = form.cleaned_data.get("password")
    first_name = form.cleaned_data.get("first_name")
    last_name = form.cleaned_data.get("last_name")

    new_user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
    new_user.set_password(password)
    new_user.save()
    return super(UserRegisterView, self).form_valid(form)

class UserDetailView(DetailView):
	template_name = 'accounts/user_detail.html'
	queryset = User.objects.all()

	def get_object(self):
		return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

	def get_context_data(self, *args, **kwargs):
	  	context = super(UserDetailView, self).get_context_data(*args, **kwargs)
	  	following = UserProfile.objects.is_following(self.request.user, self.get_object())
	  	context['following'] = following
	  	context['recommended'] = UserProfile.objects.recommended(self.request.user)
	  	return context


class UserFollowView(View):
 	def get(self, request, username, *args, **kwargs):
 		toggle_user = get_object_or_404(User, username__iexact=username)
 		if request.user.is_authenticated():
 			is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
 		return redirect("profiles:detail", username=username)
 		# user_profile, created = UserProfile.objects.get_or_create(user=request.user)
 			# if toggle_user in user_profile.following.all():
 			# 	user_profile.following.remove(toggle_user)
 			# else:
 			# 	user_profile.following.add(toggle_user)

class EditProfileView(UserChangeForm):

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password',
			)
