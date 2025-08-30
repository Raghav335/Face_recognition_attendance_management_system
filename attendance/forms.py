from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Teacher, Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect,
        label="Register as",
        required=True
    )
    
    # Teacher-specific fields
    department = forms.CharField(max_length=100, required=False, label="Department")
    designation = forms.CharField(max_length=100, required=False, label="Designation")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'department', 'designation']

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        department = cleaned_data.get('department')
        designation = cleaned_data.get('designation')

        if role == 'teacher':
            if not department:
                raise forms.ValidationError("Department is required for teachers")
            if not designation:
                raise forms.ValidationError("Designation is required for teachers")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=True)
        role = self.cleaned_data.get('role')
        profile = user.profile
        # Explicitly set both to False first
        profile.is_student = False
        profile.is_teacher = False
        if role == 'student':
            profile.is_student = True
        elif role == 'teacher':
            profile.is_teacher = True
            # Create teacher profile with department and designation
            Teacher.objects.create(
                profile=profile,
                department=self.cleaned_data.get('department'),
                designation=self.cleaned_data.get('designation')
            )
        profile.save()
        return user

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_number', 'department', 'semester']

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['department', 'designation']

class FaceImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['face_image'] 