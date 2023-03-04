from django.test import TestCase
from .models import Patient
from .views import calculate_score
import unittest

class CURB65CalculatorTestCase(unittest.TestCase):
    
    def setUp(self):
        # Create test patient objects with different values
        self.patient1 = Patient.objects.create(patient_id='P001', dob='1950-01-01', confusion=True, blood_urea=8, respiratory_rate=20, systolic_bp=110, diastolic_bp=70)
        self.patient2 = Patient.objects.create(patient_id='P002', dob='1970-01-01', confusion=False, blood_urea=4, respiratory_rate=28, systolic_bp=80, diastolic_bp=60)
        self.patient3 = Patient.objects.create(patient_id='P003', dob='1990-01-01', confusion=True, blood_urea=5, respiratory_rate=10, systolic_bp=150, diastolic_bp=90)
    
    def tearDown(self):
        # Delete test patient objects
        self.patient1.delete()
        self.patient2.delete()
        self.patient3.delete()
    
    def test_score_calculation(self):
        # Test score calculation for different patient objects
        calculate_score(self.patient1)
        self.assertEqual(self.patient1.score, 5)
        calculate_score(self.patient2)
        self.assertEqual(self.patient2.score, 2)
        calculate_score(self.patient3)
        self.assertEqual(self.patient3.score, 2)
    
    def test_null_values(self):
        # Test score calculation for null values
        self.patient4 = Patient.objects.create(patient_id='P004', dob='1980-01-01', confusion=None, blood_urea=None, respiratory_rate=None, systolic_bp=None, diastolic_bp=None)
        calculate_score(self.patient4)
        self.assertEqual(self.patient4.score, 0)
        self.patient4.delete()
        
    def test_edge_cases(self):
        # Test score calculation for edge cases
        self.patient5 = Patient.objects.create(patient_id='P005', dob='1955-01-01', confusion=True, blood_urea=7, respiratory_rate=30, systolic_bp=89, diastolic_bp=59)
        calculate_score(self.patient5)
        self.assertEqual(self.patient5.score, 5)
        self.patient5.delete()


