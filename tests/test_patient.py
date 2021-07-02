"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient, Doctor

    name_doc = 'George'
    doc = Doctor(name=name_doc)

    p1 = doc.add_patient('Alice' , '../data/inflammation-01.csv')
    p2 = doc.add_patient('Djalma', '../data/inflammation-02.csv')
    p3 = doc.add_patient('Chiara', '../data/inflammation-03.csv')

    print(doc.patients[0].name)
    print(doc.patients_name)
    print(doc.patient_list())
    # print(doc.patients[0].inflammation_measurements[0])