import datetime

org_data = {
    'org_name': 'Non Profit',
    'org_address': '123 main st',
    'org_city': 'Cityville',
    'org_state': 'NC',
    'org_zip_code': '12345',
    'org_phone': '(123) 456-7890'
}

agency_data = {
    'agency_name': 'Agency',
    'agency_dept': 'DEPT',
    'agency_address': '456 second st',
    'agency_city': 'Cityville',
    'agency_state': 'NC',
    'agency_zip_code': '12345'
}

rep_data = {
    'rep_name': 'Lorem Ipsum',
    'rep_title': 'Title'
}

data = {**org_data, **agency_data, **rep_data, 'date': datetime.date.today()}