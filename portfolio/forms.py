from django import forms
from .models import Person, Occupation, Skills, WorkExp, AcadExp, Contact

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'display_picture']

        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
        }
class OccupationForm(forms.ModelForm):
    class Meta:
        model = Occupation
        fields = ['occupation']

        widgets = {
            'occupation' : forms.TextInput(attrs={'class' : 'form-control'})
        }


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skills']

        widgets = {
            'skills' : forms.TextInput(attrs={'class' : 'form-control'})
        }

class WorkExpForm(forms.ModelForm):
    class Meta:
        model = WorkExp
        fields = ['company', 'started', 'left', 'position']

        widgets = {
            'company' : forms.TextInput(attrs={'class' :'form-control'}),
            'started' : forms.Select(attrs={'class' : 'form-control col-4'}),
            'left' : forms.Select(attrs={'class' : 'form-control col-4'}),
            'position' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

class AcadExpForm(forms.ModelForm):
    class Meta:
        model = AcadExp
        fields = ['education']

        widgets = {
            'education' : forms.TextInput(attrs={'class' : 'form-control'})
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['cell', 'twitter', 'instagram', 'linkedin']

        widgets = {
            'cell' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'twitter' : forms.TextInput(attrs={'class' : 'form-control'}),
            'instagram' : forms.TextInput(attrs={'class' : 'form-control'}),
            'linkedin' : forms.TextInput(attrs={'class' : 'form-control'}),
        }
    
