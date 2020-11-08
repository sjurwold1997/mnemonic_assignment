from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=25)
    available_cash = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    description = models.CharField(max_length=50)
    executed_time = models.DateTimeField(auto_now=True)
    success = models.BooleanField(default=False)
    cash_amount = models.FloatField()
    source_account = models.ForeignKey(Account, related_name="source_account", on_delete=models.CASCADE)
    destination_account = models.ForeignKey(Account, related_name="destinatuon_account", on_delete=models.CASCADE)

    def __str__(self):
        return self.description