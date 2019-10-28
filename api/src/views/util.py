
def __is_string(string):
    if (not isinstance(string, str)) or (not string.strip()):
        return False
    return True

def validate_movie(obj):
    errors = []
    if not __is_string(obj.title):
        errors.append("title should be a string.")
    if not __is_string(obj.release_date):
        errors.append("Date is Invalid!")
    if errors:
        return errors
    return True

def validate_actor(obj):
    errors = []
    if not __is_string(obj.name):
        errors.append("name should be a string.")
    if not __is_string(obj.gender):
        errors.append("Gender should be a string.")
    if not isinstance(obj.age, int):
        errors.append("Age should be an integer.")
    if errors:
        return errors
    return True

RECORDS_PER_PAGE = 10

def paginate(page, records):
    """ return paginated questions """
    start = (page - 1) * RECORDS_PER_PAGE
    end = start + RECORDS_PER_PAGE
    allRecords = []

    for record, category in records:
        record = record.format()
        record['category_id'] = record['category']
        record['category'] = category
        allRecords.append(record)

    current_records = allRecords[start:end]

    return current_records
