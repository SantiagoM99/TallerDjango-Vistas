from variables.models import Variable
from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(msr_pk):
    measurement = Measurement.objects.get(pk=msr_pk)
    return measurement

def update_measurement(msr_pk, new_msr):
    measurement = get_measurement(msr_pk)
    measurement.place = new_msr["place"]
    measurement.save()
    return measurement

def create_measurement(msr):
    variable_id = Variable.objects.get(pk=msr["variable"])
    measurement = Measurement(variable=variable_id, value=msr["value"], place=msr["place"], unit=msr["unit"])
    measurement.save()
    return measurement

def delete_measurement(msr_pk):
    measurement = get_measurement(msr_pk)
    measurement.delete()
    return measurement