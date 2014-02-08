from django.db import models
import psycopg2



class Persons(models.Model):
	name=models.CharField(max_length=100)
	passw=models.CharField(max_length=100)
class Book(models.Model):
	bname=models.CharField(max_length=100)
	number=models.CharField(max_length=100)
        idname=models.CharField(max_length=100)
