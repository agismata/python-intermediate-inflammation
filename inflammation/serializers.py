from inflammation.models import Patient
import json

class PatientSerializer:
    model = Patient

    @classmethod
    def save(cls, instances, path):
        raise NotImplementedError

    @classmethod
    def load(cls, path):
        raise NotImplementedError


class PatientJSONSerializer(PatientSerializer):
    @classmethod
    def save(cls, instances, path):
        data = [{
            'name': instance.name,
            'observations': instance.observations,
        } for instance in instances]

        with open(path, 'w') as jsonfile:
            json.dump(data, jsonfile)

    @classmethod
    def load(cls, path):
        with open(path) as jsonfile:
            data = json.load(jsonfile)

        return [cls.model(**d) for d in data]