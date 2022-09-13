#from mongoengine import  EmbeddedDocument 
from django_mongoengine import Document, fields, EmbeddedDocument
 
from django_mongoengine.fields.djangoflavor import EmbeddedDocumentField

#from stringfield import formfield

class Designation(EmbeddedDocument):
    
    name = fields.StringField(max_length=250)

    def __str__(self):
        return self.name 


class Employee(Document):
        
        

    name = fields.StringField(max_length=250, editable = True)
    username = fields.StringField(max_length=250)
    email = fields.EmailField()
    emp_id = fields.IntField()
    designation = fields.EmbeddedDocumentField(Designation)
    file = fields.FileField()
    

    def __str__(self):
        return self.name

        #meta = { 'abstract': True }


class Department(Document):
    name = fields.StringField(max_length=250)
    file = fields.FileField()

    def __str__(self):
        return self.name

    # meta = {
    #     'abstract': True
    # }
