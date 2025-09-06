import datetime

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

data = {**agency_data, **rep_data, 'date': datetime.date.today()}