from django.db import models

# Create your models here.
class TestTable(models.Model):  # Class names should follow PascalCase
    id = models.AutoField(primary_key=True, serialize=True)
    name = models.CharField(max_length=50, null=False, blank=False)  # Removed extra comma
    email = models.CharField(max_length=100)
    contact = models.BigIntegerField(null=True)

    class Meta:
        db_table = 'test_table'
