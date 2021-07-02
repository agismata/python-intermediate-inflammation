
import numpy as np
import numpy.testing as npt
import pytest
from inflammation.models import Patient
from inflammation.serializers import PatientJSONSerializer

def test_patients_json_serializer():
    patients = [
        Patient('Alice', observations=[1, 2, 3]),
        Patient('Bob', observations=[3, 4, 5]),
    ]

    output_file = 'patients.json'
    PatientJSONSerializer.save(patients, output_file)

    patients_new = PatientJSONSerializer.load(output_file)

    assert patients_new[0].name == 'Alice'
    assert patients_new[1].observations == [3, 4, 5]