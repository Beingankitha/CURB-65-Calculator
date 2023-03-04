from django.shortcuts import redirect, render
from .forms import PatientForm
from .models import Patient
from django.contrib import messages
from datetime import datetime

# Create your views here.

def calculate_score(patient):
    
    score = 1 if patient.confusion else 0
    score += 1 if patient.respiratory_rate >= 30 else 0
    score += 1 if patient.systolic_bp < 90 or patient.diastolic_bp <= 60 else 0
    score += 1 if patient.blood_urea >= 7 else 0
    score += 1 if patient.dob.year >= 65 else 0
    patient.score = score
    patient.save()

def index(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient_id = form.cleaned_data['patient_id']
            dob = form.cleaned_data['dob']
            confusion = form.cleaned_data['confusion']
            blood_urea = form.cleaned_data['blood_urea']
            respiratory_rate = form.cleaned_data['respiratory_rate']
            systolic_bp = form.cleaned_data['systolic_bp']
            diastolic_bp = form.cleaned_data['diastolic_bp']
            if Patient.objects.filter(patient_id=patient_id).exists():
                messages.error(request, f"A patient with ID {patient_id} already exists.")
                return redirect('index')
            else:
                patient = Patient(
                    patient_id=patient_id,
                    dob=dob,
                    confusion=confusion,
                    blood_urea=blood_urea,
                    respiratory_rate=respiratory_rate,
                    systolic_bp=systolic_bp,
                    diastolic_bp=diastolic_bp,
                )
                print(patient)

                calculate_score(patient)
                
                patient.save()
                
                return redirect('score', patient_id=patient.patient_id)
        else:
            messages.error(request, 'Please correct the errors below')
            context = {'form': form}
            return render(request, 'index.html', context)
    else:
        form = PatientForm()
    return render(request, 'index.html', {'form': form})

def score(request, patient_id):
    patient = Patient.objects.get(patient_id=patient_id)
    return render(request, 'score.html', {'patient': patient})

def search(request):
    patient = Patient.objects.all()
    return render(request, 'search.html', {'patient': patient})

