from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class Department(Model):

    class Meta:
        table_name = 'flask_pynamodb_example_department'
        host = "http://localhost:8000"

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()


class Role(Model):

    class Meta:
        table_name = 'flask_pynamodb_example_roles'
        host = "http://localhost:8000"

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()


class Employee(Model):

    class Meta:
        table_name = 'flask_pynamodb_example_employee'
        host = "http://localhost:8000"

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()
    # TODO DynamoDB doesn't have any date function so we can't set a default of now()
    hired_on = UTCDateTimeAttribute(default=datetime.now)
    department_id = UnicodeAttribute(null=False)
    role_id = UnicodeAttribute(null=False)
