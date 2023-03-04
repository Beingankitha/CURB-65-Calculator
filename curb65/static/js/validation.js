const patientIdField = document.getElementById('id_patient_id');
const dobField = document.getElementById('id_dob');
const confusionField = document.getElementById('id_confusion');
const bloodUreaField = document.getElementById('id_blood_urea');
const respiratoryRateField = document.getElementById('id_respiratory_rate');
const systolicBpField = document.getElementById('id_systolic_bp');
const diastolicBpField = document.getElementById('id_diastolic_bp');

// Add event listener to form submit button
document.querySelector('#patient-form').addEventListener('submit', function(event) {
  // Prevent form submission
  event.preventDefault();

  // Validate patient ID field
  const patientId = patientIdField.value;
  const patientIdRegex = /^P[0-9]{6}$/;
  if (!patientIdRegex.test(patientId)) {
    patientIdField.setCustomValidity('Patient ID must start with P and be followed by 6 digits.');
    return;
  }

  // Validate other fields
  if (!dobField.value) {
    dobField.setCustomValidity('Date of birth is required.');
    return;
  }
  if (!confusionField.checked && !confusionField.value) {
    confusionField.setCustomValidity('Either Confusion or GCS score is required.');
    return;
  }
  if (!bloodUreaField.value) {
    bloodUreaField.setCustomValidity('Blood Urea level is required.');
    return;
  }
  if (!respiratoryRateField.value) {
    respiratoryRateField.setCustomValidity('Respiratory rate is required.');
    return;
  }
  if (!systolicBpField.value) {
    systolicBpField.setCustomValidity('Systolic blood pressure is required.');
    return;
  }
  if (!diastolicBpField.value) {
    diastolicBpField.setCustomValidity('Diastolic blood pressure is required.');
    return;
  }

  // Submit form
  event.target.submit();
});