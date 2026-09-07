import re

# List of medical records
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

# This function checks whether the VALUES inside a medical record are valid or not.

def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    # Stores the validation rules for each value
    constraints = {
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch(r'p\d+', patient_id, re.IGNORECASE),
        'age': isinstance(age, int) and age >= 18,
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE)
    }
    # Go through every key/value pair in constraints. If the VALUE is False, that field is invalid.
    return [key for key, value in constraints.items() if not value]

# Checks the entire list of medical records
def validate(data):
    is_sequence = isinstance(data, (list, tuple))

    # If data isn't a list or tuple, stop immediately.
    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
        
    is_invalid = False

    # These are the keys that EVERY medical record is supposed to have.
    key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])

    # Goes through each record and its position
    for index, dictionary in enumerate(data):
        # Checks if the current item is a dictionary
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        # Checks if the dictionary has the correct KEYS
        if set(dictionary.keys()) != key_set:
            print(f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.')
            is_invalid = True
            continue

        # Checks if the VALUES inside the dictionary are valid
        invalid_records = find_invalid_records(**dictionary)

        # Goes through each invalid value
        for key in invalid_records:
            print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
            is_invalid = True

    # Returns False if anything was invalid
    if is_invalid:
        return False
    # Everything passed the validation
    print('Valid format.')
    return True

validate(medical_records)