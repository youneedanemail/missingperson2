from django.db import models
from datetime import datetime

class missingperson (models.Model):
    date_missing= models.DateField(default=datetime.today, blank=True)
    last_name=models.CharField(max_length =30)
    first_name=models.CharField(max_length =30)
    age_at_missing=models.IntegerField(default =0)
    city=models.CharField(max_length =30)
    state=models.CharField(max_length =30)
    gender=models.CharField(max_length =30)
    race=models.CharField(max_length =30)

    def __str__ (self):
        return (self.first_name)

    @property
    def full_name (self) :
        return '% %' % (self.first_name, self.last_name)