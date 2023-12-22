from utils.models import BaseModel
from django.db import models
from accounts.models.profile import Company

class Zone(BaseModel):
    name = models.CharField(max_length=255)

class Country(BaseModel):
    name = models.CharField(max_length=255)

class State(BaseModel):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE)

class City(BaseModel):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

class Pincode(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Address(BaseModel):
    ADDRESS_TYPE = (('Business', 'Business'),('Residential','Residential'))

    address_type = models.CharField(max_length=255, choices=ADDRESS_TYPE, default= 'Business')
    street_address = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255,null=True, blank=True)
    locality = models.CharField(max_length=255,null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    pincode = models.ForeignKey(Pincode, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.city}, {self.country} - {self.pincode}'
    
    def save(self, *args, **kwargs):
        if not self.zone_id: # type: ignore
            self.zone = self.state.zone
        super().save()