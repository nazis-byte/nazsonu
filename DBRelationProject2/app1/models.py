from django.db import models
class PersonModel(models.Model):
    aadhar = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=30)
    contact = models.IntegerField()
    address= models.TextField()
    def __str__(self):
        return self.pname

class PassportModel(models.Model):
    pno = models.IntegerField(primary_key=True)
    p_details = models.OneToOneField(PersonModel, on_delete=models.CASCADE)
