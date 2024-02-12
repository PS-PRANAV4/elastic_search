from django_elasticsearch_dsl import fields,Document,Index

from .models import Student
from django_elasticsearch_dsl.registries import registry

PUBLISHER_INDEX = Index('student')
PUBLISHER_INDEX.settings(number_of_shards=1,number_of_replicas=1)



@PUBLISHER_INDEX.doc_type
class StudentDocument(Document):
    id = fields.IntegerField(attr='id')
    studentname = fields.TextField(fields={
        "raw":{
            "type":"keyword"
        }
    })
    place = fields.TextField(fields={
        "raw":{
            "type":"keyword"
        }
    })
    designation = fields.TextField(fields={
        "raw":{
            "type":"keyword"
        }
    })
    email = fields.TextField(fields={
        "raw":{
            "type":"keyword"
        }
    })
   