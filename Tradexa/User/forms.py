from django import forms
from .models import User, Post

class CreatePost(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'text']

class UserRegistration(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']
		labels = {'first_name':'Enter first name', 
		'last_name':'Enter last name','password':'Enter password', 'email':'Enter email'}
		widgets = {'password':forms.PasswordInput, 
					'first_name':forms.TextInput(attrs={'placeholder':'First name'}),
					'last_name':forms.TextInput(attrs={'placeholder':'Last name'}),
					'email':forms.TextInput(attrs={'placeholder':'Email'}),
					'username':forms.TextInput(attrs={'placeholder':'Username'}),
		}
