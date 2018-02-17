from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

User = get_user_model()

class UserRegisterForm(forms.Form):

	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'js-username-field email-input js-initial-focus', 'placeholder': 'Username'}), max_length=30, required=True)
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'js-username-field email-input js-initial-focus', 'placeholder': 'Firstname'}), max_length=20, required=True)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'js-username-field email-input js-initial-focus', 'placeholder': 'Lastname'}), max_length=30, required=True)
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'js-username-field email-input js-initial-focus' , 'placeholder': 'Email'}), required=True,)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'js-password-field js-initial-focus', 'placeholder': 'Password'}), required=True,)
	# password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

	# def clean_password2(self):
	# 	password = self.cleaned_data.get('password')
	# 	password2 = self.cleaned_data.get('password2')

	# 	if password != password2:
	# 		raise forms.ValidationError("Password must match")
	# 	return password2

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username__icontains=username).exists():
			raise forms.ValidationError("This username is already taken.")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email__icontains=email).exists():
			raise forms.ValidationError("This email is already registered.")
		return email

class EditProfileView(UserChangeForm):

	class Meta:
		model = User
	# username = forms.CharField(widget=forms.TextInput(attrs={'class': 'js-username-field email-input js-initial-focus', 'placeholder': 'Username'}), max_length=30, required=True)
	# first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'js-username-field email-input js-initial-focus', 'placeholder': 'Firstname'}), max_length=20, required=True)
	# last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'js-username-field email-input js-initial-focus', 'placeholder': 'Lastname'}), max_length=30, required=True)
	# email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'js-username-field email-input js-initial-focus' , 'placeholder': 'Email'}), required=True,)
	# password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'js-password-field js-initial-focus', 'placeholder': 'Password'}), required=True,)

		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password',
			)
