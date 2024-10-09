# nis_app/models.py
from django.db import models

class Country(models.Model):
    name_tk = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    name_ja = models.CharField(max_length=100)
    population = models.BigIntegerField()
    flag = models.ImageField(upload_to="flags/", blank=True, null=True)
    gdp = models.DecimalField(max_digits=15, decimal_places=2)
    innovation_index_rank = models.IntegerField()
    description_tk = models.TextField()
    description_en = models.TextField()
    description_ja = models.TextField()
    huge_data_tk = models.TextField()
    huge_data_en = models.TextField()
    huge_data_ja = models.TextField()
    
    def __str__(self):
        return self.name_en

class InnovationPractice(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year = models.IntegerField()
    description_tk = models.TextField()
    description_en = models.TextField()
    description_ja = models.TextField()
    success_case = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.country.name_en} - {self.year}"
    

class Message(models.Model):
    fullname = models.CharField(max_length=55)
    gmail = models.CharField(max_length=55)
    title = models.CharField(max_length=55)
    desc = models.TextField()
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.fullname