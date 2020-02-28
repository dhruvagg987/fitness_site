from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import userprofile

class signup_form(UserCreationForm):
    email= forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name= forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )

    def __init__(self, *args, **kwargs):
        super(signup_form, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='User Name'
        self.fields['username'].label=''
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password1'].label=''
        self.fields['password1'].help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

       
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Comfirm Password'
        self.fields['password2'].label=''
        self.fields['password2'].help_text='<span class="form-text text-muted"><small> Enter the same password as before, for verification.</small></span>'

class edit_form(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name', 'email','password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='User Name'
        self.fields['username'].label='User Name'
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['first_name'].widget.attrs['class']='form-control'
        self.fields['first_name'].widget.attrs['placeholder']='First Name'
        self.fields['first_name'].label='First Name'
        
        self.fields['last_name'].widget.attrs['class']='form-control'
        self.fields['last_name'].widget.attrs['placeholder']='Last Name'
        self.fields['last_name'].label='Last Name'
        
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='Email'
        self.fields['email'].label='Email'



class edit_profileform(UserChangeForm):
    # password = forms.CharField(label="", widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model=userprofile
        fields=('age','weight','height','calories')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields['age'].widget.attrs['class']='form-control'
        self.fields['age'].widget.attrs['placeholder']='Age'
        self.fields['age'].label=''

        self.fields['weight'].widget.attrs['class']='form-control'
        self.fields['weight'].widget.attrs['placeholder']='Weight (in kg)'
        self.fields['weight'].label=''

        self.fields['height'].widget.attrs['class']='form-control'
        self.fields['height'].widget.attrs['placeholder']='Height (in cm)'
        self.fields['height'].label=''

        self.fields['calories'].widget.attrs['class']='form-control'
        self.fields['calories'].widget.attrs['placeholder']='Calories'
        self.fields['calories'].label=''

class password_changeform(PasswordChangeForm):

    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class']='form-control'
        self.fields['old_password'].widget.attrs['placeholder']='old password'
        self.fields['old_password'].label=''

        self.fields['new_password1'].widget.attrs['class']='form-control'
        self.fields['new_password1'].widget.attrs['placeholder']='New Password'
        self.fields['new_password1'].label=''
        self.fields['new_password1'].help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'


        self.fields['new_password2'].widget.attrs['class']='form-control'
        self.fields['new_password2'].widget.attrs['placeholder']='Confirm New Password'
        self.fields['new_password2'].label=''
      

class userprofileForm(forms.ModelForm):

    class Meta:
        model = userprofile
        fields=('age','weight','height','calories')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields['age'].widget.attrs['class']='form-control'
        self.fields['age'].widget.attrs['placeholder']='Age'
        self.fields['age'].label=''

        self.fields['weight'].widget.attrs['class']='form-control'
        self.fields['weight'].widget.attrs['placeholder']='Weight (in kg)'
        self.fields['weight'].label=''

        self.fields['height'].widget.attrs['class']='form-control'
        self.fields['height'].widget.attrs['placeholder']='Height (in cm)'
        self.fields['height'].label=''

        self.fields['calories'].widget.attrs['class']='form-control'
        self.fields['calories'].widget.attrs['placeholder']='Calories'
        self.fields['calories'].label=''

