from datetime import date
from django import forms
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


from .models import Patient

class PatientForm(forms.ModelForm):
    patient_id = forms.CharField(label='Patient ID', max_length=10, validators=[RegexValidator('^P[0-9]{6}$', 'Patient ID must start with P and be followed by 6 digits.')])
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date', 'max': str(date.today())}))
    confusion = forms.BooleanField(label='Confusion',  required=False)
    blood_urea = forms.IntegerField(label='Blood Urea', validators=[MinValueValidator(0), MaxValueValidator(100)], error_messages={'min_value': 'Blood Urea: Must be a positive number, with a maximum value of .'})
    respiratory_rate = forms.IntegerField(label='Respiratory Rate', validators=[MinValueValidator(0), MaxValueValidator(60)], error_messages={'min_value': 'Respiratory Rate: Must be a positive integer, with a maximum value of 60.'})
    systolic_bp = forms.IntegerField(label='Systolic Blood Pressure', validators=[MinValueValidator(90), MaxValueValidator(200)], error_messages={'min_value': 'Systolic Blood Pressure: Must be a positive integer, with a minimum value of 90 and a maximum value of 200.'})
    diastolic_bp = forms.IntegerField(label='Diastolic Blood Pressure', validators=[MinValueValidator(60), MaxValueValidator(120)], error_messages={'min_value': 'Diastolic Blood Pressure: Must be a positive integer, with a minimum value of 60 and a maximum value of 120.'})

    class Meta:
        model = Patient
        fields = ['patient_id', 'dob', 'confusion', 'blood_urea', 'respiratory_rate', 'systolic_bp', 'diastolic_bp']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'max': str(date.today())}),
        }

    def clean_patient_id(self):
        patient_id = self.cleaned_data['patient_id']
        if not patient_id.startswith('P'):
            raise forms.ValidationError('Patient ID must start with P')
        if not patient_id[1:].isdigit() or len(patient_id) != 7:
            raise forms.ValidationError('Patient ID must have 6 digits after P')
        return patient_id