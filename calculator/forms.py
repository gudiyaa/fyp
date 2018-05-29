from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Personal,Qualification,Research_Publications

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['post_apply', 'department','email','category','pwd_status',
                    'internal_candidate','profile_image','first_name','middle_name',
                    'last_name','father_name','date_of_birth','age','gender','nationality',
                    'aadhar_card','marital_status','correspondence_address',
                    'permanent_address','mobile','areas_of_specialization',
                    'phd_thesis_title','date_of_acquiring_phd']


class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ['exam_passed','year_of_passing','degree_name','discipline_or_subjects',
        'board_or_university_or_institution',
        'cgpa_or_marks','class_or_division']

class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research_Publications
        fields = '__all__'
        exclude=['user','score1','score2','score3','score4','score5','score6','score7','score8','score9','score10','score11','score12','score13','score14','score15','score16','score17','score18','score19','score20','score21','score22','score']
        