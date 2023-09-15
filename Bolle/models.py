import json

from django.db import models


# Create your models here.
class Bolla_dst(models.Model):
    name = models.CharField(max_length=100, unique=True)
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    alt_dst = models.BooleanField(default=False)


    def to_dict(self):
        return {
            'usr': self.name,
            'riga1': self.line1,
            'riga2': self.line2,
            'citta': self.city,
            'cap': self.zip,
            'prov': self.province,
            'paese': self.country.capitalize()
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_array(self):
        return [self.name, self.line1, self.city, self.zip, self.country]


class Bolla(models.Model):
    data = models.DateField()
    descrizioni = models.JSONField(default=dict)
    qta = models.JSONField(default=dict)
    um = models.JSONField(default=dict)
    note = models.JSONField(default=dict)
    lavorazione = models.CharField(max_length=50)
    respSpedizione = models.CharField(max_length=50)
    dataTrasp = models.DateField()
    aspetto = models.CharField(max_length=50)
    dst = models.ForeignKey(Bolla_dst, on_delete=models.PROTECT, to_field='id', related_name='dst')
    sameAddress = models.BooleanField(default=True)
    dst2 = models.ForeignKey(Bolla_dst, on_delete=models.PROTECT, to_field='id', related_name='dst2',null=True )
    number = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        unique_together = ('number', 'year')
    def to_json(self):
        if self.sameAddress:
            r = {
                'data': str(self.data.day) + '/' + str(self.data.month) + '/' + str(self.data.year),
                'descrizioni': self.descrizioni['descrizioni'],
                'qta': self.qta['qta'],
                'um': self.um['um'],
                'note': self.note['note'],
                'lavorazione': self.lavorazione,
                'respSpedizione': self.respSpedizione,
                'dataTrasp': str(self.dataTrasp.day) + '/' + str(self.dataTrasp.month) + '/' + str(self.dataTrasp.year),
                'aspetto': self.aspetto,
                'dst': self.dst.to_dict(),
                'sameAddress': self.sameAddress,
                'dst2':[],
                'year': str(self.year),
                'number': str(self.number)
            }
        else:
            r = {
                'data': str(self.data.day) + '/' + str(self.data.month) + '/' + str(self.data.year),
                'descrizioni': self.descrizioni['descrizioni'],
                'qta': self.qta['qta'],
                'um': self.um['um'],
                'note': self.note['note'],
                'lavorazione': self.lavorazione,
                'respSpedizione': self.respSpedizione,
                'dataTrasp': str(self.dataTrasp.day) + '/' + str(self.dataTrasp.month) + '/' + str(self.dataTrasp.year),
                'aspetto': self.aspetto,
                'dst': self.dst.to_dict(),
                'sameAddress': self.sameAddress,
                'dst2': self.dst2.to_array(),
                'year': str(self.year),
                'number': str(self.number)
            }

        return json.dumps(r)

    def __str__(self):
        return f"{self.data} - {self.descrizioni} - {self.qta} - {self.um} - {self.note} - {self.lavorazione} - {self.respSpedizione} - {self.dataTrasp}  - {self.aspetto} - {self.dst} - {self.sameAddress} - {self.dst2} - {self.number} - {self.year}"

