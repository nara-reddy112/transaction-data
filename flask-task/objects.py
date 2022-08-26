from mongoengine import *
from mongoengine.fields import StringField, ListField

class Transaction(DynamicDocument):
	# In mongodb we have _id 
    transactionId = StringField(required=True)
    profileId =  StringField(required = True)
    transactionAmount =  ListField(default=[])
    transactionDatetime = DateField(required=True)
    

class Product(DynamicDocument):
    productId = StringField(required=True)
    productName =  StringField(required = True)
    productManufacturingCity =  StringField(required = True)
    
