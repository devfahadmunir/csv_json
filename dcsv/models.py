from django.db import models

# Create your models here.


class csvdata(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(null=True)
    csv_file = models.FileField(upload_to='csv/')
    json_data = models.TextField(null=True)

    def __str__(self):
        return self.name
